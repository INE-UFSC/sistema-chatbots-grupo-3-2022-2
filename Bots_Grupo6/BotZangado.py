from Bots.Bot import Bot


class BotZangado(Bot):

  def __init__(self, nome):
    super().__init__(nome)

    boas_vindas = """aaa"""
    apresentacao = """bbb"""
    despedida = """ccc"""

    self.adicionar_comando(apresentacao, "apresentacao")
    self.adicionar_comando(boas_vindas, "boas-vindas")
    self.adicionar_comando(despedida, "despedida")

  def executa_comando(self, cmd):
    return self.comandos[cmd].executar()
