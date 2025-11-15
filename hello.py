from openai import OpenAI

client = OpenAI(
  base_url="https://ente.openai.azure.com/openai/v1"
)

response = client.responses.create(
  model="gpt-5.1",
  input="Hello, world!"
)

print(response.output_text)
