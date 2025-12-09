from openai import OpenAI
from argparse import ArgumentParser
import re
from pathlib import Path
from datetime import datetime
from pprint import pprint

def main():
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", required=True, help="The model to use")
    args = parser.parse_args()

    transcript_file = None
    client = None
    context = []

    try:
        while True:
            prompt = input('\033[1m>\033[0m ')
            if not transcript_file:
                transcript_file = open(transcript_path(prompt), 'a')
                client = OpenAI()
            chat(client, args.model, context, prompt, transcript_file)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        if transcript_file:
            transcript_file.close()

def transcript_path(input):
    base = Path(__file__).stem
    slug = re.sub(r"[^a-z0-9]+", "-", input.lower()).strip("-")[:15]
    date = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = Path("transcripts") / f"{base}-{slug}-{date}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

def chat(client, model, context, prompt, transcript_file):
    def log(label, s):
        print(f"{datetime.now()} {label}:", file=transcript_file)
        print(s, file=transcript_file, flush=True)

    log("prompt", prompt)

    context.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(model=model, messages=context, temperature=1.0, reasoning_effort="high")

    log("completion", "")
    pprint(completion, stream=transcript_file)

    message = completion.choices[0].message
    context.append(message)

    if hasattr(message, "reasoning_content"):
        reasoning_content = getattr(message, "reasoning_content")
        log("reasoning_content:", reasoning_content)

        print("\033[37m") # gray
        print(reasoning_content)
        print("\033[0m")

    content = message.content
    log("content", content)
    print(content)
    print("")

if __name__ == "__main__":
    main()
