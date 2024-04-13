import streamlit as st
from summarizer import summarize_and_translate, SUPPORTED_LANGUAGES
from audio_generator import text_to_speech, play_audio_blocking, stop_audio
def main():
    st.title("YouTube Transcript Summarizer")

    supported_languages = list(SUPPORTED_LANGUAGES.keys())
    target_language = st.selectbox("Select Target Language:", supported_languages)

    video_url = st.text_input("Enter YouTube video URL:")

    if st.button("Generate Summary Audio"):
        if video_url:
            transcript_text, translated_summary = summarize_and_translate(video_url, target_language)

            if transcript_text and translated_summary:
                st.subheader("Original Transcript:")
                st.write(transcript_text)

                st.subheader(f"Translated Summary ({target_language}):")
                st.write(translated_summary)

                st.success("Generating summary audio...")
                text_to_speech(translated_summary, lang=SUPPORTED_LANGUAGES[target_language])
                play_audio_blocking()
        else:
            st.warning("Please enter a valid YouTube video URL.")

    if st.button("Stop Audio"):
        stop_audio()
        st.success("Audio playback stopped.")

if __name__ == '__main__':
    main()
