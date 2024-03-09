    # passo 4 : cadastrar um produto
# passo 5 : repetir o processo do cadastro ate acabar a base de dados
import pyautogui
import time
pyautogui.PAUSE=2   

# pyautogui.click --> clicar em algum lugar da tela
# pyautogui.write --> escrever um texto
# pyautogui.press --> pressionar uma tecla

#passo 1 : entrar no sistema da empresa
# abrir o navegador(chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#entrar no site
link=("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link)
pyautogui.press("enter")
# dar uma pausa um pouco maior (3 segundos)
time.sleep(3)
# abrir em tela cheia
pyautogui.hotkey("winleft", "up")
# passo 2 : fazer o login 
# clicar no campo e-mail e senha(como o email e a seha ficaram salvos apenas de 2 tabs e enter)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
# passo 3 : importar a base de dados
import pandas
tabela=pandas.read_csv("produtos.csv")
print(tabela)
# passo 4 : cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=409, y=291)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    
    pyautogui.press("tab")

    obs=tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))  

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter  ")
    pyautogui.scroll(5000)


    
    






























