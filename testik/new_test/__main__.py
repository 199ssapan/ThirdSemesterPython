from .VA_Module import executable as ex
from .Audio_Module import audio_processing as ap
import os

#ap.create_audio_by_text("открытие файла", "FILE_OPENING.wav")

if __name__ == "__main__":
    ex.start_VA()
    #os.remove("C:\\Users\\maksm\\Desktop\\testik\\output.mp3")




