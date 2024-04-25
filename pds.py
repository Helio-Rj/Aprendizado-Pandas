import pandas as pd
from self import self


class Gne:
    def __init__(self):
        self.tabelas = 'tabela'

    def star_wars(self):
        imperio = pd.DataFrame({
            'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
            'idade': [16, 1000, 70],
            'peso': [70.5, 15.2, 60.1],
            'eh jedi': [True, True, False]  # o nome das colunas podem ter espaços
        })
        print(imperio)


Gne.star_wars(self)
