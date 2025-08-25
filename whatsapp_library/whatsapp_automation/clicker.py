import pyautogui as py
import os
import time
from whatsapp_automation import whatsapp_launch
IMAGE_FOLDER = "image"  

def whatsapp_button_click(image_name, confidence=0.9):
    image_path = os.path.join(IMAGE_FOLDER, f"{image_name}.jpg")
    
    print(f"🔍Looking for '{image_path}'...")
    button = py.locateCenterOnScreen(image_path, confidence=confidence)
    
    if button:
        py.moveTo(button)
        time.sleep(0.1)
        py.click()
        print(f"Clicked on '{image_name}' button.")
    else:
        print(f"'{image_name}.jpg' not found in folder '{IMAGE_FOLDER}'.")

def click_relative(x_offset=0, y_offset=0):
    x, y = py.position()
    py.click(x + x_offset, y + y_offset)

def status():
    whatsapp_button_click("status")

def voice_call():
    whatsapp_button_click("voice call")

def video_call():
    whatsapp_button_click("video call")

def type_a_message():
    whatsapp_button_click("type a sms")
    py.click()
    
def setting():
    whatsapp_button_click("setting")

def search_bar():
    whatsapp_button_click("search bar")

def archived():
    whatsapp_button_click("archived")

def attach():
    whatsapp_button_click("attach")

def chat():
    try:
        whatsapp_button_click("chat")
    except:
        whatsapp_button_click("chats")

def contect():
    attach()
    time.sleep(0.1)
    whatsapp_button_click("contect")
    py.click()

def document():
    attach()
    time.sleep(0.1)
    whatsapp_button_click("document")
    py.click()

def profile():
    whatsapp_button_click("profile")
    
def filter_chat():
    whatsapp_button_click('filter chat')
    
def contects():
    whatsapp_button_click('contects')
    py.click()    

def caret():
    whatsapp_button_click('caret')
    py.click()

def whatsapp_icon():
    whatsapp_button_click('whatsapp icon')
    py.click()
    
def pxldown_max():
    try:
        position = py.locateCenterOnScreen(r'image\blank search bar max.jpg', confidence=0.9)


        if position:
            x, y = position
            time.sleep(1)
            py.click(x, y + 103)  # 100 px niche click karega
            print(f"Clicked 100 pixels below caret: {x},{y}")
        else:
            print("Caret position not found.")
    except Exception as e:
        print(f"Image not found or error: {e}")

def send_botton():
    whatsapp_button_click('Send_button')
    py.click()


