import streamlit as st
import pyttsx3

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

# Streamlit app
def main():
    st.title("Screen Reader for the Elderly")

    # Text input for the user to enter text
    user_text = st.text_input("Enter text:")

    # Button to trigger text-to-speech conversion
    if st.button("Read"):
        if user_text:
            st.write(f"Reading: {user_text}")
            text_to_speech(user_text)
        else:
            st.write("Please enter some text above.")

if __name__ == '__main__':
    main()
