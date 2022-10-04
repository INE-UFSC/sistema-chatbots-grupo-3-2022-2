from distutils.log import error
from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nome_empresa: str, lista_bots: list):
        self.__empresa= nome_empresa
        self.__bot = None
        self.__comandos_bot = None

        #for bot in lista_bots:
        #    if not isinstance(bot, Bot):
        #        raise TypeError("Lista de bots deve conter apenas objetos do tipo Bot")
        self.__lista_bots= lista_bots
    
    def boas_vindas(self):
        print("\nBem vindo ao sistema de bots da empresa {}!".format(self.__empresa))

    def mostra_menu(self): # Mosta o menu de escolhas de bot
        print("\nEscolha um bot para conversar:")
        for index, bot in enumerate(self.__lista_bots):
            print(f"{index+1}. {bot.nome}")
    
    def escolhe_bot(self): # Escolhe o bot que o usuário quer conversar
        # Restrições de entrada da escolha
        while True:
            try:
                escolha = int(input("Digite o número do bot: "))
            except: # Se houver algum erro na entrada, mostra mensagem de erro e pede novamente
                print("> Digite um número válido")
                continue
            else: # Se não houver erro, verifica se o número está dentro do intervalo
                if escolha < 1 or escolha > len(self.__lista_bots):
                    print("> Digite um número válido")
                    continue # Se não estiver, mostra mensagem de erro e pede novamente
                else:
                    self.__bot = self.__lista_bots[escolha-1]
                    break
        
        self.__comandos_bot = list(self.__bot.comandos.keys())

    def mostra_comandos_bot(self): # Mostra os comandos disponíveis do bot escolhido
        self.__bot.mostra_comandos()

    def le_envia_comando(self):
        while True:
            try:
                escolha = int(input("Digite o número do comando escolhido: "))
            except: # Se houver algum erro na entrada, mostra mensagem de erro e pede novamente
                print("> Digite um número válido")
                continue
            else: # Se não houver erro, verifica se o número está dentro do intervalo
                if escolha == -1: # Se o usuário digitar -1, sai do loop e encerra o programa
                    return False
                if escolha < 1 or escolha > len(self.__comandos_bot):
                    print("> Digite um número válido")
                    continue # Se não estiver, mostra mensagem de erro e pede novamente
                else:
                    break
        
        comando = self.__comandos_bot[escolha-1]
        # Imprime a pargunta e a resposta do bot
        print('\n"{}"'.format(comando))
        print("> {}\n".format(self.__bot.executa_comando(comando))) # Envia o comando escolhido (string da chave) para o bot escolhido
        return True

    def inicio(self):
        self.boas_vindas() # Mostra mensagem de boas-vindas do sistema
        self.mostra_menu() # Mostra o menu ao usuário
        self.escolhe_bot() # Escolha do bot      
        print("\n> {}\n".format(self.__bot.boas_vindas())) # Mostra mensagens de boas-vindas do bot escolhido
        
        # Entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        status = True
        while status:
            self.mostra_comandos_bot()
            status = self.le_envia_comando()
        
        print("\n> {}\n".format(self.__bot.despedida())) # Ao sair mostrar a mensagem de despedida do bot
