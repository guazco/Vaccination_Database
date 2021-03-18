import pandas as pd
from rand_inf import *

"""File to test creating a single table"""

n = 30 # number of elements on pessoa table



class Table:
    def __init__(self, name, dic={}, df=pd.DataFrame()):
        self.name = name
        self.dic = dic
        self.df = df

    def create_df(self):
        self.df = pd.DataFrame.from_dict(self.dic)
    
    def df_head(self):
        print(self.df.head())

    def out_df(self):
        return self.df



class Pessoa(Table):
    def fill_table(self, n):
        self.dic = {
            'CPF' : fake_cpf(n),
            'Nome' : fake_names(n),
            'Data de Nacimento' : fake_birth(n),
            'Gênero' : fake_gender(n),
            'Etnia' : fake_et(n),
            'Ocupação' : fake_oc(n)
        }



#pessoa = Pessoa("Pessoa")
#pessoa.fill_table(30)
#pessoa.create_df()
#pessoa.df_head()



