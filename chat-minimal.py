from openai import OpenAI

client = OpenAI()
context = []

def chat(prompt):
    context.append({"role": "user", "content": prompt})
    completion = client.chat.completions.create(
        messages=context,
        model='gpt-5.1'
    )
    message = completion.choices[0].message
    context.append(message)
    return message.content

while True:
    prompt = input(">>> ")
    result = chat(prompt)
    print(result)
