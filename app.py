import streamlit as st
from gtts import gTTS
from io import BytesIO
from pygame import mixer

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')  # Create gTTS object with text and language
    fp = BytesIO()  # Create an in-memory file-like object
    tts.write_to_fp(fp)  # Write audio content to the file-like object
    fp.seek(0)  # Move cursor to the beginning of the file-like object
    mixer.init()  # Initialize the audio mixer
    mixer.music.load(fp)  # Load audio data from the file-like object
    mixer.music.play()  # Play the audio

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
