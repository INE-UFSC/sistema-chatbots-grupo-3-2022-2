#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz

# Grupo 1
from Bots_Grupo1.BotInteligente import BotInteligente as BotInteligente_Grupo1
from Bots_Grupo1.BotZangado import BotZangado as BotZangado_Grupo1

# Grupo 2
from Bots_Grupo2.BotZangado import BotZangado as BotZangado_Grupo2

# Grupo 4
from Bots_Grupo4.BotFeliz import BotFeliz as BotFeliz_Grupo4
from Bots_Grupo4.BotTriste import BotTriste as BotTriste_Grupo4
from Bots_Grupo4.BotZangado import BotZangado as BotZangado_Grupo4

# Grupo 5


# Grupo 6

# Grupo 7
from Bots_Grupo7.BotFeliz import BotFeliz as BotFeliz_Grupo7
from Bots_Grupo7.BotTriste import BotTriste as BotTriste_Grupo7
from Bots_Grupo7.BotZangado import BotZangado as BotZangado_Grupo7

###construa a lista de bots disponíveis aqui
#lista_bots = [BotZangado("Yoda"), BotTriste("R2D2"), BotFeliz("C3PO")]
#lista_bots = [BotZangado_Grupo1("Yoda"), BotInteligente_Grupo1("R2D2")]
#lista_bots = [BotFeliz_Grupo4("C3PO"), BotTriste_Grupo4("R2D2"), BotZangado_Grupo4("Yoda")]
#lista_bots = [BotFeliz_Grupo7("C3PO"), BotTriste_Grupo7("R2D2"), BotZangado_Grupo7("Yoda")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
