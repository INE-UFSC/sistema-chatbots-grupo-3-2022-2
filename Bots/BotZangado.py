from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        super.__init__(nome , {"Qual é o seu nome?" : f"Meu nome é {self.nome} e pare de falar comigo", 
        "Quero um conselho": "Meu conselho é que você vá embora. Eu não quero conversar com você!",
        "Quero uma piada": "Não sou palhaço para contar uma piada para você. Vá embora!"})


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