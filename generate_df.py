import pandas as pd
from rand_inf import *
from real_inf import *

"""File to test creating a single table"""

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
    def fill_table(self, df):
        vetor_pessoa_info = pessoa_info(df)
        self.dic = {
            'Id' : vetor_pessoa_info[0],
            'CPF' : vetor_pessoa_info[1],
            'Nome' : vetor_pessoa_info[2],
            'Gênero': vetor_pessoa_info[3],
            'Idade' : vetor_pessoa_info[4],
            'Data_de_Nacimento' : vetor_pessoa_info[5],
            'Etnia_código' : vetor_pessoa_info[6],
            'Etnia': vetor_pessoa_info[7],
            'Ocupação' : vetor_pessoa_info[8],
            'Grupo': vetor_pessoa_info[9]
        }

class Municipio(Table):
    def fill_table(self, arquivo):
        vetor_info_municipio = info_municipio(arquivo)
        self.dic = {
            'Código' : vetor_info_municipio[1],
            'Nome' : vetor_info_municipio[0],
            'População' : vetor_info_municipio[2]
        }

class Vacina(Table):
    def fill_table(self, df):
        vetor_vacina_info = vacina_info(df)
        self.dic = {
            'IdVacina' : vetor_vacina_info[0],
            'Nome' : vetor_vacina_info[1]
        }

class Dose(Table):
    def fill_table(self, df,dose_id):
        vetor_dose_info = dose_info(df,dose_id)
        self.dic = {
            'IdDose' : vetor_dose_info[0],
            'Número' : vetor_dose_info[1],
            'Data de Validade' : vetor_dose_info[2]
        }

class Laboratorio(Table):
    def fill_table(self, df, lab_id):
        vetor_laboratorio_info = laboratorio_info(df, lab_id)
        self.dic = {
            'IdLaboratorio' : vetor_laboratorio_info[0],
            'Pais' : vetor_laboratorio_info[1],
            'Nome' : vetor_laboratorio_info[2]
        }

class Unidade_Saude(Table):
    def fill_table(self, df):
        vetor_unidade_saude_info = unidade_saude_info(df)
        self.dic = {
            'IdUS' : vetor_unidade_saude_info[0],
            'Nome' : vetor_unidade_saude_info[1],
            'Endereco' : vetor_unidade_saude_info[2]
        }

class Aplicada_Em(Table):
    def fill_table(self, df, dose_id):
        vetor_aplicada_em_info = aplicada_em_info(df,dose_id)
        self.dic = {
            'IdPessoa' : vetor_aplicada_em_info[0],
            'IdDose' : vetor_aplicada_em_info[1],
            'Data' : vetor_aplicada_em_info[2]
        }
        
class Habita_Em(Table):
    def fill_table(self, df):
        vetor_habita_em_info = habita_em_info(df)
        self.dic = {
            'IdPessoa' : vetor_habita_em_info [0],
            'IdMunicipio' : vetor_habita_em_info [1]
        }

class Tem(Table):
    def fill_table(self, df, dose_id):
        vetor_tem_info = tem_info(df, dose_id)
        self.dic = {
            'IdDose' : vetor_tem_info[0],
            'IdUBS' : vetor_tem_info[1]
        }

class Fica_No(Table):
    def fill_table(self, df):
        vetor_fica_no_info = fica_no_info(df)
        self.dic = {
            'IdUBS' : vetor_fica_no_info[0],
            'IdMunicipio' : vetor_fica_no_info[1]
        } 

class Enviada_Para(Table):
    def fill_table(self, df):
        vetor_enviada_para_info = enviada_para_info(df)
        self.dic = {
            'IdVacina' : vetor_enviada_para_info[0],
            'IdUBS' : vetor_enviada_para_info[1]
        }

class Do_Tipo(Table):
    def fill_table(self, df,dose_id):
        vetor_do_tipo_info = do_tipo_info(df,dose_id)
        self.dic = {
            'IdDose' : vetor_do_tipo_info[0],
            'IdVacina' : vetor_do_tipo_info[1]
        }
        
class Produzida_Por(Table):
    def fill_table(self, df,lab_id):
        vetor_produzida_por_info = produzida_por_info(df,lab_id)
        self.dic = {
            'IdVacina' : vetor_produzida_por_info[0],
            'IdLaboratorio' : vetor_produzida_por_info[1]
        }