import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
import pygame

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')  # Create gTTS object with text and language
    tts.save('output.mp3')  # Save the synthesized audio as 'output.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()

# Streamlit app
def main():
    st.title("YouTube Transcript Reader")

    # Input field for YouTube video URL
    video_url = st.text_input("Enter YouTube video URL:")

    # Button to fetch transcript and read out
    if st.button("Get Transcript"):
        if video_url:
            try:
                video_id = video_url.split("v=")[1]  # Extract video ID from URL
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
                transcript_text = ' '.join([t['text'] for t in transcript_list])
                st.write("Transcript:")
                st.write(transcript_text)
                st.write("Reading Transcript:")
                text_to_speech(transcript_text)
            except Exception as e:
                st.write("Error occurred:", e)
        else:
            st.write("Please enter a valid YouTube video URL.")

if __name__ == '__main__':
    main()
