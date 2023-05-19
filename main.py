from config.config import Define_me #Definição de configuração padrão da applicação
from config.auth import Define_me1 #Definição de configuração de autenticação padrão da applicação (Se necessario)
#from config.connection import connection #Conexão com o Banco de Dados (Se necessario)

from app.controller.app_controller import Controller # Importa o controller da Aplicação 

class Main(): 
    
    def __init__(self) -> None:
        pass

    def init_app():
        
        #Exemplo - Test Application
        for i in range(0, 10):
            soma = Controller.app(i, 9)

            print(soma)

Main.init_app()