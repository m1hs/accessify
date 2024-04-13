import streamlit as st
import fitz  
from summa.summarizer import summarize
from googletrans import Translator
from gtts import gTTS
from io import BytesIO

LANGUAGES = {
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
}

def extract_text_from_pdf(file):
    pdf_data = file.read()
    doc = fitz.open(stream=pdf_data, filetype="pdf")
    text = "".join(page.get_text() for page in doc)
    doc.close()
    return text

def translate_text(text, dest_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def main():
    st.title("Accessify - PDF Translator and Summarizer")

    file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if file:
        pdf_text = extract_text_from_pdf(file)

        st.subheader("PDF Content")
        st.write(pdf_text)

        dest_language = st.selectbox("Select destination language:", list(LANGUAGES.keys()))

        if st.button("Summarize and Translate"):
            if pdf_text:
                summarized_text = summarize(pdf_text)
                translated_text = translate_text(summarized_text, LANGUAGES[dest_language])

                st.subheader("Summarized and Translated Text")
                st.write(translated_text)

                if translated_text:
                    with BytesIO() as audio_bytes:
                        gTTS(translated_text, lang=LANGUAGES[dest_language]).write_to_fp(audio_bytes)
                        st.audio(audio_bytes.getvalue(), format='audio/mp3')

if __name__ == "__main__":
    main()
