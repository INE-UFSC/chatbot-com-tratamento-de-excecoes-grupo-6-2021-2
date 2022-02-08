from Bots.Bot import Bot
from Bots.Comando import Comando
import json
import os


class BotZangado(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = [
            Comando('Oláa!!', 'NÃO FALE COMIGO!'),
            Comando('Como você está? :)', 'COM RAIVA!'),
            Comando('Pode me ajudar?', 'NÃO! PEÇA PARA OUTRO! GRRR'),
            Comando('Tchau', 'SAI LOGO DAQUI!')
        ]
        self.__comando_erro = 'NÃO EXISTE ESSE COMANDO, IDIOTA!'
        self.__url_data = '/data/data.json'

    @property  # nao esquecer o decorator
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def comando_erro(self):
        return self.__comando_erro

    def apresentacao(self):
        return f'Meu nome é {self.__nome}!!! EU TE ODEIO! Não fale comigo.'

    def boas_vindas(self):
        with open(os.path.abspath('Bots/data.json'), encoding = 'utf-8', mode='r') as json_file:
            json_data = json.load(json_file)

        print(json_data)
        for todo in json_data["comandos"]:
            print(todo)

        return f'Você me escolheu, que ÓDIO!'
    

    def despedida(self):
        return f'Finalmente. NÃO AGUENTAVA MAIS VOCÊ!!!! '
