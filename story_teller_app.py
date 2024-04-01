import streamlit as st
from transformers import pipeline

generator = pipeline("text-generation")

def generate_story(prompt, max_length=200):
    story = generator(prompt, max_length=max_length, do_sample=True)[0]['generated_text']
    return story

def main():
    st.title("Storytelling Application")

    prompt = st.text_input("Enter a Story Prompt:", "Once upon a time,")

    if st.button("Generate Story"):
        with st.spinner("Generating story......"):
            story = generate_story(prompt)
            st.write(story)
        
if __name__ == "__main__":
    main()
