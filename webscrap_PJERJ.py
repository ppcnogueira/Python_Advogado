from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import pyautogui
from time import sleep
import openpyxl

class WebScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.get = self.driver.get('https://tjrj.pje.jus.br/1g/ConsultaPublica/listView.seam')
        self.wait = WebDriverWait(self.driver, 10)    


    def scrap_and_update_excel(self):
        workbook = openpyxl.load_workbook(r"C:\\Users\\ppcno\\OneDrive\\Documentos\\git_pedro\\Python_Advogado\\planilha2.xlsx")
        sheet_processos = workbook['Processos']
        for linha in sheet_processos.iter_rows(min_row=2):
            original_window = self.driver.current_window_handle                   
            num_processo = linha[0].value
            pyperclip.copy(num_processo)
            pyautogui.press('f5')
            sleep(0.5)
            pyautogui.press('f5')
            sleep(0.5)
            self.driver.find_element(By.ID,'fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso').click()
            pyautogui.hotkey('ctrl', 'v')
            sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[@id='fPP:searchProcessos']").click()       
            sleep(2)  
            pyautogui.click(455, 289, duration=1)
            self.wait.until(EC.number_of_windows_to_be(2))
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break        
            
            andamentos = self.driver.find_elements(By.XPATH, "//*[@id='j_id131:processoEvento']")
            andamentos_texto = ""
            for andamento in andamentos:
                andamentos_texto += andamento.text
            linha[2].value = andamentos_texto
            #salvar a planilha
            workbook.save("C:\\Users\\ppcno\\OneDrive\\Documentos\\git_pedro\\Python_Advogado\\planilha2.xlsx")
            #fechar a segunda janela
            self.driver.close()
            #voltar para a janela principal de pesquisa do processo
            self.driver.switch_to.window(original_window)
            sleep(2)


web_scraper = WebScraper()
web_scraper.scrap_and_update_excel()

