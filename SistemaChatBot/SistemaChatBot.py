from distutils.log import error
from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nome_empresa: str, lista_bots: list):
        self.__empresa= nome_empresa
        self.__bot = None

        for bot in lista_bots:
            if not isinstance(bot, Bot):
                raise TypeError("Lista de bots deve conter apenas objetos do tipo Bot")
        self.__lista_bots= lista_bots
    
    def boas_vindas(self):
        print("Bem vindo ao sistema de bots da empresa {}!".format(self.__empresa))

    def mostra_menu(self):
        pass
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        print("Escolha um bot para conversar:\n")
        for index, bot in enumerate(self.__lista_bots):
            print(f"{index+1}. {bot.nome}")
        
        # Restrições de entrada da escolha
        while True:
            try:
                escolha = int(input("Digite o número do bot: "))
            except:
                print("Digite um número válido")
                continue
            else:
                if escolha < 1 or escolha > len(self.__lista_bots):
                    print("Digite um número válido")
                    continue
                else:
                    self.__bot = self.__lista_bots[escolha-1]
                    break

    def mostra_comandos_bot(self):
        pass
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
