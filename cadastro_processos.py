"""
Esse módulo criará automaticamente o cadastro de um processo no sistema do escritório.
Necessário alterar a posição dos clicks conforme a resolução utilizada.
"""

import pyautogui
import time

processos =  # Informar o número de processos que serão cadastrados

x = 0

while x < processos:

    # Planilha
    pyautogui.hotkey('winleft', '5')
    time.sleep(1)
    pyautogui.click(x=1910, y=976)
    time.sleep(1)
    pyautogui.click(x=119, y=251)
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 'c')
    time.sleep(1)
     

    # Sistema - Cadastrar processo
    pyautogui.hotkey('winleft', '4')
    time.sleep(1)
    pyautogui.click(x=1755, y=431) # Botão cadastrar
    time.sleep(4)    
    pyautogui.click(x=174, y=589) # Processo
    time.sleep(1)  
    pyautogui.hotkey('ctrlleft', 'v')
    time.sleep(2)
    pyautogui.click(x=991, y=457) # Honorários
    time.sleep(1)
    pyautogui.write('negociacao padrao') 
    time.sleep(1)
    pyautogui.press('enter')    
    time.sleep(2)
    pyautogui.press('down')    
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')    
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')    
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=682, y=699)
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)
    pyautogui.click(x=177, y=749) # Reu
    time.sleep(1)
    pyautogui.write('reu')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=815, y=722)
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)
    pyautogui.click(x=107, y=568) # Adicionar centro de custo
    time.sleep(1)
    pyautogui.click(x=178, y=577)
    time.sleep(1)
    pyautogui.write('middle')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=956, y=582)
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1) 
    pyautogui.click(x=302, y=746) # Codigo Cliente
    time.sleep(1)
    pyautogui.write('Nome do Cliente')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=300, y=779)
    time.sleep(2)

    # Excel
    pyautogui.hotkey('winleft', '5')
    time.sleep(1)
    pyautogui.click(x=63, y=236)
    time.sleep(1)
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 'c')
    time.sleep(1)

    # Sistema do escritório
    pyautogui.hotkey('winleft', '4')
    time.sleep(1)
    pyautogui.click(x=300, y=779)
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 'v')
    time.sleep(1)
    pyautogui.click(x=1513, y=930) # Botão Salvar
    time.sleep(5)

    x += 1
