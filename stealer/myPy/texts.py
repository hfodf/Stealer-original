import os
import shutil
import re
import pyautogui

def proverka(p, destination_folder):
    try:
        pyautogui.screenshot(r'C:\Min\screen.png')
        for item in os.scandir(p):
            if item.is_file() and (re.search(r".*\.txt", item.name) or re.search(r".*\.csv", item.name) or re.search(r".*\.json", item.name)):
                source_file_path = item.path
                shutil.copy2(source_file_path, destination_folder)
            
            elif item.is_dir():
                for ite in os.scandir(item.path):
                    if ite.is_file() and (re.search(r".*\.txt", ite.name) or re.search(r".*\.csv", ite.name) or re.search(r".*\.json", ite.name)):
                        source = ite.path
                        shutil.copy2(source, destination_folder)

    except PermissionError:
        print("Отказано в доступе")
    except Exception as e:
        print(f"Произошла ошибка: {e}")      
