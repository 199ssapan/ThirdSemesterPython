import speech_recognition as sr

from . import program_manager as pm
from . import web_searcher as ws

OPEN_FILE_COMMAND_LIST = ["открой файл", "открыть файл",
                           "открой", "открыть"]
CREATION_COMMAND_LIST = ["создай", "создать"]
LAUNCH_COMMAND_LIST = ["запусти", "запустить", "запуск"]
DELETE_COMMAND_LIST = ["удалить", "удали"]

DOCUMENT_LIST = ["документ", "документа",
                  "документы", "document"]
PRESETATION_LIST = ["презентация", "презентацию", "презентации"]
TEXTFILE_LIST = ["файл", "текстовый файл", "текстовый документ"]

SEARCH_WIKI_LIST = ["поищи на википедии", "википедия", 
                    "википедии", "википедию"]
SEARCH_GOOGLE_LIST = ["загугли", "гугл", 
                      "google", "посмотри в интернете", 
                      "узнай", "найди", "найти"]

EXIT_COMMAND_LIST = ["выйти", "выйди", "выход"]

def recognize_speech():
    recognizer = sr.Recognizer()  # Инициализация распознавателя речи для каждой итерации
    with sr.Microphone() as source:
        print("Говорите что-нибудь...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="ru-RU")
        return command.lower()
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
        return ""
    except sr.RequestError:
        print("Не удалось отправить запрос к сервису распознавания речи")
        return ""
    

def start_VA():
    while True:
        command = recognize_speech()
        print(command)
        if command:
            if (com_part_action := pm.find_same_command(LAUNCH_COMMAND_LIST, command)) != None:
                pm.launch_application(command)

            elif (com_part_action := pm.find_same_command(OPEN_FILE_COMMAND_LIST, command)) != None:
                file_name = command.replace(com_part_action, "", 1).strip()
                pm.open_file(file_name)

            elif (com_part_action := pm.find_same_command(CREATION_COMMAND_LIST, command)) != None:
                file_name = command.replace(com_part_action, "", 1)
                if (com_part_file_type := pm.find_same_command(PRESETATION_LIST, command)) != None:
                    file_name = file_name.replace(com_part_file_type, "", 1).strip()
                    pm.create_file(file_name, ext = ".pptx")
                elif (com_part_file_type := pm.find_same_command(TEXTFILE_LIST, command)) != None:
                    file_name = file_name.replace(com_part_file_type, "", 1).strip()
                    pm.create_file(file_name, ext = ".txt")
                elif (com_part_file_type := pm.find_same_command(DOCUMENT_LIST, command)) != None:
                    file_name = file_name.replace(com_part_file_type, "", 1).strip()
                    pm.create_file(file_name, ext = ".docx")

            elif (com_part_action := pm.find_same_command(SEARCH_WIKI_LIST, command)) != None:
                query = command.replace(com_part_action, "", 1)
                ws.voice_answer_wiki(query)
            elif (com_part_action := pm.find_same_command(SEARCH_GOOGLE_LIST, command)) != None:
                query = command.replace(com_part_action, "", 1)
                ws.search_and_open_browser(query)
            
            elif (com_part_action := pm.find_same_command(EXIT_COMMAND_LIST, command)) != None:
                print("Good Bye!")
                break
        else:
            print("error")
