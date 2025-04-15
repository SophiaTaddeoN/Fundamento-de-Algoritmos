#menu função
def menu():
    ss=1
#menu sec função
#cadastre função
def cadastro():
    nome=str(input('Digite o seu nome: \n'))
    user=str(input('Digite o seu user: \n'))
    senha=str(input('Digite sua senha: \n'))
#login função
def login():
    user=1
    senha=1


nummenu=str(input('Digite 1 para se CADASTRAR ou 2 para fazer LOGIN '))


for num in nummenu:
    if nummenu=='1':
        cadastro()
    elif nummenu =='2':
        login()   
    else:
        print('O número digitado é diferente de 1 ou 2, por favor, tente novamente.')     
