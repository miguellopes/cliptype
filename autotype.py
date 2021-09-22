from tkinter import Tk
import pyautogui

r = Tk()
passos = 5

while 1:
    if pyautogui.confirm("Colar o conteudo do clipboard?") == "OK":
        tmp = r.clipboard_get()
        for i in range(0,len(tmp),passos):
            pyautogui.write(tmp[i:i+passos])
    else:
        break
