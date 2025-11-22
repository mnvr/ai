from openai import OpenAI

print(OpenAI().chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "List 10 different random animals. No explanations, just a comma separated list."}],
    temperature=2,
).choices[0].message.content)
