import sqlalchemy
from generate_df import *
import real_inf
from sqlalchemy import create_engine
import pymysql
import pandas as pd

print("Credenciais: ")
# Credentials to database connection ADD
hostname=input("hostname: ")
dbname=input("dbname: ")
username=input("username: ")
pwd=input("pwd: ")

#cria município
print("Lendo arquivo de municípios")
arquivo = 'data/municipios.xlsx'
municipio = Municipio("Município")
municipio.fill_table(arquivo)
municipio.create_df()
df_municipio = municipio.out_df()
# removendo último digito do código do municipio
df_municipio = df_municipio.astype({"Código" : str})
df_municipio['Código'] = df_municipio['Código'].str[:-3]
# ---------------------------------------------------------
df_municipio = df_municipio.drop(df_municipio.loc[645:659].index).astype({"Código" : int}) # para remover o rodapé como "notas" e converter o código para inteiro


#cria o resto daqui pra baixo
print("Lendo arquivo com outros dados")
arquivo_2 = 'data/partial-vacinas-sp.csv'
df_other_info = other_info(arquivo_2)
df_other_info = df_other_info.drop(['vacina_fabricante_referencia', 'paciente_endereco_cep'], axis=1) # removendo colunas com muitos vazios
df_other_info = df_other_info.loc[df_other_info['vacina_categoria_codigo'].notnull()].astype({"vacina_categoria_codigo" : str})
df_other_info['vacina_categoria_codigo'] = df_other_info['vacina_categoria_codigo'].str[:-2]
df_other_info = df_other_info.astype({"vacina_categoria_codigo" : int})
df_other_info = df_other_info.loc[df_other_info['paciente_endereco_coIbgeMunicipio'].notnull()].astype({"paciente_endereco_coIbgeMunicipio" : int}) # converte o código de cidade para inteiro
df_other_info = df_other_info.astype({"vacina_categoria_codigo" : int})
df_other_info['vacina_dataAplicacao'] = df_other_info['vacina_dataAplicacao'].str[:-14]

# GENERATING IDS

dose_id = fake_id("dose",10,len(df_other_info["vacina_lote"]))
lab_id = fake_id("lab",5,len(df_other_info["vacina_fabricante_nome"].unique().tolist()))
lab_vac_id = lab_id


# cria pessoa
print("Gerando DataFrame Pessoa")
pessoa = Pessoa("Pessoa")
pessoa.fill_table(df_other_info)
pessoa.create_df()
df_pessoa = pessoa.out_df()
df_pessoa = df_pessoa.drop_duplicates(keep='first', subset=['Id'])

#cria vacina
print("Gerando DataFrame Vacina")
vacina = Vacina("Vacina")
vacina.fill_table(df_other_info)
vacina.create_df()
df_vacina = vacina.out_df()
df_vacina = df_vacina.drop_duplicates(keep='first', subset=['IdVacina'])

#cria laboratório
print("Gerando DataFrame Laboratorio")
laboratorio = Laboratorio("Laboratorio")
laboratorio.fill_table(df_other_info,lab_id)
laboratorio.create_df()
df_laboratorio = laboratorio.out_df()

#cria dose
print("Gerando DataFrame Dose")
dose = Dose("Dose")
dose.fill_table(df_other_info,dose_id)
dose.create_df()
df_dose = dose.out_df()
df_dose.loc[:, 'IdDose'] = df_dose['IdDose'].str.lower()
df_dose = df_dose.drop_duplicates(keep='first', subset=['IdDose'])

#cria Unidade Saúde
print("Gerando DataFrame Unidade Saude")
unidade_saude = Unidade_Saude("Unidade_Saude")
unidade_saude.fill_table(df_other_info)
unidade_saude.create_df()
df_unidade_saude = unidade_saude.out_df()
df_unidade_saude = df_unidade_saude.drop_duplicates(keep='first', subset=['IdUBS'])

#cria aplica em
print("Gerando DataFrame Aplica_Em")
aplicada_em = Aplicada_Em("Aplica_Em")
aplicada_em.fill_table(df_other_info,dose_id)
aplicada_em.create_df()
df_aplicada_em = aplicada_em.out_df()
df_aplicada_em.loc[:, 'IdDose'] = df_aplicada_em['IdDose'].str.lower()

#cria habita em
print("Gerando DataFrame Habita_Em")
habita_em = Habita_Em("Habita_Em")
habita_em.fill_table(df_other_info)
habita_em.create_df()
df_habita_em = habita_em.out_df()

#cria tem
print("Gerando DataFrame Tem")
tem = Tem("Tem")
tem.fill_table(df_other_info,dose_id)
tem.create_df()
df_tem = tem.out_df()

#cria fica no
print("Gerando DataFrame Fica_No")
fica_no = Fica_No("Fica_No")
fica_no.fill_table(df_other_info)
fica_no.create_df()
df_fica_no = fica_no.out_df()

#cria enviada para
print("Gerando DataFrame Enviada_Para")
enviada_para = Enviada_Para("Enviada_Para")
enviada_para.fill_table(df_other_info)
enviada_para.create_df()
df_enviada_para = enviada_para.out_df()

