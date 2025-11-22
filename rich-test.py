from openai import OpenAI
from rich.console import Console
from rich.pretty import Pretty
from rich.tree import Tree

console = Console()

client = OpenAI()

model="DeepSeek-V3.1"

completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Tell me a joke"}
    ]
)

console.print_json(completion.model_dump_json())

# For "inline when it fits"
console.print(Pretty(completion.model_dump()))

# Tree
tree = Tree(model)
for key, value in completion.model_dump().items():
    tree.add(f"{key}: {value}")

console.print(tree)
