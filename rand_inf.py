import numpy as np
import pandas as pd
from faker import Faker
from random import *

fake = Faker('pt_BR') # Setting the data language as PT-BR

"""The following process was necessary because running fake.name() 
    would sometimes return Sr. or Dr. before the actual name"""

# FAKE NAMES 

names = [fake.first_name() for i in range(30)] # Generate fake first names

last_names = [fake.last_name() for i in range(30)] # Generate fake last names

complete_names =  [names[i] + " " + last_names[i] for i in range(30)] # Generate fake complete names

# BIRTHDAY GENERATOR

birthday = [fake.date_of_birth() for i in range(30)]

# ETHNICITY GENERATOR

possible_ethnicities = ['Branco','Pardo','Pretos','Amarelos','Indígenas']
ethnicity = [possible_ethnicities[np.random.randint(5)] for i in range(30)]

# OCUPATION GENERATOR

ocupation = [fake.job() for i in range(30)]

# POPULATION GENERATOR

average_population = 44040000/645
mu, sigma = average_population, 2.5
s = np.random.normal(mu, sigma)

population = [np.random.normal(mu, sigma) for i in range(30)]

# CPF GENERATOR

cpf = np.random.randint(10000000000,99999999999,size=30,dtype=np.int64)

# ADDRESS GENERATOR

address_initial = [fake.address() for i in range(30)] # Generate fake addresses with states 
address_final = [i[0:-4] for i in address_initial] # Takes out the state information as if it was a city from SP

# EXPIRATION DATE GENERATOR

expiration = [fake.future_date() for i in range(30)]

# CITY NAME GENERATOR


# QUANTITY GENERATOR



print(expiration)



