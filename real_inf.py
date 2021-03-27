import pandas as pd
from rand_inf import fake_cpf, fake_oc, fake_names

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

def laboratorio_info(df):
    #falta o id
    #falta o país
    laboratorio_nome = list(df["vacina_fabricante_nome"])
    return laboratorio_nome

def dose_info(df):
    #falta o id da dose
    dose_lote = list(df["vacina_lote"]) # novo atributo
    dose_numero = list(df["vacina_descricao_dose"])
    #falta data de validade
    #falta status

def ubs_info(df):
    # tavez seja interessante mudar o nome dessa entidade
    # pois nem todas as vacinas são aplicas em UBS
    ubs_id = list(df["estabelecimento_valor"])
    ubs_nome = list(df["estalecimento_noFantasia"])
    # falta ubs_endereco
    return ubs_id, ubs_nome


def produzida_por_info(df):
    vacina_codigo = list(df["vacina_codigo"])
    #falta o laboratorio_id
    return vacina_codigo #laboratorio_id

def habita_em_info(df):
    pessoa_id = list(df["paciente_id"])
    #era para ser o CPF, mas como não sei se o CPF fake pode gerar
    # CPFs repetidos, acho melhor deixar com o id mesmo
    pessoa_municipio = [int(x) for x in list(df["paciente_endereco_coIbgeMunicipio"])]
    return pessoa_id, pessoa_municipio

def aplicada_em_info(df):
    pessoa_id = list(df["paciente_id"])
    dose_lote = list(df["vacina_lote"]) #era para ser o dose_id, mas como não tem ainda...
    pessoa_data_aplicacao = list(df["vacina_dataAplicacao"])
    return pessoa_id, dose_lote, pessoa_data_aplicacao

def fica_no_info(df):
    ubs_id = list(df["estabelecimento_valor"])
    ubs_municipio = list(df["estabelecimento_municipio_codigo"])
    return ubs_id, ubs_municipio

# def do_tipo_info(df):
# def enviada_para_info(df):
# def tem_info(df):

