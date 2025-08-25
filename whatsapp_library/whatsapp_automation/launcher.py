
import pyautogui as py
import time

def whatsapp_launch():
    try:
        py.hotkey('win')
        time.sleep(0.1)
        py.write('whatsapp')
        time.sleep(0.1)
        py.press('enter')
        print("Whatsapp launced bhai ...")
    except Exception as e:
        print(f"Whatsapp launching error:{e}")
        
