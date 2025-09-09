
################ IMPORTS ################
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from os import path
from selenium.webdriver.ie.options import Options as IeOptions
from selenium.webdriver.ie.service import Service as IeService

from config import *

class function_web:
    def open_browser_edge_ie_mode():
        """
        Abre o Microsoft Edge em Modo de Compatibilidade com o Internet Explorer,
        iniciando o IEDriver com as opções para se anexar ao Edge.
        """
        print("Configurando opções para o Modo IE no Edge...")
        
        # 1. Usamos as opções do Internet Explorer (IeOptions)
        ie_options = IeOptions()
        
        # 2. Esta é a instrução chave: anexa o controle do driver do IE a uma instância do Edge
        ie_options.attach_to_edge_chrome = True
        
        # 3. Define o caminho para o EXECUTÁVEL do Edge (não o driver)
        # Isso informa ao IEDriver qual navegador Edge ele deve iniciar
        ie_options.edge_executable_path = path_edge_executable # Ex: "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

        # Adiciona as outras opções que você já usava para o IE
        ie_options.ignore_protected_mode_settings = True
        ie_options.ignore_zoom_level = True
        ie_options.native_events = True
        # Para abrir em modo privado, o argumento é passado de forma diferente no Edge
        # Adicionaremos isso diretamente se necessário, mas o attach_to_edge_chrome já pode lidar com isso.

        # 4. O serviço que vamos usar é o do IEDriverServer.exe
        # O msedgedriver.exe não é chamado diretamente nesta abordagem
        service = IeService(executable_path=path_ie_drive)

        # 5. Inicializamos o webdriver.Ie, não o webdriver.Edge
        print("Abrindo navegador Edge via IEDriver...")
        driver = webdriver.Ie(service=service, options=ie_options)

        # A partir daqui, o código é o mesmo
        print("Navegador aberto com sucesso!")
        driver.get(url_AdmSite)
        driver.maximize_window()

        print("Realizando login...")
        try:
            user_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "strUsuario"))
            )
            driver.execute_script("arguments[0].value = arguments[1];", user_element, user_AdmSite)

            pass_element = driver.find_element(By.NAME, "strSenha")
            driver.execute_script("arguments[0].value = arguments[1];", pass_element, pwd_AdmSite)

            time.sleep(1)
            
            submit_button = driver.find_element(By.XPATH, '//input[@type="submit" and @value="     OK     "]')
            driver.execute_script("arguments[0].click();", submit_button)
            
            time.sleep(2)
            print("Login realizado com sucesso!")
            
        except Exception as e:
            print(f"Ocorreu um erro durante o login: {e}")
            driver.quit()
            return None

        return driver