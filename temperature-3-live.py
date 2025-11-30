from openai import OpenAI
from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser
from time import perf_counter
import re
from rich.console import Console
from rich.rule import Rule
from rich.pretty import Pretty
from rich.highlighter import NullHighlighter
from rich.live import Live
from rich.table import Table
from rich.spinner import Spinner

client = OpenAI()

models = ["gpt-4o-mini", "mistral-small-2503", "DeepSeek-V3-0324"]
temps = [0.1, 0.7, 1, 2]

input = "List 10 different random animals. No explanations, just a comma separated list."

parser = ArgumentParser()
parser.add_argument(
    "--self-test", action="store_true", help="Run a POST (Power-On Self-Test)"
)
args = parser.parse_args()

console = Console(highlight=False)

def transcript_path():
    base = Path(__file__).stem
    slug = re.sub(r"[^a-z0-9]+", "-", input.lower()).strip("-")[:15]
    date = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = Path("transcripts") / f"{base}-{slug}-{date}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

transcript_file = open(transcript_path(), "w")
file_console = Console(file=transcript_file, force_terminal=False, width=120)

def log_print(*args, **kwargs):
    console.print(*args, **kwargs)
    file_console.print(*args, **kwargs)

def print_tree(completion):
    pretty = Pretty(
        completion.model_dump(), max_string=999, highlighter=NullHighlighter()
    )
    log_print(pretty, style="gray50")

def render_progress(inference):
    table = Table(box=None, expand=True)
    table.add_column("", width=20, no_wrap=True, style="gray50")
    table.add_column("", width=6, no_wrap=True, style="gray50")
    table.add_column(input, ratio=1, overflow="ellipsis", no_wrap=True)

    for (model, temp), status in inference.items():
        table.add_row(
            model, f"{temp:.1f}",
            Spinner("dots", style="gray50") if status is None else status
        )

    return table

def run(input, model, temp):
    start = perf_counter()
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": input}],
        temperature=temp,
    )
    elapsed = perf_counter() - start
    output = completion.choices[0].message.content
    tokens = completion.usage.total_tokens

    log_print(Rule(f"{model} / temp {temp:.1f} / {tokens} tokens / {elapsed:.1f}s"))
    log_print(output)
    print_tree(completion)
    log_print("")

    return output.split("\n")[0][:200]

def do_runs():
    inference = {}  # (model, temp) -> string | None
    for temp in temps:
        for model in models:
            t = temp if not (model == "mistral-small-2503" and temp > 1) else 1.0
            inference[(model, t)] = None

    console.print("")
    log_print(f"Prompt: [i]{input}[/i]\n")

    with Live(render_progress(inference), console=console) as live:
        for model, temp in inference:
            inference[(model, temp)] = run(input, model, temp)
            live.update(render_progress(inference))
            if args.self_test:
                return

try:
    do_runs()
except KeyboardInterrupt:
    pass

console.print("")
console.print(f"Wrote {transcript_file.name}", style="gray50")
transcript_file.close()
