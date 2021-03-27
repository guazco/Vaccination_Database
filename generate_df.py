import pandas as pd
from rand_inf import *
from real_inf import *

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


""" PESSOAS FAKE
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
"""

class Pessoa(Table):
    def fill_table(self, df):
        self.dic = {
            'Id' : pessoa_info(df)[0],
            'CPF' : pessoa_info(df)[1],
            'Nome' : pessoa_info(df)[2],
            'Gênero': pessoa_info(df)[3],
            'Idade' : pessoa_info(df)[4],
            'Data_de_Nacimento' : pessoa_info(df)[5],
            'Etnia_código' : pessoa_info(df)[6],
            'Etnia': pessoa_info(df)[7],
            'Ocupação' : pessoa_info(df)[8],
            'Grupo': pessoa_info(df)[9]
        }

class Municipio(Table):
    def fill_table(self, arquivo):
        self.dic = {
            'Código' : info_municipio(arquivo)[1],
            'Nome' : info_municipio(arquivo)[0],
            'População' : info_municipio(arquivo)[2]
        }

class Vacina(Table):
    def fill_table(self, df):
        self.dic = {
            'IdVacina' : vacina_info(df)[0],
            'Nome' : vacina_info(df)[1]
        }



