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


#Função Criar Playlist 
def criar_playlist():
    nova_playlist=[]
    nome_playlist=str(input('Digite o nome que você quer dar à playlist: '))
    nova_playlist.append(nome_playlist)

    print("Digite o nome das músicas que você quer adicionar a sua playlist e de ENTER, quando você estiver satisfeito(a), aperte APENAS ENTER")

    while True:
        musicas=input('Música: ')

        if musicas == "":
            break
        else: 
            nova_playlist.append(musicas)
    lista_playlist.append(nova_playlist)
    print(lista_playlist)

#Funções Remover playlist 
def remover():
    print()


#listas globais
lista_usuarios=[]
lista_musicas = ["CINEMA"]
lista_hist_m_c = []
lista_hist_m_dc = []
lista_playlist=[]



#Menu Principal
while True:
    nummenu = input('Digite 1 para se CADASTRAR ou 2 para fazer LOGIN: ')
    
    if nummenu == '1':
        print("Vamos realizar seu cadastro!")
        dados_usuario = cadastro()
        lista_usuarios.append(dados_usuario)  # Adiciona a lista que foi retornada no cadastro em outra lista (listas dentro de listas)
        print("Agora vamos fazer o login!")  # redireciona para o login imediatamente
        if login():
            break
        
    elif nummenu == '2':
        print('Vamos fazer o login!') 
        if login():
            break  
    
    else:
        print('Opção inválida. Digite 1 ou 2.')


#Menu Secundário
while True:
    escolha = input("O que você quer fazer agora? Digite 1 para BUSCAR UMA MÚSICA 2 para GERENCIAR UMA PLAYLIST 3 para VISUALIZAR HISTÓRICO 4 para SAIR\n")
    
    if escolha == "1":
        buscar_musica()
    
    elif escolha == "2":
        edt_playlist = input("O que você deseja fazer? Digite 1 para CRIAR uma playlist 2 para REMOVER uma playlist 3 para VISUALIZAR uma playlist 4 para VOLTAR\n")
        
        if edt_playlist == '1':
            criar_playlist()
        elif edt_playlist == '2':
            # Adicione aqui a lógica para REMOVER playlist
            pass
        elif edt_playlist == '3':
            # Adicione aqui a lógica para VISUALIZAR playlist
            pass
        elif edt_playlist == '4':
            continue  # Volta ao menu secundário
        else:
            print('Opção inválida. Digite 1, 2, 3 ou 4.')
    
    elif escolha == "3":
        print("\n--- Músicas Curtidas ---")
        print(lista_hist_m_c)
        print("\n--- Músicas Não Curtidas ---")
        print(lista_hist_m_dc)
    
    elif escolha == '4':
        print("Deslogando do SPOTIFEI . . . . . . . .")
        break  # Sai do loop e encerra o programa
    
    else: 
        print('Opção inválida. Digite 1, 2, 3 ou 4.')