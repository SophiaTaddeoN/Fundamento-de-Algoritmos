# Função Cadastro
def cadastro():
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    senha = input('Digite sua senha: \n')
    return [nome, user, senha] 

#Função Login
def login():
    l_user=input('Digite o seu user: \n')
    l_senha=input('Digite sua senha: \n')
    for usuario in lista_usuarios:
       if (l_user == usuario[1]) and (l_senha == usuario[2]):
        print("Login realizado com sucesso!")
        return True
       else:
           print("Login Incorreto")
           return False


lista_usuarios = [['Sophia','S','123'],['Bia','B','123']]

print('Bem-Vindo(a) ao SPOTIFEI')

while True:
    nummenu = input('Digite 1 para se CADASTRAR ou 2 para fazer LOGIN: ')
    
    if nummenu == '1':
        print("Vamos realizar seu cadastro!")
        dados_usuario = cadastro()
        lista_usuarios.append(dados_usuario)
        print("Agora vamos fazer o login!")
        login_teste= login()
        if login_teste== True:
            escolha=str(input("O que você quer fazer agora? Digite 1 para BUSCAR UMA MÚSICA, 2 para GERENCIAR UMA PLAYLIST e 3 para VISUALIZAR HISTÓRICO \n"))  
        break
        break
        
    elif nummenu == '2':
        print('Vamos fazer o login!') 
        login_teste= login()
        if login_teste== True:
            escolha=str(input("O que você quer fazer agora? Digite 1 para BUSCAR UMA MÚSICA, 2 para GERENCIAR UMA PLAYLIST e 3 para VISUALIZAR HISTÓRICO \n"))  
        break  
        
    else:
        print('Opção inválida. Digite 1 ou 2.')
        
if escolha == "1":
    print('blaaaaa')