import pyautogui
import time

processos = 26
x = 0

# Planilha
pyautogui.hotkey('winleft', '5')
pyautogui.click(x=1910, y=981)
pyautogui.click(x=63, y=236)
pyautogui.hotkey('ctrlleft', 'c')
time.sleep(1)
    

# Legalone - Procurar a pasta
pyautogui.hotkey('winleft', '4')
pyautogui.click(x=211, y=607) # Posição do GCPJ
    
while x < processos:
    
    pyautogui.hotkey('ctrlleft', 'v')
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.keyDown('ctrl')
    pyautogui.click(x=543, y=882) # Pasta depois que encontrar
    time.sleep(3)
    pyautogui.hotkey('ctrlleft', '2') # Trocar aba do Chrome
    time.sleep(4)
    

    # Legalone - Criar a tarefa
    pyautogui.click(x=1743, y=557)
    time.sleep(5)
    
    pyautogui.click(x=176, y=378) # Civel
    pyautogui.write('civel')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(4)

    pyautogui.click(x=176, y=416) # Civel
    pyautogui.write('civel')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.click(x=176, y=460) # Descrição
    pyautogui.write('Subsidios no GCPJ')
    time.sleep(3)
    
    pyautogui.doubleClick(x=176, y=533) # Tipo/Subtipo
    time.sleep(2)
    pyautogui.write('subsi')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)   

    pyautogui.click(x=176, y=723) # Data da tarefa
    time.sleep(2)
    pyautogui.write('11062021')
    time.sleep(2)
    pyautogui.click(x=528, y=627) # Clicar fora para dar page down
    time.sleep(2)
    pyautogui.press('pagedown')
    time.sleep(2)
    pyautogui.click(x=1523, y=935) # Clicar para salvar
    time.sleep(6)
    pyautogui.click(x=466, y=11) # Fechar a aba da tarefa
    time.sleep(2)
    pyautogui.press('pageup')
    time.sleep(1)

    # Planilha
    pyautogui.hotkey('winleft', '5')
    time.sleep(1)
    pyautogui.click(x=1910, y=981)
    time.sleep(1)
    pyautogui.click(x=63, y=236)
    pyautogui.hotkey('ctrlleft', 'c')
    time.sleep(1)
    pyautogui.hotkey('winleft', '4')
    time.sleep(1)
    pyautogui.doubleClick(x=211, y=607) # Posição do GCPJ
    x += 1

