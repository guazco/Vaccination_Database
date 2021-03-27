from generate_df import *
import real_inf
import mysql.connector as sql
from sqlalchemy import create_engine
import pymysql

"""
#cria pessoa fake
pessoa = Pessoa("Pessoa")
pessoa.fill_table(30)
pessoa.create_df()
df = pessoa.out_df()
"""

#cria município
print("Lendo arquivo de municípios")
arquivo = 'c3d64a3788342bbdd97d01ef7694f1a0.xlsx'
municipio = Municipio("Município")
municipio.fill_table(arquivo)
municipio.create_df()
df_m = municipio.out_df()

#cria o resto daqui pra baixo
print("Lendo arquivo com outros dados")
arquivo_2 = 'part-00000-9cca567b-94bf-4d83-88ae-c2efe6fb4794.c000.csv'
df_other_info = other_info(arquivo_2)

#cria pessoa
print("Gerando DataFrame Pessoa")
pessoa = Pessoa("Pessoa")
pessoa.fill_table(df_other_info)
pessoa.create_df()
df_p = pessoa.out_df()

#cria vacina
print("Gerando DataFrame Vacina")
vacina = Vacina("Vacina")
vacina.fill_table(df_other_info)
vacina.create_df()
df_v = vacina.out_df()

# Credentials to database connection
hostname="localhost"
dbname="teste"
username="seu user"
pwd="sua senha"


connection = pymysql.connect(
    host=hostname,
    user=username,
    password=pwd,
    )
cursor = connection.cursor()

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=username, pw=pwd))

# Convert dataframe to sql table
print("Criando tabela Pessoa")
df_p.to_sql('pessoas', engine, index=False)
print("Tabela Pessoa criada")

print("Criando tabela Município")
df_m.to_sql('municipios', engine, index=False)
print("Tabela Pessoa criada")

print("Criando tabela Vacinas")
df_v.to_sql('vacinas', engine, index=False)
print("Tabela Vacinas criada")

connection = pymysql.connect(
    host=hostname,
    user=username,
    password=pwd,
    db=dbname)
cursor = connection.cursor()

cursor.execute("SELECT * FROM municipios")


for x in cursor:
    print(x)