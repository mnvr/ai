from transformers import pipeline

gpt2 = pipeline('text-generation', model='gpt2')
gpt2xl = pipeline('text-generation', model='gpt2-xl')
smol = pipeline('text-generation', model='HuggingFaceTB/SmolLM2-135M')

def show(seqs):
    print('\n•\n'.join(s['generated_text'] for s in seqs))

def make(label, f):
    def g(prompt):
        print(f"\n{label} ==\n")
        return show(f(prompt, max_new_tokens=150, num_return_sequences=3))
    return g

while True:
    prompt = input(">>> ")
    gen = [make("gpt2", gpt2),
           make("gpt2-xl", gpt2xl),
           make("smol", smol)]
    for g in gen:
        g(prompt)
