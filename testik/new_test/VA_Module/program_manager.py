import os
import glob
from Audio_Module import audio_processing as ap
save_path = "C:\\Users\\maksm\\Desktop\\testik\\new_test\\test_folder\\"

def find_same_command(commands_list, command):
    for com in commands_list:
        if com in command:
            return com
    return None
def launch_application(app_name):
    try:
        if "браузер" in app_name:
            os.system("start C:\\Users\\maksm\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe")
        elif "текстовый редактор" in app_name:
            os.system("notepad")
        elif "проводник" in app_name:
            os.system("explorer")
        else:
            ap.say(ap.APPLICATION_FIND_ERROR)
    except Exception as e:
        print(f"Ошибка: {e}")

def create_file(file_name, ext=".txt"):
    try:
        # Путь к папке, где будем создавать файл
        folder_path = save_path
        # Полный путь к новому файлу
        file_path = os.path.join(folder_path, file_name) + ext

        # Проверяем наличие файла с таким именем
        if os.path.exists(file_path):
            print(f"Файл с именем {file_name} уже существует")
        else:
            # Создаем новый файл
            with open(file_path, 'w') as new_file:
                print(f"Файл {file_name} успешно создан")
    except Exception as e:
        print(f"Ошибка: {e}")

def open_file(file_name):
    try:
        # Путь к папке, где находятся файлы
        folder_path = save_path

        # Создаем шаблон для поиска файлов с разными расширениями
        search_pattern = os.path.join(folder_path, f"{file_name}.*")
        print(search_pattern)

        # Ищем файлы по шаблону
        matching_files = glob.glob(search_pattern)

        if matching_files:
            # Открываем первый найденный файл
            os.system(f"start {matching_files[0]}")
        else:
            print("Файл не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

def delete_file(file_name):
    try:
        # Путь к папке, где находятся файлы
        folder_path = save_path

        # Полный путь к файлу
        file_path = os.path.join(folder_path, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)  # Удаляем файл
            print(f"Файл {file_name} успешно удален")
        else:
            print("Файл не найден")
    except Exception as e:
        print(f"Ошибка: {e}")