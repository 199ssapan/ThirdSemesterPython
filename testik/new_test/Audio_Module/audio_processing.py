import sounddevice as sd
import soundfile as sf
from gtts import gTTS

ACCORDING_TO_WIKIPEDIA = "ACCORDING_TO_WIKIPEDIA.wav"
APPLICATION_FIND_ERROR = "APPLICATION_FIND_ERROR.wav"
ERROR = "ERROR.wav"
FILE_CREATION_ERROR = "FILE_CREATION_ERROR.wav"
FILE_FIND_ERROR = "FILE_FIND_ERROR.wav"
FILE_CREATION_SUCCESS = "FILE_CREATION_SUCCESS.wav"
OPENING_BROWSER = "OPENING_BROWSER.wav"
SPEECH_RECOGNITION_ERROR = "SPEECH_RECOGNITION_ERROR.wav"

def say(filename):
    filepath = 'C:\\Users\\maksm\\Desktop\\testik\\new_test\\Audio_Module\\audio_files\\' + filename
    # Extract data and sampling rate from file
    data, fs = sf.read(filepath, dtype='float32')  
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing

def create_audio_by_text(text, filename):
    text_to_speak = text
    tts = gTTS(text=text_to_speak, lang='ru')
    tts.save("C:\\Users\\maksm\\Desktop\\testik\\new_test\\Audio_Module\\audio_files\\" + filename)
    