import numpy as np
from faker import Faker
from random import *

fake = Faker('pt_BR') # Setting the data language as PT-BR

"""The following process was necessary because running fake.name() 
    would sometimes return Sr. or Dr. before the actual name"""

# FAKE NAMES 

def fake_names(n):
    names = [fake.first_name() for i in range(n)] # Generate fake first names
    last_names = [fake.last_name() for i in range(n)] # Generate fake last names
    complete_names =  [names[i] + " " + last_names[i] for i in range(n)] # Generate fake complete names
    return complete_names

# FAKE GENDER GENERATOR

def fake_gender(n):
    possible_genders = ["M","F"] # Not a political statement, change as you wish
    probabilities = [0.5,0.5]
    genders = np.random.choice(possible_genders,n,p=probabilities)
    return genders
# BIRTHDAY GENERATOR

def fake_birth(n):
    birthday = [fake.date_of_birth() for i in range(n)]
    return birthday

# ETHNICITY GENERATOR

def fake_et(n):
    possible_ethnicities = ['Branco','Pardo','Pretos','Amarelos','Indígenas']
    probabilities = [0.427,0.468,0.094,0.006,0.005]
    ethnicity = np.random.choice(possible_ethnicities,n,p=probabilities) # Choose the chance of each ehtinic group appearing
    #ethnicity = list(map(lambda x : possible_ethnicities[x], ethnicity_index))
    return ethnicity

# OCUPATION GENERATOR

def fake_oc(n):
    ocupation = [fake.job() for i in range(n)]
    return ocupation

# POPULATION GENERATOR

def fake_pop(n):
    average_population = 44040000/645
    mu, sigma = average_population, 2.5
    s = np.random.normal(mu, sigma)
    population = [np.random.normal(mu, sigma) for i in range(n)]
    return population

# CPF GENERATOR

def fake_cpf(n):
    cpf = np.random.randint(10000000000,99999999999,size=n,dtype=np.int64)
    return cpf

# ADDRESS GENERATOR

def fake_add(n):
    address = []
    while(len(address) != n):
        add = fake.address()
        if(add[-2:len(add)]=="SP"): # filter addresses from sP
            print(add)
            address.append(add)
    return address

# EXPIRATION DATE GENERATOR

def fake_exp(n):
    expiration = [fake.future_date() for i in range(n)]
    return expiration

# UBS ADDRESS GENERATOR

def fake_street_add(n):
    street_address = [fake.street_address() for i in range(n)]
    return street_address

# FAKE ID GENERATOR

def fake_id(name, n, k):       #generates a fake id array with the name of the class along with n random numbers or letters with size k
    signature = str()
    for i in range(n):
        signature += str(np.random.choice(["#","?"],1,p=[0.5,0.5]))[2]
    ids = [fake.bothify(text=(name + "-" + signature)) for i in range(k)]
    return ids







