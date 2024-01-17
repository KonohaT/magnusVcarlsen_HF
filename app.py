import streamlit as st

from transformers import pipeline
generator2 = pipeline('text-generation', model='gpt2')

prompt = "Return an opening move in chess."
generated_text = generator2(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
st.write(generated_text)