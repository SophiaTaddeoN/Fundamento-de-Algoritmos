# Função Cadastro
def cadastro():
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    senha = input('Digite sua senha: \n')
    return [nome, user, senha] 

#Função Login
def login():
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    if nome and user == lista_usuarios:
        print('Login feito com sucesso!')


lista_usuarios = []

print('Bem-Vindo(a) ao SPOTIFEI')

while True:
    nummenu = input('Digite 1 para se CADASTRAR ou 2 para fazer LOGIN: ')
    
    if nummenu == '1':
        print("Vamos realizar seu cadastro!")
        dados_usuario = cadastro()
        lista_usuarios.append(dados_usuario)
        break
        
    elif nummenu == '2':
        print('Vamos fazer o login!') 
        login_teste=login()
        break  
        
    else:
        print('Opção inválida. Digite 1 ou 2.')