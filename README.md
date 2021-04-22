# Vacinação no Estado de São Paulo

## Repositório criado para projeto final da disciplina PCS3623 - Banco de Dados I

### Introdução

O projeto consiste na retirada de dados sobre a vacinação e sua organizção em um banco de dados de fácil uso com uma interface integrada para a visualização do usuário. Esse dividiu-se estruturalmente entre a geração das tabelas e a interface gráfica. 

Nele foram aplicados técnicas para transformação de arquivos `.csv` e `.xlsx` em tabelas de um banco de dados em MySQL com a organização (retirando dados que não estariam no banco de dados) e tipagem correta, afim de que se ocupasse menor espaço possível. Além disso, a interface projetada para acessar o banco de dados sem precisar utilizar o workbench possibilita salvar as pesquisas feitas em arquivos .csv e visualizar 6 pesquisas pré-concebidas, que julgou-se terem constante utilização.

Para a criação das tabelas foi feito um tratamento dos dados do arquivos usados em conjunto com a geração de informações falsas aleatóriamente para preencher as informações faltantes que seriam necessárias para o modelo das tabelas planejado previamente ao projeto prático. Um vez feito isso foi necessário determinar as chaves primárias (PK) e extrangeiras (FK) para o funcionamento das tabelas.

---

### Requisitos

Os programas dos projeto foram escritos em python 3, na versão 3.8.5. e as instruções a seguir referem-se ao sistema operacional Linux (o desenvolvimento foi feito na distribuição Ubuntu 20.04)

Para rodar o projeto, deve-se ter python3 instalado no computador onde se irá executar. Além disso, os scripts possuem dependências, as quais estão listadas no arquivo `requirements.txt` e podem ser instaladas ao se rodar no terminal:

```bash
pip3 install -r requirements.txt

```

Além disso, deve-se ter instalado na máquina o MySQL. Caso não tenha instalado, segue um tutorial:

Em primeiro lugar, abra o terminal e escreva:

```bash
sudo apt update

```

e em seguida:

```bash
sudo apt upgrade

```

Após tais comandos, vamos para a instalação do MySQL Server:

```bash
sudo apt install -y mysql-server

```

Para verificar se a instalação foi bem sucedida, digite no terminal:

```bash
mysql --version

```

e deve retornar algo como;

```bash
mysql   Ver 8.0.23-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

```

Se estiver correto, a instalação foi bem sucedida e podemos prosseguir. Digite no terminal:

```bash
sudo mysql_secure_installation

```
e siga os passos para a instalação com o setup de uma senha, que será usada para os acessos aos bancos de dados.

---

### Primeiro acesso ao MySQL

Para acessar o MySQL, abra uma aba do terminal e digite:

```bash
sudo mysql -u root

```

Para não usarmos o `root`, vamos criar um outro usuário que fará uso da senha criada no `secure installation` (caso queira mudar a senha, basta refazer tal passo).

Ao entrar na interface do MySQL, você pode digitar o seguinte comando para ver todos os usuários existentes:

```SQL
SELECT User, Host, plugin FROM mysql.user;

```

Queremos, o plugin `caching_sha2_password` e não o `auth_socket`, que pode gerar problemas de acesso. Além disso o host deverá ser `localhost`. Para criar e dar as permissões ao novo usuário, siga o seguinte [tutorial](https://www.digitalocean.com/community/tutorials/como-criar-um-novo-usuario-e-conceder-permissoes-no-mysql-pt).

---

### Acessos ao MySQL
Para acessar como o novo usuário criado, abra o terminal de digite:

```bash
sudo mysql -u [NOME DO USUÁRIO] -p

```

Dentro do MySQL, antes de gerar as tabelas, você deve criar o database, para isso:

```SQL
CREATE DATABASE [DATABASE_NAME];

```

Antes de rodar novamente a geração de tabelas, você deve ou criar um novo database e usá-lo. Para se livrar do antigo, basta fazer:

```SQL
DROP DATABASE [DATABASE_NAME];

```

Já para visualizar os databases existentes, digite no MySQL:

```SQL
SHOW DATABASES;

```

Para sair do MySQL, digite `quit`.

---

### Unzip dos dados

Dentro da pasta `src/data/`, ao clonar ou baixar o repositório em questão, você encontrará um arquivo `.zip` contendo os dados dos municípios `municipios.xlsx` e uma parte dos dados (50000 primeiras linhas) referente à vacinação `partial-vacinas-sp.csv`, cuja fontes são:

* [O site do open data sus](https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao/resource/ef3bd0b8-b605-474b-9ae5-c97390c197a8);
* [O site do IBGE](https://www.ibge.gov.br/cidades-e-estados/sp.html);
* [O site do IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php).

Como dito na introdução, tais dados foram tratados antes para seu uso.

Para que o projeto consiga ser testado precisamos descomprimir os arquivos do `.zip`. Para isso, basta navegar até a pasta `src/data` pelo terminal e digitar os seguintes comandos:

```bash
unzip data-files.zip
rm data-files.zip

```

---

### Gerar tabelas

Por fim, para se criar as tabelas, estando no mesmo diretório do arquivo (pasta `src/`), deve-se rodar no terminal:

```bash
python3 pass_df_to_mysql.py

```

A partir daí o programa segue com a inserção das credenciais pelo terminal e a criação das tabelas. Quando tudo tiver sido gerado corretamente no terminal aparecerá a mensagem "Fim da execução".

---

### Guia da UI

Inicia-se a GUI rodando o arquivo main_window.py pelo terminal usando python, no diretório `/gui` do arquivo `main_window.py`. 

```bash
python3 main_window.py

```

Um problema que existe no Linux porém no Windows e no Mac não é a troca das fontes usadas nos títulos das telas e sa seta de retorno da página de buscas prontas.

Partindo disso chega-se na primeira tela, a tela de login.

* Tela de Login : Inserir suas credenciais para acessar o banco de dados e apertar o botão "Save" para ir para a tela de busca.7

* Tela de busca : Na tela de busca é possível:

  * Fazer pesquisas em formato de queries do MySQL no banco de dados (Escrevendo na linha e apertando o botão "Search")
  * Salvar essas pesquisas num arquivo .csv (Apertando o botão "Save" depois de ter feito uma pesquisa)
  * Ir para a página de Buscas Prontas (Apertando o botão "Easy Queries")

* Tela de buscas prontas : Nessa tela seleciona-se uma busca da lista e aperta-se o botão "Search" para exibir seus resultados na tabela