from openai import OpenAI

client = OpenAI(
  base_url="https://ente.openai.azure.com/openai/v1"
)

print(client.models.list())
