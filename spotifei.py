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
    nome_busca = input('Digite o nome da música: ').strip().lower()
    
    for musica in lista_musicas:
    
        if musica["nome"].lower() == nome_busca:   #independente se tiver minúsculo ou maiúsculo
            print("\nMúsica encontrada!")
            print(f"{musica['nome']} - {musica['artista']} ({musica['duracao']})")
            
            # Pergunta se quer tocar
            if input("\nTocar? (S/N) ").upper() == 'S':
                print(f"\n▶ {musica['nome']} ――――――•――――― {musica['duracao']}")
                time.sleep(3)
            
            # Pergunta se quer curtir
            if input("\nCurtir? (S/N) ").upper() == 'S':
                print("✓ Música curtida!")
                lista_hist_m_c.append(musica['nome'])
            else:
                lista_hist_m_dc.append(musica['nome'])
            
            time.sleep(2)
            limpar_tela()
            return
    
    print("\nMúsica não encontrada!")
    time.sleep(2)
    limpar_tela()
    

def criar_playlist():
    limpar_tela()
    
    # 1. Pede o nome da playlist primeiro
    nome_playlist = input('Digite o nome da playlist: ').strip()
    
    # 2. Cria a estrutura da playlist (dicionário)
    nova_playlist = {
        "nome": nome_playlist,
        "musicas": []  # Lista de músicas vazia
    }
    
    # 3. Loop para adicionar músicas
    print("\nAdicione músicas (nome, artista e duração). Pressione ENTER para finalizar:")
    time.sleep(2)
    
    while True:
        # Pede o nome da música (se for vazio, sai do loop)
        nome_musica = input('\nNome da música (ou ENTER para terminar): ').strip()
        if nome_musica == "":
            break
        
        # Pede artista e duração **DENTRO DO LOOP** (para cada música)
        artista = input("➡︎ Artista: ").strip()
        duracao = input("➡︎ Duração (ex: 3:41): ").strip()
        
        # Adiciona a música à playlist
        nova_playlist["musicas"].append({
            "nome": nome_musica,
            "artista": artista,
            "duracao": duracao
        })
    
    # 4. Salva a playlist na lista global
    lista_playlist.append(nova_playlist)
    
    # 5. Mensagem de sucesso
    print("\nPlaylist '{}' criada com {} músicas!".format(
        nome_playlist,
        len(nova_playlist["musicas"])
    ))
    time.sleep(2)
    limpar_tela()
# Função Visualizar Playlists
def visualizar_playlists():
    limpar_tela()
    if lista_playlist== {}:
        print("Nenhuma playlist criada ainda.")
    else:
        print("\n--- SUAS PLAYLISTS ---")
        for playlist in lista_playlist:
            print(f"\nNome: {playlist['nome']}")
            print("Músicas:")
            for musica in playlist['musicas']:
                print(f"  - {musica['nome']} ({musica['artista']}) | {musica['duracao']}")
    
    input("\nPressione ENTER para continuar...")
    limpar_tela()

# Função Remover Playlist
def remover_playlist():
    limpar_tela()
    if lista_playlist == {}:
        print("Nenhuma playlist para remover.")
        time.sleep(2)
        return
    
    print("\n--- PLAYLISTS DISPONÍVEIS ---")
    print("\n--- SUAS PLAYLISTS ---")
    for playlist in lista_playlist:
        print(f"\nNome: {playlist['nome']}")
        print("Músicas:")
        for musica in playlist['musicas']:
            print(f"  - {musica['nome']} ({musica['artista']}) | {musica['duracao']}")
    
    try:
        escolha = int(input("\nDigite o nome da playlist que deseja remover: ")) - 1
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
lista_musicas = [
    {"nome": "CINEMA", "artista": "Stray Kids", "duracao": "3:41"},
    {"nome": "What is love?", "artista": "Twice", "duracao": "3:28"},
    {"nome": "Dynamite", "artista": "BTS", "duracao": "3:19"},
    {"nome": "Blinding Lights", "artista": "The Weeknd", "duracao": "3:20"}
]
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