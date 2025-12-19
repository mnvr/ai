from transformers import pipeline

generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M")
prompt = "The secret to baking a good cake is "
seqs = generator(prompt, max_new_tokens=30, num_return_sequences=5)
print(*[s['generated_text'] for s in seqs], sep='\n')
