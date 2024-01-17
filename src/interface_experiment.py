import transformers

model_id = "BlueSunflower/gpt2-medium-chess"
text_generator = transformers.pipeline("text-generation", model = model_id)
input_text = "1-0 2995 3110 1.e4 e5 2.Nf3 Nc6"

generated = text_generator(input_text, max_new_tokens = 500)[0]["generated_text"]
print(generated)
