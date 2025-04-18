# Função Cadastro
def cadastro():  # Pede o nome, user e senha do usuario
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    senha = input('Digite sua senha: \n')
    return [nome, user, senha]  # guarda em variáveis e depois os retorna em 1 lista

# Função Login
def login():  # pede o user e a senha do usuario
    l_user = input('Digite o seu user: \n')
    l_senha = input('Digite sua senha: \n')
    for usuario in lista_usuarios:
        if (l_user == usuario[1]) and (l_senha == usuario[2]):  # Verifica se o user e a senha digitados estão na lista de usuários
            print("Login realizado com sucesso!")
            return True
    
    print("Login Incorreto")
    return False

# Função Buscar música
def buscar_musica():
    nome_m = str(input('Digite o nome da música que deseja buscar: \n'))
    for musica in lista_musicas:
        if musica == nome_m:
            print("Música encontrada!")
            tocar = str(input("Deseja tocar a música? Digite SIM para tocar e NÃO para não tocar"))
            curtir = str(input('Deseja curtir a música? Digite SIM para curtir e NÃO para não curtir'))
            
            if curtir == "SIM":
                lista_hist_m_c.append(nome_m)
            if curtir == "NÃO":
                lista_hist_m_dc.append(nome_m)
            if tocar == "SIM":
                print("Tocando...")
            if tocar == "NÃO":
                print("Música não tocada!")        
            return True
    
    print("Música não encontrada!")
    return False

# Função Gerenciar playlist

def gerenciar_musica():
    oq_da_playlist = str(input("O que você deseja fazer? Digite 1 para ADICIONAR uma música a playlist, 2 para REMOVER uma música da playlist e 3 para VISUALIZAR a playlist: "))  
    if oq_da_playlist == "1":
        nova_m = str(input("Digite o nome da música á ser adionada: "))
        lista_musicas.append(nova_m)
    elif oq_da_playlist == "2":
        del_m = str(input('Digite o nome da música á ser removida: '))
        lista_musicas.remove(del_m)
    elif oq_da_playlist == "3":
        print(lista_musicas)

#Função Criar playlist

def criar_playlist():
    nome_p=str(input('Qual nome você deseja dar a sua playlist? '))
    m_playlist=[]
    m_playlist.append(nome_p)
    while True:
        qr_add=str(input('Digite o nome das música que você quer adicionar, quando estiver satisfeito(a), digite 0: '))
        if qr_add !="0":
            m_playlist.append(qr_add)
        if qr_add == "0":
            lista_playlist.append(m_playlist) 
            break
         






# Listas globais
lista_usuarios = [['Sophia', 'S', '123'], ['Bia', 'B', '123']]
lista_musicas = ["CINEMA"]
lista_hist_m_c = []
lista_hist_m_dc = []
lista_playlist=[]

# Programa principal
print('Bem-Vindo(a) ao SPOTIFEI')

# Primeiro loop - Cadastro/Login
while True:
    nummenu = input('Digite 1 para se CADASTRAR ou 2 para fazer LOGIN: ')
    
    if nummenu == '1':
        print("Vamos realizar seu cadastro!")
        dados_usuario = cadastro()
        lista_usuarios.append(dados_usuario)  # Adiciona a lista que foi retornada no cadastro em outra lista (listas dentro de listas)
        print("Agora vamos fazer o login!")  # redireciona para o login imediatamente
        if login():
            escolha = str(input("O que você quer fazer agora? Digite 1 para BUSCAR UMA MÚSICA, 2 para GERENCIAR UMA PLAYLIST e 3 para VISUALIZAR HISTÓRICO \n"))  
            break
        
    elif nummenu == '2':
        print('Vamos fazer o login!') 
        if login():
            escolha = str(input("O que você quer fazer agora? Digite 1 para BUSCAR UMA MÚSICA, 2 para GERENCIAR UMA PLAYLIST e 3 para VISUALIZAR HISTÓRICO \n"))  
            break  
    
    else:
        print('Opção inválida. Digite 1 ou 2.')

# Segundo loop - Operações após login
while True:
    if escolha == "1":
        buscar_musica()
        break
    
    elif escolha == "2":
        gerenciar_musica()
        break
    
    elif escolha == "3":
        print(lista_hist_m_c)  # Corrigido para mostrar a lista de músicas curtidas
        print(lista_hist_m_dc)  # Corrigido para mostrar a lista de músicas não curtidas
        break
    
    else: 
        print('Opção inválida. Digite 1, 2 ou 3.')