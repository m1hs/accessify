from youtube_transcript_api import YouTubeTranscriptApi
from textsum.summarize import Summarizer
from googletrans import Translator

SUPPORTED_LANGUAGES = {
    'Arabic': 'ar',
    'Spanish': 'es',
    'Hindi': 'hi',
    'German': 'de'
}

def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([t['text'] for t in transcript_list])
        return transcript_text
    except Exception as e:
        raise Exception(f"Error occurred while fetching transcript: {e}")

def summarize_and_translate(video_url, target_language):
    try:
        video_id = video_url.split("v=")[1]
        transcript_text = get_video_transcript(video_id)

        summarizer = Summarizer()
        summary = summarizer.summarize_string(transcript_text)

        translator = Translator()

        if target_language not in SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {target_language}")

        target_language_code = SUPPORTED_LANGUAGES[target_language]
        translated_summary = translator.translate(summary, dest=target_language_code).text

        return transcript_text, translated_summary
    except Exception as e:
        raise Exception(f"Error occurred: {e}")
