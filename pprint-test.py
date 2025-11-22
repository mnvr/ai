from openai import OpenAI
from pprint import pprint

client = OpenAI()

completion = client.chat.completions.create(
    model="DeepSeek-V3.1",
    messages=[
        {"role": "user", "content": "Tell me a joke"}
    ]
)

print("pprint(completion.model_dump())")
pprint(completion.model_dump())
print("\n\npprint(completion.model_dump_json())")
pprint(completion.model_dump_json())
print("\n\n print(completion.model_dump_json())")
print(completion.model_dump_json())
print("\n\n print(completion.model_dump_json(indent=2))")
print(completion.model_dump_json(indent=2))
