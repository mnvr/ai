from openai import OpenAI

client = OpenAI()

models = ["gpt-4o-mini", "mistral-small-2503", "DeepSeek-V3-0324"]
temps = [0.1, 0.7, 1, 2]

input = "List 10 different random animals. No explanations, just a comma separated list."

def run(input, model, temp=1.0):
    if model == "mistral-small-2503" and temp > 1:
        temp = 1.0
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": input}],
        temperature=temp,
    )
    output = completion.choices[0].message.content
    print(f"{model:15.15s} {temp:>4.1f} {output}")

for temp in temps:
    for model in models:
        run(input, model, temp)

