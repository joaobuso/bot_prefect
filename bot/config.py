import os

## Inserir registros de configuração do Bot


# Alterar o Kill Process de acordo o processo que deverá ser encerrado
Kill_Process = {'iexplore.exe','msedge.exe'}

# Não alterar os parâmetros abaixo
bibliotecas = ["requests", "psutil", "pyautogui","rpa-hypercoe","jsonpickle"]
path = fr"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\config.txt"

# Chrome drive
path_chrome_drive = r"C:\chromedriver\chromedriver.exe"
path_ie_drive = r"C:\IEDriverServer\IEDriverServer.exe"
path_queue = r'C:\temp\MGL_Coleta_Comum\queue.json'
path_edge_drive = r"C:\Users\coletacomum\Downloads\edgedriver_win64\msedgedriver.exe"
path_edge_executable = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

#Dados AdmSite
url_AdmSite = 'http://admsite.magazineluiza.intranet/login.asp'
user_AdmSite = 'jaoc_junior'
pwd_AdmSite = 'Fiscal19!'

# Dados Dispatcher / Performer
# Esse parametro definirá se o processo terá a função habilitada ou não dentro do template
blnDispatcher = False
blnPerformer = True

# Dados Planilha Eletronica Aprovação de Exceção 
spreadsheet_id_matriz = '1SWPoythU9fN5SRdiy-zidID0SMc25WmPIJ50cpZf9rU'#44
sheet_title_matriz = 'EMISSOES'
spreadsheetDePara_id = '1doCd8py1_M_1fUej0Q7A3SlLigfXWG6XV8IzaGT34k4' #44
sheet_title_DePara = 'BASE CD'
spreadsheet_id_depara_envio = "1wGozFpQnYi34eHMpGhW616Vxk-MhjzxB4WFsMATibZE"
sheet_title_depara_envio = "DE_PARA _TRIA_ENVIOS"
spreadsheet_id_analise_rle = "1doCd8py1_M_1fUej0Q7A3SlLigfXWG6XV8IzaGT34k4"
sheet_title_depara_analise_rle = "BASE CD"

# Numero máximo de tentativas de reprocessamento
maxy_retry = 3

# Gmail da magalu para envio de email
EMAIL = 'emissaonfereversa@magazineluiza.com.br'
PASSWORD_EMAIL = 'mhrf vxad gynd dije' # senha de app da Google


# Dados Planilha Eletronica Aprovação de Exceção
path_Autenticador_Google = fr"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\resources\Autenticador.json"


