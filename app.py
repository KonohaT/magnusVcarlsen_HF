import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

from transformers import pipeline
generator2 = pipeline('text-generation', model='meta-llama/Llama-2-7b-chat-hf')

prompt = "Return an opening move in chess."
generated_text = generator2(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
print(generated_text)