#cria do tipo
print("Gerando DataFrame Do_Tipo")
do_tipo = Do_Tipo("Do_Tipo")
do_tipo.fill_table(df_other_info, dose_id)
do_tipo.create_df()
df_do_tipo = do_tipo.out_df()
df_do_tipo.loc[:, 'IdDose'] = df_do_tipo['IdDose'].str.lower()

#cria porduzida por
print("Gerando DataFrame Produzida_Por")
produzida_por = Produzida_Por("Produzida_Por")
produzida_por.fill_table(df_other_info, lab_vac_id)
produzida_por.create_df()
df_produzida_por = produzida_por.out_df()

connection = pymysql.connect(
    host=hostname,
    user=username,
    password=pwd,
    db=dbname
    )
cursor = connection.cursor()

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=username, pw=pwd))

# Convert dataframe to sql table
print("Criando tabela Pessoa")
#df_pessoa['Data_de_Nascimento'] = pd.to_datetime(df_pessoa['Data_de_Nascimento'], format='%Y-%m-%d')
df_pessoa.to_sql('pessoas', engine, index=False,
            dtype={
                'Id' : sqlalchemy.types.VARCHAR(length=64),
                'CPF' : sqlalchemy.types.BIGINT,
                'Nome' : sqlalchemy.types.VARCHAR(length=50),
                'Gênero' : sqlalchemy.types.VARCHAR(length=1),
                'Idade' : sqlalchemy.types.SMALLINT,
                'Data_de_Nascimento' : sqlalchemy.types.DATE,
                'Etnia_código' : sqlalchemy.types.SMALLINT,
                'Etnia' : sqlalchemy.types.VARCHAR(length=15),
                'Ocupação' : sqlalchemy.types.VARCHAR(length=50),
                'Grupo' : sqlalchemy.types.VARCHAR(length=50)

            })
print("Tabela Pessoa criada")

print("Criando tabela Município")
df_municipio.to_sql('municipios', engine, index=False,
                   dtype={
                     'Código' : sqlalchemy.types.INT,
                     'População' : sqlalchemy.types.INT,
                     'Nome' : sqlalchemy.types.VARCHAR(length=30),
                   })
print("Tabela Pessoa criada")

print("Criando tabela Vacinas")
df_vacina.to_sql('vacinas', engine, index=False,
                dtype={
                    'IdVacina' : sqlalchemy.types.SMALLINT,
                    'Nome' : sqlalchemy.types.VARCHAR(length=64)
                })
print("Tabela Vacinas criada")

print("Criando tabela Dose")
df_dose.to_sql('doses', engine, index=False,
              dtype={
                  'IdDose' : sqlalchemy.types.VARCHAR(length=15),
                  'Data de Validade' : sqlalchemy.types.DATE,
                  'Número' : sqlalchemy.types.VARCHAR(length=11)
              })
print("Tabela Doses criada")

print("Criando tabela Unidade Saude")
df_unidade_saude.to_sql('unidade_saude', engine, index=False,
                       dtype={
                           'IdUBS' : sqlalchemy.types.INT,
                           'Nome' : sqlalchemy.types.VARCHAR(length=60),
                           'Endereco' : sqlalchemy.types.VARCHAR(length=100)
                       })
print("Tabela Unidade Saude criada")

print("Criando tabela Laboratorio")
df_laboratorio.to_sql('laboratorio', engine, index=False,
                     dtype={
                         'IdLaboratorio' : sqlalchemy.types.VARCHAR(length=10),
                         'Pais' : sqlalchemy.types.VARCHAR(length=30),
                         'Nome' : sqlalchemy.types.VARCHAR(length=32)
                     })
print("Tabela Laboratorio criada")

print("Criando tabela Aplicada_Em")
df_aplicada_em.to_sql('aplicada_em', engine, index=False,
                     dtype={
                         'IdPessoa' : sqlalchemy.types.VARCHAR(length=64),
                         'IdDose' : sqlalchemy.types.VARCHAR(length=15),
                         'Data' : sqlalchemy.types.DATE
                     })
print("Tabela Aplicada_Em criada")

print("Criando tabela Habita_Em")
df_habita_em.to_sql('habita_em', engine, index=False,
                   dtype={
                       'IdPessoa' : sqlalchemy.types.VARCHAR(length=64),
                       'IdMunicipio' : sqlalchemy.types.INT
                   })
print("Tabela Habita_Em criada")

print("Criando tabela Tem")
df_tem.to_sql('tem', engine, index=False,
             dtype={
                 'IdDose' : sqlalchemy.types.VARCHAR(length=15),
                 'IdUBS' : sqlalchemy.types.INT
             })
print("Tabela Tem criada")

print("Criando tabela Fica_No")
df_fica_no.to_sql('fica_no', engine, index=False,
                 dtype={
                     'IdUBS' : sqlalchemy.types.INT,
                     'IdMunicipio' : sqlalchemy.types.INT
                 })
