from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Tell me a joke"}
    ]
)

print(completion)
print(completion.choices[0].message.content)
