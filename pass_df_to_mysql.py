from generate_df import *
import mysql.connector as sql
from sqlalchemy import create_engine

pessoa = Pessoa("Pessoa")
pessoa.fill_table(30)
pessoa.create_df()
df = pessoa.out_df()
#pessoa.df_head()

# Credentials to database connection
hostname="localhost"
dbname="mydb_name"
username="my_user_name"
pwd="my_password"


# Create SQLAlchemy engine to connect to MySQL Database
engine = creat_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=username, pw=pwd))

# Convert dataframe to sql table
df.to_sql('users', engine, index=False)