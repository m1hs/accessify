import streamlit as st
from gtts import gTTS
import pygame


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')  
    tts.save('output.mp3')  
    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()


def main():
    st.title("Screen Reader for the Elderly")

    
    user_text = st.text_input("Enter text:")

    
    if st.button("Read"):
        if user_text:
            st.write(f"Reading: {user_text}")
            text_to_speech(user_text)
        else:
            st.write("Please enter some text above.")

if __name__ == '__main__':
    main()
