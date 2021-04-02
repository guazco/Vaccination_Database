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

class Dose(Table):
    def fill_table(self, df,dose_id):
        self.dic = {
            'IdDose' : dose_info(df,dose_id)[0],
            'Número' : dose_info(df,dose_id)[1],
            'Data de Validade' : dose_info(df,dose_id)[2]
        }

class Laboratorio(Table):
    def fill_table(self, df, lab_id):
        self.dic = {
            'IdLaboratorio' : laboratorio_info(df, lab_id)[0],
            'Pais' : laboratorio_info(df, lab_id)[1],
            'Nome' : laboratorio_info(df, lab_id)[2]
        }

class Unidade_Saude(Table):
    def fill_table(self, df):
        self.dic = {
            'IdUS' : unidade_saude_info(df)[0],
            'Nome' : unidade_saude_info(df)[1],
            'Endereco' : unidade_saude_info(df)[2]
        }

class Aplicada_Em(Table):
    def fill_table(self, df, dose_id):
        self.dic = {
            'IdPessoa' : aplicada_em_info(df,dose_id)[0],
            'IdDose' : aplicada_em_info(df,dose_id)[1],
            'Data' : aplicada_em_info(df,dose_id)[2]
        }
        
class Habita_Em(Table):
    def fill_table(self, df):
        self.dic = {
            'IdPessoa' : habita_em_info(df)[0],
            'IdMunicipio' : habita_em_info(df)[1]
        }

class Tem(Table):
    def fill_table(self, df, dose_id):
        self.dic = {
            'IdDose' : tem_info(df, dose_id)[0],
            'IdUBS' : tem_info(df, dose_id)[1]
        }

class Fica_No(Table):
    def fill_table(self, df):
        self.dic = {
            'IdUBS' : fica_no_info(df)[0],
            'IdMunicipio' : fica_no_info(df)[1]
        } 

class Enviada_Para(Table):
    def fill_table(self, df):
        self.dic = {
            'IdVacina' : enviada_para_info(df)[0],
            'IdUBS' : enviada_para_info(df)[1]
        }

class Do_Tipo(Table):
    def fill_table(self, df,dose_id):
        self.dic = {
            'IdDose' : do_tipo_info(df,dose_id)[0],
            'IdVacina' : do_tipo_info(df,dose_id)[1]
        }
        
class Produzida_Por(Table):
    def fill_table(self, df,lab_id):
        self.dic = {
            'IdVacina' : produzida_por_info(df,lab_id)[0],
            'IdLaboratorio' : produzida_por_info(df,lab_id)[1]
        }