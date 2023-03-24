from gtts import gTTS
import os
from datetime import datetime

def text2audio(text):
    tts = gTTS(text=text, lang='en')

    audio_save_path = './audios/out'
    now = datetime.now()
    audio_path = os.path.join(audio_save_path, now.strftime('%Y-%m-%d_%H-%M-%S') + '.mp3')

    tts.save(audio_path)

    return audio_path

if __name__ == '__main__':
    text = "hi, my name is Haodong, could you hear me clearly?"
    text2audio(text)
