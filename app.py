import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
import pygame
from textsum.summarize import Summarizer


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')  
    tts.save('output.mp3')  
    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()


def main():
    st.title("YouTube Transcript Reader")

    
    video_url = st.text_input("Enter YouTube video URL:")

    
    if st.button("Get summary"):
        if video_url:
            try:
                video_id = video_url.split("v=")[1] 
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
                transcript_text = ' '.join([t['text'] for t in transcript_list])
                st.write("Transcript:")
                summRY = summarizer.summarize_string(transcript_text)
                print(f'{summRY}')
                
            except Exception as e:
                st.write("Error occurred:Fix it")
        else:
            st.write("Please enter a valid YouTube video URL.")

if __name__ == '__main__':
    main()
