# Transformers

[Transformers](https://huggingface.co/docs/transformers/quicktour) is HuggingFace's Python library that provides a collection of pre-implemented model architectures and tokenizer classes, plus convenient APIs to fetch the weights and token data from a HF repository. The actual inference / execution happens on an execution engine, PyTorch by default.

HF has the data. Transformers has the blueprint. PyTorch executes. Transformers provides convenient abstractions like "pipelines" to orchestrate all this.

e.g. generating text using the OG

```py
from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')
generator("The gift of mathematics is ", max_new_tokens=20)
```

A bit more explicitly:

```py
from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
encoded_input = tokenizer("I worked at a ", return_tensors='pt')
output = model(**encoded_input)
```

The output is specific to GPT2 and will need decoding. And we had to specify the exact model and tokenizer classes. At an intermediate between the above and the pipeline are the "Auto" classes:

```py
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModelForCausalLM.from_pretrained('gpt2')
encoded_input = tokenizer("I worked at a ", return_tensors='pt')
generated_ids = model.generate(**encoded_input)
print(tokenizer.batch_decode(generated_ids)[0])
```

Example using another model:

```py
model = AutoModelForCausalLM.from_pretrained("HuggingFaceTB/SmolLM2-135M")
tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-135M")
model_inputs = tokenizer("The secret to baking a good cake is ", return_tensors="pt")
generated_ids = model.generate(**model_inputs, max_length=30)
print(tokenizer.batch_decode(generated_ids)[0])
```
