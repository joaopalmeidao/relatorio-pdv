import pyautogui
# import pygetwindow
import time
from datetime import datetime
import keyring
from module.telegram import TelegramBot
# import os 
# Parâmetros da tela
size = str(pyautogui.size())
size.split('=')
size_fomated_x = size[11:15]
size_fomated_y = size[24:-1]
# print(size_fomated_x)
# print(size_fomated_y)

# if pyautogui.size()==(1920,1080):
#     print(size)

# def config_size(width,height):
#     if width != 1920:

password = keyring.get_password('dbvenda','S')
data = datetime.today().strftime('%d-%m-%Y')

mensagem = 'Relatório PDV enviado para impressão'

def pesquisar():

    # os.startfile("C:\\DBVenda\\Binarios\\DBVenda.exe")
    # os.system("start DBVendaPDV.exe")

    pyautogui.hotkey('win', 'r')
    time.sleep(0.2)
    pyautogui.write('C:\DBVenda\Binarios\DBVendaPDV.exe')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.click(864,508)



def fechamento_caixa():
    pyautogui.press('f7')
    pyautogui.press('f4')
    time.sleep(2)

def digita_senha():
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(40)

def imprimir_fechamento():
    time.sleep(5)
    pyautogui.screenshot(f'Vendas PDV--{data}.png')
    
    time.sleep(2)
    TelegramBot.send_message_with_image(f'Vendas PDV--{data}.png',mensagem)
    pyautogui.click(1115, 648)
    
    time.sleep(1)

def sair():
    time.sleep(5)
    pyautogui.press('esc')
    pyautogui.click(1208, 47)
    pyautogui.press('esc')
    pyautogui.hotkey('alt', 'f4')
    pyautogui.press('f1')
    pyautogui.press('f2')
    pyautogui.press('esc', presses=2)
    time.sleep(2)
    pyautogui.press('esc', presses=2)
    pyautogui.press('esc', presses=2)


def main():

    TelegramBot.load_config()

    pesquisar()
    

    fechamento_caixa()
    digita_senha()
    imprimir_fechamento()
    sair()
    
    exit()


if __name__ == '__main__':
    main()
