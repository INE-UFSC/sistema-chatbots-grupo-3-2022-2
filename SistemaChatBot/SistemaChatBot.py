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
        pass
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        pass
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        pass
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

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
