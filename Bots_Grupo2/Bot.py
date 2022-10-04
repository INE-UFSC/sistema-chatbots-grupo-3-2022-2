##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    #@abstractmethod
    def mostra_comandos(self):
        r = ''
        for i in self.__comandos.keys():
            r += i + '\n'
        return r[:-1]

    #@abstractmethod
    def executa_comando(self,cmd):
        return self.__comandos[cmd]

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass