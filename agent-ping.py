from openai import OpenAI
import subprocess
import json

client = OpenAI()
messages = []

tools = [{
    "type": "function",
    "function": {
        "name": "ping",
        "description": "ping some host on the internet",
        "parameters": {
            "type": "object",
            "properties": {
                "host": {
                    "type": "string",
                    "description": "hostname or IP",
                }
            },
            "required": ["host"]
        }
    }
}]

def ping(host=""):
    try:
        result = subprocess.run(
            ["ping", "-c", "5", host],
            text=True,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE)
        return result.stdout
    except Exception as e:
        return f"error: {e}"

def handle_tool_call(tool_call):
    name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    print(f"tool call: {name} {arguments}")
    content = ping(**arguments)
    return {"role": "tool", "tool_call_id": tool_call.id, "content": content}

def call():
    return client.chat.completions.create(model="gpt-5.2", messages=messages, tools=tools)

def process(input):
    messages.append({"role": "user", "content": input})
    while True:
        completion = call()
        message = completion.choices[0].message
        messages.append(message)
        if message.tool_calls:
            for tool_call in message.tool_calls:
                messages.append(handle_tool_call(tool_call))
        elif message.content:
            break
    return message.content

while True:
    line = input(">>> ")
    output = process(line)
    print(output)
