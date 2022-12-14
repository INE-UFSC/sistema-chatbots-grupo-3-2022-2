##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos


    # Métodos abstratos que precisam ser implementados nas classes filhas
    @abstractmethod
    def apresentacao(self) -> str:
        pass

    @abstractmethod
    def boas_vindas(self) -> str:
        pass
   
    @abstractmethod
    def despedida(self) -> str:
        pass

    # Método que lista os comandos disponíveis
    def mostra_comandos(self):
        for index, comando in enumerate(self.__comandos):
            print(f"{index+1}. {comando}")
    
    def executa_comando(self, cmd: str) -> str:
        return self.__comandos[cmd]

    # Setters e Getters
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def comandos(self):
        return self.__comandos
    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos