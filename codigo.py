# 1 entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 2 fazer o login
# 3 importar base de dados
# 4 cadastrar o produto
# 5 repetição para todos produtos

import pyautogui
import time
#1 
pyautogui.PAUSE = 0.8
pyautogui.press("win")
pyautogui.write("chrome ")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=700, y=370)
pyautogui.write("test@marciodrodrigues.pode.contratar") 
pyautogui.press("tab")
pyautogui.write("100%contratado")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

