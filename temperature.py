from openai import OpenAI
from rich.console import Console
from rich.tree import Tree
from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser
from time import perf_counter

client = OpenAI()

models = ["gpt-4o-mini", "mistral-small-2503", "DeepSeek-V3-0324"]
temps = [0.1, 0.7, 1, 2]

input = "List 10 different random animals. No explanations, just a comma separated list."

console = Console(highlight=False, record=True)

def print_tree(completion):
    tree = Tree("", style="dim")
    for key, value in completion.model_dump().items():
        tree.add(f"{key}: {value!s:.999}")
    console.print(tree, style="gray50")

def save_transcript():
    base = Path(__file__).stem
    date = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = Path("transcripts") / f"{base}-{date}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    console.save_text(path.as_posix())
    print(f"Wrote {path}")

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
    console.rule(f"{model} / temp {temp:.1f} / {tokens} tokens / {elapsed:.1f}s")
    console.print(output)
    print_tree(completion)
    console.print()

def do_runs():
    console.print(f"\nPrompt: [i]{input}[/i]\n")

    for temp in temps:
        for model in models:
            run(input, model, temp)
            if args.self_test:
                return

parser = ArgumentParser()
parser.add_argument("--self-test", action="store_true", help="Run a POST (Power-On Self-Test)")
args = parser.parse_args()

do_runs()
save_transcript()
