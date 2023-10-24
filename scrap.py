from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import openpyxl
import pyperclip
import pyautogui

#entrar no site do ESAJ SP
driver = webdriver.Chrome()
#entrar na planilha
workbook = openpyxl.load_workbook(r"C:\Users\ppcno\OneDrive\Documentos\pedro\python\planilha.xlsx")
sheet_processos = workbook['Processos']

#Função que copia o número do processo, insere no ESAJ SP e copia andamentos
def scrap_processos(comeco=0, total=10):
    while comeco < total:
        for linha in sheet_processos.iter_rows(min_row=2):
            driver.get('https://esaj.tjsp.jus.br/cpopg/open.do')
            sleep(1)            
            num_processo = linha[0].value
            pyperclip.copy(num_processo)
            pyautogui.click(331,275,duration=1)
            pyautogui.hotkey('ctrl','v')
            pyautogui.click(879,273,duration=1)
            sleep(2)
            andamentos = driver.find_elements(By.XPATH, "//*[@id='tabelaUltimasMovimentacoes']")
            andamentos_texto = ""

            for andamento in andamentos:
                andamentos_texto += andamento.text

            linha[1].value = andamentos_texto  # Atualiza a segunda coluna com os andamentos

            # Salva a planilha
            workbook.save(r"C:\Users\ppcno\OneDrive\Documentos\pedro\python\planilha.xlsx")
            comeco += 1

scrap_processos()

    
