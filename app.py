import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
import pygame


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()


def main():
    st.title("YouTube Transcript Reader")

    video_url = st.text_input("Enter YouTube video URL:")

    if st.button("Get Transcript"):
        if video_url:
            try:
                video_id = video_url.split("v=")[1]
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
                transcript_text = ' '.join([t['text'] for t in transcript_list])
                st.write("Transcript:")
                st.write(transcript_text)
                st.session_state.transcript_text = transcript_text  # Store transcript in session state
            except Exception as e:
                st.write("Error occurred:", e)
        else:
            st.write("Please enter a valid YouTube video URL.")

    if st.button("Read Transcript") and 'transcript_text' in st.session_state:
        transcript_text = st.session_state.transcript_text
        st.write("Reading Transcript:")
        text_to_speech(transcript_text)

    # Audio playback control buttons
    if 'transcript_text' in st.session_state:
        if st.button("Play"):
            pygame.mixer.music.unpause()  # Resume playback if paused or stopped
        if st.button("Pause"):
            pygame.mixer.music.pause()  # Pause playback
