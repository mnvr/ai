from openai import OpenAI
from rich.console import Console
from rich.rule import Rule
from rich.pretty import Pretty
from rich.highlighter import NullHighlighter
from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser
from time import perf_counter

client = OpenAI()

models = ["gpt-4o-mini", "mistral-small-2503", "DeepSeek-V3-0324"]
temps = [0.1, 0.7, 1, 2]

input = "List 10 different random animals. No explanations, just a comma separated list."

parser = ArgumentParser()
parser.add_argument("--self-test", action="store_true", help="Run a POST (Power-On Self-Test)")
args = parser.parse_args()

console = Console(highlight=False)

def transcript_path():
    base = Path(__file__).stem
    date = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = Path("transcripts") / f"{base}-{date}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    console.print(f"Transcript will be saved in {path}")
    return path

transcript_file = open(transcript_path(), "w")
file_console = Console(file=transcript_file, force_terminal=False, width=120)

def log_print(*args, **kwargs):
    console.print(*args, **kwargs)
    file_console.print(*args, **kwargs)

def print_tree(completion):
    pretty = Pretty(completion.model_dump(),
                    max_string=999,
                    highlighter=NullHighlighter())
    log_print(pretty, style="gray50")

def run(input, model, temp=1.0):
    start = perf_counter()
    if model == "mistral-small-2503" and temp > 1:
        temp = 1.0
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

def do_runs():
    console.print("")
    log_print(f"Prompt: [i]{input}[/i]\n")

    for temp in temps:
        for model in models:
            run(input, model, temp)
            if args.self_test:
                return


do_runs()

transcript_file.close()
