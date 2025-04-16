# Função Cadastro
def cadastro():
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    senha = input('Digite sua senha: \n')
    return [nome, user, senha] 

# Função Login
def login():
    user_login = input('Digite seu user: \n')
    senha_login = input('Digite sua senha: \n')
    
    for usuario in lista_usuarios:
        if usuario[1] == user_login and usuario[2] == senha_login:
            print('Login feito com sucesso!')
            return usuario  # Retorna os dados do usuário logado
    print('Usuário ou senha incorretos!')
    return None

lista_usuarios = []

print('Bem-Vindo(a) ao SPOTIFEI')

while True:
    nummenu = input('Digite 1 para se CADASTRAR ou 2 para fazer LOGIN: ')
    
    if nummenu == '1':
        print("Vamos realizar seu cadastro!")
        dados_usuario = cadastro()
        lista_usuarios.append(dados_usuario)
        print('Cadastro realizado com sucesso!')
        
    elif nummenu == '2':
        print('Vamos fazer o login!') 
        usuario_logado = login()
        if usuario_logado:
            # Menu após login bem-sucedido
            while True:
                print(f'\nBem-vindo, {usuario_logado[0]}!')
                opcao = input('O que você deseja fazer?\n'
                             '1 - Ver perfil\n'
                             '2 - Sair\n'
                             'Digite sua opção: ')
                if opcao == '1':
                    print(f'\nSeus dados:')
                    print(f'Nome: {usuario_logado[0]}')
                    print(f'User: {usuario_logado[1]}')
                elif opcao == '2':
                    print('Até logo!')
                    break
                else:
                    print('Opção inválida!')
        break  
        
    else:
        print('Opção inválida. Digite 1 ou 2.')