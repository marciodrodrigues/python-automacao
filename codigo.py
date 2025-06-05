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
#2
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=700, y=370)
pyautogui.write("test@marciodrodrigues.pode.contratar") 
pyautogui.press("tab")
pyautogui.write("100%contratado")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

print(pyautogui.position())
3#
import pandas as pd
basedados = pd.read_csv("produtos.csv")
print(basedados)

4#
'''pyautogui.click(x=700, y=260)
codigo = "MOLO000251"
pyautogui.write(codigo)'''

#5
for linha in basedados.index:
    pyautogui.click(x=700, y=260)
    codigo = basedados.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = basedados.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = basedados.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(basedados.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(basedados.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(basedados.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(basedados.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(10000)