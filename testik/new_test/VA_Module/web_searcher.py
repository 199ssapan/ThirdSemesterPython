import requests, webbrowser
import speech_recognition as sr
import wikipedia
import gtts
import threading
import pygame
from ..Audio_Module import audio_processing as ap

def search_google(query):
    base_url = "https://www.google.com/search"
    params = {"q": query}
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.url
    else:
        return "Ошибка при выполнении запроса в Google"
    

interrupted = False

def voice_answer_wiki(query, paragraph_index=0):
    global interrupted

    wikipedia.set_lang("ru")

    try:
        # Get the Wikipedia page based on the query
        page = wikipedia.page(query)

        # Get the paragraphs from the article
        paragraphs = page.content.split('\n')

        if paragraph_index < len(paragraphs):
            # Select the desired paragraph
            selected_paragraph = paragraphs[paragraph_index]

            # Convert the paragraph to speech using gTTS
            tts = gtts.gTTS(text=selected_paragraph, lang='ru')

            # Save the speech to an audio file
            tts.save("output.mp3")

            # Create a Pygame mixer
            pygame.mixer.init()
            pygame.mixer.music.load("output.mp3")

            # Play the audio
            pygame.mixer.music.play()

            # Listen for user interruption in a separate thread
            recognition_thread = threading.Thread(target=listen_for_interrupt)
            recognition_thread.start()

            # Wait for audio to finish playing
            while pygame.mixer.music.get_busy() and not interrupted:
                continue

            # Stop the audio if it's still playing
            pygame.mixer.music.stop()

            # Check if interrupted
            if interrupted:
                return "Чтение прервано пользователем."

            return "Аудио сгенерировано и воспроизведено."

        else:
            return "Запрашиваемый абзац не найден в статье."

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Найдено несколько вариантов: {', '.join(e.options)}"
    except wikipedia.exceptions.PageError as e:
        return "Страница не найдена."

def listen_for_interrupt():
    global interrupted

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Слушаю... (скажите 'прервать' для прерывания)")
        try:
            audio = recognizer.listen(source, timeout=None)
            command = recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: '{command}'")
            if "прервать" in command.lower():
                interrupted = True
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Не удалось распознать команду. Пожалуйста, попробуйте снова.")


def search_and_open_browser(query):
    google_search_url = f"https://www.google.com/search?q={query}"

    try:
        response = requests.get(google_search_url)
        if response.status_code == 200:
            ap.say(ap.ACCORDING_TO_WIKIPEDIA)
            webbrowser.open(google_search_url)
            print(f"Результаты поиска в Google: {google_search_url}")
        else:
            print("Ошибка при выполнении запроса в Google.")
    except Exception as e:
        print(f"Ошибка при выполнении запроса и открытии браузера: {e}")
