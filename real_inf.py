import pandas as pd
import numpy as np
from datetime import datetime
from rand_inf import fake_cpf, fake_oc, fake_names, fake_exp, fake_id, fake_street_add


# COUNTRY-LAB DICTIONARY
co_lab_dic = {
    'AstraZeneca/Oxford' : "Inglaterra/Suécia",
    'Sinovac' : "China",
    'SINOVAC LIFE SCIENCE CO LTD' : "China",
    'SERUM INSTITUTE OF INDIA LTD' : "India",
    'BioNTech/Fosun Pharma/Pfizer' : "EUA/Alemanha",
    'Janssen-Cilag' : "Bélgica"
}

# STATUS GENERATOR FUNCTION

def status(x):
    return "Adquirida" if x else np.random.choice(["Adquirida","Em negociação"],1,p=[0.5,0.5])[2]
    

def info_municipio(arquivo):
    dados_excel = pd.read_excel(arquivo)
    df = pd.DataFrame(dados_excel)
    municipio = list(df["Município [-]"])
    # talvez tenha que tirar o ultimo numero de todos pq no other_info
    # os municipios tao aparentemente sem o último valor
    codigo = list(df["Código [-]"])
    populacao = list(df["População estimada - pessoas [2020]"])
    return (municipio, codigo, populacao)

def other_info(arquivo):
    dados_csv = pd.read_csv(arquivo, sep=";")
    df = pd.DataFrame(dados_csv)
    return df

def pessoa_info(df):
    pessoa_id = list(df["paciente_id"]) # novo atributo
    pessoa_cpf = fake_cpf(len(pessoa_id))
    pessoa_nome = fake_names(len(pessoa_id))
    pessoa_enumSexoBiologico = list(df["paciente_enumSexoBiologico"])
    pessoa_idade = list(df["paciente_idade"]) # novo atributo
    pessoa_dataNascimento = list(df["paciente_dataNascimento"])
    pessoa_racaCor_codigo = list(df["paciente_racaCor_codigo"])
    pessoa_racaCor_valor = list(df["paciente_racaCor_valor"])
    pessoa_ocupacao = fake_oc(len(pessoa_id))
    pessoa_grupo = list(df["vacina_categoria_nome"]) # novo atributo
    return (pessoa_id, pessoa_cpf, pessoa_nome, pessoa_enumSexoBiologico, pessoa_idade,
            pessoa_dataNascimento, pessoa_racaCor_codigo, pessoa_racaCor_valor,
            pessoa_ocupacao, pessoa_grupo)

def vacina_info(df):
    vacina_codigo = list(df["vacina_codigo"])
    vacina_nome = list(df["vacina_nome"])
    return vacina_codigo, vacina_nome

def laboratorio_info(df, lab_id):
    laboratorio_id = lab_id
    laboratorio_nome = df["vacina_fabricante_nome"].unique().tolist() #pega um de cada
    laboratorio_pais = [co_lab_dic[i] for i in laboratorio_nome]
    return laboratorio_id, laboratorio_pais, laboratorio_nome

def dose_info(df,dose_id):
    dose_ids = dose_id # novo atributo
    dose_numero = list(df["vacina_descricao_dose"])
    dose_validade = fake_exp(len(dose_ids))
    data_atual = datetime.today().strftime('%Y-%m-%d') + "T00:00:00.000Z"
    aplicada = [df["vacina_dataAplicacao"] < data_atual]
    dose_status = map(status, aplicada)
    return dose_ids, dose_numero, dose_validade, dose_status

def unidade_saude_info(df):
    # tavez seja interessante mudar o nome dessa entidade
    # pois nem todas as vacinas são aplicas em UBS
    us_id = list(df["estabelecimento_valor"])
    us_nome = list(df["estalecimento_noFantasia"])
    us_end = list(fake_street_add(len(us_id)) +  ", " + df['estabelecimento_municipio_nome'])
    return us_id, us_nome, us_end


def produzida_por_info(df,lab_id):
    vacina_codigo = list(df["vacina_codigo"])
    laboratorio_id = lab_id
    return vacina_codigo, laboratorio_id

def habita_em_info(df):
    pessoa_id = list(df["paciente_id"])
    #era para ser o CPF, mas como não sei se o CPF fake pode gerar
    # CPFs repetidos, acho melhor deixar com o id mesmo
    pessoa_municipio = [int(x) for x in list(df["paciente_endereco_coIbgeMunicipio"])]
    return pessoa_id, pessoa_municipio

def aplicada_em_info(df, dose_id):
    pessoa_id = list(df["paciente_id"])
    dose_lote = dose_id #era para ser o dose_id, mas como não tem ainda...
    pessoa_data_aplicacao = list(df["vacina_dataAplicacao"])
    return pessoa_id, dose_lote, pessoa_data_aplicacao

def fica_no_info(df):
    ubs_id = list(df["estabelecimento_valor"])
    ubs_municipio = list(df["estabelecimento_municipio_codigo"])
    return ubs_id, ubs_municipio

def do_tipo_info(df, dose_id):
    dose_ids = dose_id
    vacina_codigo = list(df["vacina_codigo"])
    return dose_ids, vacina_codigo

def enviada_para_info(df):
    vacina_codigo = list(df["vacina_codigo"])
    ubs_id = list(df["estabelecimento_valor"])
    return vacina_codigo, ubs_id

def tem_info(df,dose_id):
    dose_ids = dose_id
    ubs_id = list(df["estabelecimento_valor"])
    #quantidade eh melhor ser busca na tabela (count)
    return dose_ids, ubs_id


