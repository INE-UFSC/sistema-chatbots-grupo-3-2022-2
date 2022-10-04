from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome='Zangado'):
        comandos = {'Bom Dia': 'Bom dia pra quem?', 
                    'Qual o seu nome?': 'É sério que você quer que eu repita? É Yoda!!!',
                    'Quero um conselho': 'Não tenho filho desse tamanho.',
                    'Adeus': 'Já vai tarde!'}
        super().__init__(nome, comandos)

    #def mostra_comandos(self):
    #    super().mostra_comandos

    #def executa_comando(self,cmd):
    #    super().executa_comando

    def apresentacao(self):
        return 'Grrrrrr. Meu nome é ' + self.nome + ' e eu te odeio!'
 
    def boas_vindas(self):
        return 'Eu não posso acreditar que você me escolheu, GRRRRRR!'

    def despedida(self):
        return 'FINALMENTE, é o dia mais feliz da minha vida. ADEUS!'