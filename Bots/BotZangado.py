from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        super.__init__(nome , {})


    def apresentacao(self):
        return f"{self.__nome} diz: Estou dormindo escolha outro bot."
 
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        return f"{self.__nome} diz: Porque você me escolheu. Eu te odeio!" 

    def despedida(self):
        return f"{self.__nome} diz: Finalmente! Não aguentava mais você"