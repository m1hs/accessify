from gtts import gTTS
import pygame

audio_playing = False

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save('output.mp3')

def play_audio_blocking():
    global audio_playing
    audio_playing = True
    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy() and audio_playing:
        clock.tick(30)  # playback speed 

def stop_audio():
    global audio_playing
    audio_playing = False
    pygame.mixer.music.stop()