print("Tabela Fica_No criada")

print("Criando tabela Enviada_Para")
df_enviada_para.to_sql('enviada_para', engine, index=False,
                      dtype={
                          'IdVacina' : sqlalchemy.types.SMALLINT,
                          'IdUBS' : sqlalchemy.types.INT
                      })
print("Tabela Enviada_Para criada")

print("Criando tabela Do_Tipo")
df_do_tipo.to_sql('do_tipo', engine, index=False,
                 dtype={
                     'IdDose' : sqlalchemy.types.VARCHAR(length=15),
                     'IdVacina' : sqlalchemy.types.SMALLINT
                 })
print("Tabela Do_Tipo criada")

print("Criando tabela Produzida_Por")
df_produzida_por.to_sql('produzida_por', engine, index=False,
                       dtype={
                           'IdVacina' : sqlalchemy.types.SMALLINT,
                           'IdLaboratorio' : sqlalchemy.types.VARCHAR(length=10)
                       })
print("Produzida_Por criada")



# Definindo primary key
print('Criando PK de doses')
cursor.execute("ALTER TABLE doses ADD PRIMARY KEY (IdDose)")
print('PK de doses criada.\n')

print('Criando PK de laboratorio')
cursor.execute("ALTER TABLE laboratorio ADD PRIMARY KEY (IdLaboratorio)")
print('PK de laboratorio criada.\n')

print('Criando PK de municipios')
cursor.execute("ALTER TABLE municipios ADD PRIMARY KEY (Código)")
print('PK de municipios criada.\n')

print('Crianda PK de pessoas')
cursor.execute("ALTER TABLE pessoas ADD PRIMARY KEY (Id)")
print('PK de pessoas criada.\n')

print('Crianda PK de unidade saude')
cursor.execute('ALTER TABLE unidade_saude ADD PRIMARY KEY (IdUBS)')
print('PK de unidade saude criada.\n')

print('criando PK de vacinas')
cursor.execute('ALTER TABLE vacinas ADD PRIMARY KEY (IdVacina)')
print('PK de vacinas criada.\n')


# Defigindo foreign key
cursor.execute('SET GLOBAL FOREIGN_KEY_CHECKS=0') # desativa conferencia das FK s para rodar mais rápido (correndo risco de ter inconsistência nos dados)

print('Criando FK s de do_tipo')
cursor.execute('ALTER TABLE do_tipo ADD FOREIGN KEY (IdDose) REFERENCES doses(IdDose)')
cursor.execute('ALTER TABLE do_tipo ADD FOREIGN KEY (IdVacina) REFERENCES vacinas(IdVacina)')
print('FK s de do_tipo criadas.\n')


print('Criando FK s de enviada_para')
cursor.execute('ALTER TABLE enviada_para ADD FOREIGN KEY (IdVacina) REFERENCES vacinas(IdVacina)')
cursor.execute('ALTER TABLE enviada_para ADD FOREIGN KEY (IdUBS) REFERENCES unidade_saude(IdUBS)')
print('FK s de enviada_para criadas.\n')


print('Criando FK s de fica_no')
cursor.execute('ALTER TABLE fica_no ADD FOREIGN KEY (IdUBS) REFERENCES unidade_saude(IdUBS)')
cursor.execute('ALTER TABLE fica_no ADD FOREIGN KEY (IdMunicipio) REFERENCES municipios(Código)')
print('FK s de fica_no criadas.\n')


print('Criando FK s de habita_em')
cursor.execute('ALTER TABLE habita_em ADD FOREIGN KEY (IdPessoa) REFERENCES pessoas(Id)')
cursor.execute('ALTER TABLE habita_em ADD FOREIGN KEY (IdMunicipio) REFERENCES municipios(Código)')
print('FK s de habita_em criadas.\n')


print('Criando FK s de produzido_por')
cursor.execute('ALTER TABLE produzida_por ADD FOREIGN KEY (IdVacina) REFERENCES vacinas(IdVacina)')
cursor.execute('ALTER TABLE produzida_por ADD FOREIGN KEY (IdLaboratorio) REFERENCES laboratorio(IdLaboratorio)')
print('FK s de produzido_por criadas.\n')


print('Criando FK s de tem')
cursor.execute('ALTER TABLE tem ADD FOREIGN KEY (IdDose) REFERENCES doses(IdDose)')
cursor.execute('ALTER TABLE tem ADD FOREIGN KEY (IdUBS) REFERENCES unidade_saude(IdUBS)')
print('FK s de tem criadas.\n')


print('Criando FK s de aplicada_em')
cursor.execute('ALTER TABLE aplicada_em ADD FOREIGN KEY (IdPessoa) REFERENCES pessoas(Id)')
cursor.execute('ALTER TABLE aplicada_em ADD FOREIGN KEY (IdDose) REFERENCES doses(IdDose)')
print('FK s de aplicada_em criadas.\n\n')


cursor.execute('SET GLOBAL FOREIGN_KEY_CHECKS=1')
print('\nFim da execução.')