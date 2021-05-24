
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""


import os
import pyautogui
from time import sleep
import ctypes

app1 = 'telegram'
app2 = 'whatsapp'

def close_these():
    while 1:
        res = False         
        output = os.popen('wmic process get description, processid').read()
        apps = ''
        if (f'{app1}.exe' in output.lower()) or (f'{app2}.exe' in output.lower()):
            if f'{app1}.exe' in output.lower():
                apps += f'{app1.uppe()} is open ...\n'
            if f'{app2}.exe' in output.lower():
                apps += f'{app2.uppe()} is open ...\n'
                
            print('fuck you...')
            wrong_pass = 0
            pyautogui.keyDown('winleft')
            pyautogui.press('d')
            pyautogui.keyUp('winleft')
            os.system("TASKKILL /F /IM whatsapp.exe")
            os.system("TASKKILL /F /IM telegram.exe")
            
            pyautogui.alert(f'You should not open these...\n\n{apps}',
                            'Made a mistake!!!','Close them NOW',0)            
            while pyautogui.password('Enter password') != 'Kianoush':
                wrong_pass += 1
    
                pyautogui.keyDown('winleft')
                pyautogui.press('d')
                pyautogui.keyUp('winleft')
    
                os.system("TASKKILL /F /IM whatsapp.exe")
                os.system("TASKKILL /F /IM telegram.exe")
                ctypes.windll.user32.LockWorkStation()
                
                # if wrong_pass > 4:
                #     res = True
                #     break                
                                    
                pyautogui.alert(f'You should not open these...\n\n{apps}',
                            'Made a mistake!!!','Close them NOW',0) 
        if res:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
        sleep(5)
    
    
















