from whatsapp_automation import whatsapp_launch, pxldown_max,type_a_message,send_botton
import pyautogui as py
import time


def send_sms(name , massege):
    whatsapp_launch()
    time.sleep(1)
    py.hotkey('ctrl','f')
    time.sleep(1)
    py.write(name)
    time.sleep(1)
    pxldown_max()
    time.sleep(1)
    type_a_message()
    py.write(massege)
    time.sleep(1)
    send_botton()