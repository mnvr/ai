from openai import OpenAI

client = OpenAI()
context = []

def chat(client, model):
    completion = client.chat.completions.create(
        messages=context,
        model=model
    )
    message = completion.choices[0].message
    context.append(message)
    print(message.content)

while True:
    prompt = input(">>> ")
    context.append({
        "role": "user",
        "content": prompt
    })
    chat(client, 'gpt-4o-mini')
