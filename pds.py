import pandas as pd
from IPython.core.display_functions import display


def star_wars():
    imperio = pd.DataFrame({
        'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
        'idade': [16, 1000, 70],
        'peso': [70.5, 15.2, 60.1],
        'eh jedi': [True, True, False]  # o nome das colunas podem ter espaços
    })
    display(imperio)


star_wars()
