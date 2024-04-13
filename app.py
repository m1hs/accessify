import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from textsum.summarize import Summarizer
from gtts import gTTS
import pygame

audio_playing = False

def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([t['text'] for t in transcript_list])
        return transcript_text
    except Exception as e:
        st.error(f"Error occurred while fetching transcript: {e}")
        return None

def summarize_transcript(transcript_text):
    summarizer = Summarizer()
    summary = summarizer.summarize_string(transcript_text)
    return summary

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')

def play_audio_blocking():
    global audio_playing
    audio_playing = True
    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy() and audio_playing:
        clock.tick(30)  # Adjust playback speed if necessary

def stop_audio():
    global audio_playing
    audio_playing = False
    pygame.mixer.music.stop()

def main():
    st.title("YouTube Transcript Summarizer")

    video_url = st.text_input("Enter YouTube video URL:")

    if st.button("Get Summary"):
        if video_url:
            try:
                video_id = video_url.split("v=")[1]
                transcript_text = get_video_transcript(video_id)
                if transcript_text:
                    st.subheader("Original Transcript:")
                    st.write(transcript_text)

                    summary = summarize_transcript(transcript_text)

                    st.subheader("Summary:")
                    st.write(summary)

                    st.success("Generating summary audio...")
                    text_to_speech(summary)
                    play_audio_blocking()

                else:
                    st.warning("Failed to retrieve transcript. Please check the video URL.")
            except Exception as e:
                st.error(f"Error occurred: {e}")
        else:
            st.warning("Please enter a valid YouTube video URL.")

    if audio_playing:
        if st.button("Stop Audio"):
            stop_audio()
            st.success("Audio playback stopped.")

if __name__ == '__main__':
    main()
