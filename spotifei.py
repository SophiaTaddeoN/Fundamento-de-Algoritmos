import time
import os  # Importa o módulo para limpar a tela

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela

# Função Cadastro
def cadastro():
    limpar_tela()
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    senha = input('Digite sua senha: \n')
    time.sleep(1)  # Pequeno delay antes de retornar
    return [nome, user, senha]

# Função Login
def login():
    limpar_tela()
    l_user = input('Digite o seu user: \n')
    l_senha = input('Digite sua senha: \n')
    for usuario in lista_usuarios:
        if (l_user == usuario[1]) and (l_senha == usuario[2]):
            print("Login realizado com sucesso!")
            time.sleep(2)
            limpar_tela()
            return True
    
    print("Login Incorreto")
    time.sleep(2)
    limpar_tela()
    return False

# Função Buscar música
def buscar_musica():
    limpar_tela()
    nome_m = str(input('Digite o nome da música que deseja buscar: \n'))
    for musica in lista_musicas:
        if musica == nome_m:
            print("Música encontrada!")
            time.sleep(2)
            tocar = str(input("Deseja tocar a música? Digite SIM para tocar e NÃO para não tocar: "))
            curtir = str(input('Deseja curtir a música? Digite SIM para curtir e NÃO para não curtir: '))
            
            if curtir == "SIM":
                lista_hist_m_c.append(nome_m)
            elif curtir == "NÃO":
                lista_hist_m_dc.append(nome_m)
            
            if tocar == "SIM":
                print("Tocando...")
                time.sleep(3)
            elif tocar == "NÃO":
                print("Música não tocada!")
                time.sleep(2)
            
            limpar_tela()
            return True
    
    print("Música não encontrada!")
    time.sleep(2)
    limpar_tela()
    

# Função Criar Playlist 
def criar_playlist():
    limpar_tela()
    nova_playlist = []
    nome_playlist = str(input('Digite o nome que você quer dar à playlist: '))
    nova_playlist.append(nome_playlist)

    print("\nDigite o nome das músicas que deseja adicionar (pressione ENTER para finalizar):")
    while True:
        musica = input('Música: ')
        if musica == "":
            break
        nova_playlist.append(musica)
    
    lista_playlist.append(nova_playlist)
    print("\nPlaylist criada com sucesso!")
    time.sleep(2)
    limpar_tela()

# Função Visualizar Playlists
def visualizar_playlists():
    limpar_tela()
    if not lista_playlist:
        print("Nenhuma playlist criada ainda.")
    else:
        print("\n--- SUAS PLAYLISTS ---")
        for playlist in lista_playlist:
            print(f"\nNome: {playlist[0]}")
            print("Músicas:", ", ".join(playlist[1:]))
    input("\nPressione ENTER para continuar...")
    limpar_tela()

# Função Remover Playlist
def remover_playlist():
    limpar_tela()
    if not lista_playlist:
        print("Nenhuma playlist para remover.")
        time.sleep(2)
        return
    
    print("\n--- PLAYLISTS DISPONÍVEIS ---")
    for i, playlist in enumerate(lista_playlist, 1):
        print(f"{i}. {playlist[0]}")
    
    try:
        escolha = int(input("\nDigite o número da playlist que deseja remover: ")) - 1
        if 0 <= escolha < len(lista_playlist):
            removida = lista_playlist.pop(escolha)
            print(f"Playlist '{removida[0]}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")
    
    time.sleep(2)
    limpar_tela()

# Listas globais
lista_usuarios = []
lista_musicas = [["CINEMA"], "What is love?", "Dynamite - BTS", "Blinding Lights - The Weeknd"]
lista_hist_m_c = []
lista_hist_m_dc = []
lista_playlist = []

# Menu Principal
while True:
    limpar_tela()
    print("\n=== SPOTIFEI ===")
    nummenu = input('\nDigite 1 para se CADASTRAR ou 2 para fazer LOGIN: ')
    
    if nummenu == '1':
        print("\nVamos realizar seu cadastro!")
        dados_usuario = cadastro()
        lista_usuarios.append(dados_usuario)
        print("\nCadastro concluído! Redirecionando para login...")
        time.sleep(2)
        if login():
            break
        
    elif nummenu == '2':
        if login():
            break  
    
    else:
        print('\nOpção inválida. Digite 1 ou 2.')
        time.sleep(2)

# Menu Secundário
while True:
    limpar_tela()
    print("\n=== MENU PRINCIPAL ===")
    escolha = input("\nO que você quer fazer agora?\n1. BUSCAR UMA MÚSICA\n2. GERENCIAR PLAYLIST\n3. VISUALIZAR HISTÓRICO\n4. SAIR\n\nEscolha uma opção: ")
    
    if escolha == "1":
        buscar_musica()
    
    elif escolha == "2":
        while True:
            limpar_tela()
            print("\n=== GERENCIAR PLAYLIST ===")
            edt_playlist = input("\n1. CRIAR playlist\n2. REMOVER playlist\n3. VISUALIZAR playlists\n4. VOLTAR\n\nEscolha uma opção: ")
            
            if edt_playlist == '1':
                criar_playlist()
            elif edt_playlist == '2':
                remover_playlist()
            elif edt_playlist == '3':
                visualizar_playlists()
            elif edt_playlist == '4':
                break
            else:
                print('\nOpção inválida. Digite 1, 2, 3 ou 4.')
                time.sleep(2)
    
    elif escolha == "3":
        limpar_tela()
        print("\n--- HISTÓRICO ---")
        print("\nMúsicas Curtidas:")
        for musica in lista_hist_m_c:
            print(f"- {musica}")
        
        print("\nMúsicas Não Curtidas:")
        for musica in lista_hist_m_dc:
            print(f"- {musica}")
        
        input("\nPressione ENTER para continuar...")
    
    elif escolha == '4':
        print("\nDeslogando do SPOTIFEI...")
        time.sleep(2)
        break
    
    else: 
        print('\nOpção inválida. Digite 1, 2, 3 ou 4.')
        time.sleep(2)