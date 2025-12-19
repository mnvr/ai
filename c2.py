from transformers import pipeline

gpt2 = pipeline('text-generation', model='gpt2')
smol = pipeline('text-generation', model='HuggingFaceTB/SmolLM2-135M')

def show(seqs):
    print('\n•\n'.join(s['generated_text'] for s in seqs))

while True:
    prompt = input(">>> ")
    print("gpt2:")
    show(smol(prompt, max_new_tokens=150, num_return_sequences=3))
    print("smol:")
    show(gpt2(prompt, max_new_tokens=150, num_return_sequences=3))
