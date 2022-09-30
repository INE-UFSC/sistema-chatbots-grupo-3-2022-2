from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        comandos = {
            "Qual o seu nome?": "Meu nome é {}, meu querido!".format(nome),
            "Quero um conselho": "Você deve ser feliz! Viva sua vida como se ela não fosse acabar amanhã!"
            }
        super().__init__(nome, comandos)

    def apresentacao(self) -> str:
        pass

    def boas_vindas(self) -> str:
        pass
   
    def executa_comando(self, cmd: str) -> str:
        pass
    
    def despedida(self) -> str:
        pass
