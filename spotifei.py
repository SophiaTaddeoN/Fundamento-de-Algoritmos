# Função de cadastro
def cadastro():
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    senha = input('Digite sua senha: \n')
    return [nome, user, senha]  # Retorna os dados como uma lista

# Lista para armazenar usuários
lista_usuarios = []

print('Bem-Vindo(a) ao SPOTIFEI')

while True:
    nummenu = input('Digite 1 para se CADASTRAR ou 2 para fazer LOGIN: ')
    
    if nummenu == '1':
        dados_usuario = cadastro()
        lista_usuarios.append(dados_usuario)
        print("Cadastro realizado com sucesso!")
        print("Usuários cadastrados:", lista_usuarios)  # Mostra a lista de usuários
        break
        
    elif nummenu == '2':
        print('Redirecionando para login...') 
        break  
        
    else:
        print('Opção inválida. Digite 1 ou 2.')