from tkinter import Tk
import pyautogui

r = Tk()

while 1:
    if pyautogui.confirm("Colar o conteudo do clipboard?") == "OK":
        for i in r.clipboard_get():
            pyautogui.write(i)
    else:
        break
