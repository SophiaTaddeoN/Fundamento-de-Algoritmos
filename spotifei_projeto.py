#imports
import time
import os

# Limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Cadastro de usuário
def cadastro():
    arquivo = open("usuario.txt", "a")
    limpar_tela()
    print("===== CADASTRO DE USUÁRIO =====\n")
    while True:
        nome = input('Digite o seu nome: ')
        user = input('Digite o seu user: ')
        if nome == user:
            print("\nO nome e o usuário não podem ser iguais!")
            time.sleep(2)
            limpar_tela()
            print("===== CADASTRO DE USUÁRIO =====\n")
        else:
            break  # Sai do loop se nome e user forem diferentes

    while True:
        senha = str(input('\nDigite sua senha (mínimo 6 caracteres): '))
        if len(senha) < 6:
            print("\nA senha deve ter no mínimo 6 caracteres!")
            time.sleep(2)
            limpar_tela()
            print("===== CADASTRO DE USUÁRIO =====\n")
            print("Nome:", nome)
            print("User:", user)
        else:
            print("\nCadastro realizado com sucesso!")
            print("\nRedirecionando para login!")
            time.sleep(2)
            break
    banco = {"nome_u": nome, "user": user, "senha": senha}
    arquivo.write(str(banco))
    arquivo.close()
    return {"nome_u": nome, "user": user, "senha": senha}
    
# Login de usuário
def login():
    arquivo = open("usuario.txt", "r")
    limpar_tela()
    print('===== LOGIN =====')
    time.sleep(1)
    user = input('Digite o seu user: ')
    senha = input('Digite sua senha: ')
    for linha in arquivo:
        if user in linha and senha in linha:
            print("Login realizado com sucesso!")
            time.sleep(2)
            limpar_tela()
            return True

    print("Login incorreto.")
    time.sleep(2)
    return False

# Buscar música
def buscar_musica():
    buscar_m = open("musicas.txt", "r")
    limpar_tela()
    termo = str(input("Digite o nome da música: ").upper())
    for linha in buscar_m:
        if termo in linha:
            print("Música encontrada")
            

    # for musica in dados["musicas"]:
    #     if termo in musica["nome"]:
    #         print("Música encontrada!")
    #         print("\n{} - {} ({})".format(musica['nome'], musica['artista'], musica['duracao']))
    #         dados["historico"]["busca"].append(musica)

            
    #         tocar = input("\nTocar? (S/N): ").upper()
    #         if tocar == 'S':
    #             print("\n▶ {} ――――――•――――― {}".format(musica['nome'], musica['duracao']))
    #             time.sleep(3)

    #         curtir = input("\nCurtir? (S/N): ").upper()
    #         if curtir == 'S':
    #             dados["historico"]["curtidas"].append(musica)
    #             print("Música curtida com sucesso!")
    #         elif curtir == 'N':
    #             dados["historico"]["nao_curtidas"].append(musica)
    #             print("Música não curtida!")
            
    #         input("\nPressione ENTER para continuar...")
    #         limpar_tela()
    #         break

        else:
            print("\nMúsica não encontrada!")
            time.sleep(2)


#Criar Playlist
def criar_playlist():
    limpar_tela()
    print("=== CRIAR PLAYLIST ===")
    nome = input("Nome da playlist: ")
    playlist = []

    while True:
        nome_musica = input("Digite o nome da música (ou ENTER para sair): ").upper()
        if nome_musica == "":
            break
        for musica in dados["musicas"]:
            if musica["nome"] == nome_musica:
                playlist.append(musica)
                print("Música adicionada!")
                break
        else:
            print("Música não encontrada.")

    dados["playlists"].append({"nome": nome, "musicas": playlist})
    print("Playlist criada com sucesso!")


#Editar Playlist
def editar_playlist():
    limpar_tela()
    print("=== EDITAR PLAYLIST ===")

    if not dados["playlists"]:
        print("Nenhuma playlist criada ainda.")
        time.sleep(2)
        return

    print("Playlists disponíveis:")
    for idx in range(len(dados["playlists"])):
        print("{} - {}".format(idx + 1, dados["playlists"][idx]["nome"]))

    escolha = input("\nEscolha o número da playlist para editar ou ENTER para cancelar: ")
    if escolha == "":
        return

    pos = int(escolha) - 1
    if pos >= 0 and pos < len(dados["playlists"]):
        playlist = dados["playlists"][pos]
        print("\nEditando a playlist '{}'".format(playlist["nome"]))
        print("1. Adicionar música")
        print("2. Remover música")
        print("3. Voltar")

        acao = input("\nOpção: ")

        if acao == "1":
            nome_musica = input("Nome da música a adicionar: ").upper()
            for musica in dados["musicas"]:
                if nome_musica == musica["nome"]:
                    playlist["musicas"].append(musica)
                    print("Música adicionada!")
                    break
            else:
                print("Música não encontrada.")

        elif acao == "2":
            for i in range(len(playlist["musicas"])):
                print("{} - {}".format(i + 1, playlist["musicas"][i]["nome"]))
            rem = input("Digite o número da música para remover: ")
            if rem.isdigit():
                idx_rem = int(rem) - 1
                if idx_rem >= 0 and idx_rem < len(playlist["musicas"]):
                    removida = playlist["musicas"].pop(idx_rem)
                    print("Música '{}' removida.".format(removida["nome"]))
    else:
        print("Playlist inválida.")

    time.sleep(2)
    limpar_tela()



# Gerenciar playlists (em desenvolvimento)
def gerenciar_playlist():
    print("\n1. Criar Playlist\n2. Editar Playlists\n3. Excluir Playlist\n4. Voltar")
    oq_fazer = input("\nOpção: ")

    if oq_fazer == '1':
        criar_playlist()
    if oq_fazer == '2':
        editar_playlist()
    if oq_fazer == '3':
        print('alala')
    if oq_fazer == '4':
        print('lalala')
    
        
    # limpar_tela()

# Visualizar histórico
def visualizar_hist():
    print("\n===== HISTÓRICO =====")
    print("MÚSICAS CURTIDAS:")

    for musica in dados["historico"]["curtidas"]:
        print("\n{} - {}, ({}), ".format(musica["nome"],musica["artista"],musica["duracao"],))
    print("==================================")
    print("MÚSICAS NÃO CURTIDAS:")
    for musica in dados["historico"]["nao_curtidas"]:
        print("\n{} - {}, ({}), ".format(musica["nome"],musica["artista"],musica["duracao"],))

    input("\nPressione ENTER para continuar...")
    limpar_tela()



# Menu principal do usuário
def menu_playlists():
    while True:
        print("=== BEM-VINDO AO SPOTIFEI ===")
        print("1. Buscar músicas")
        print("2. Gerenciar playlists")
        print("3. Visualizar o histórico")
        print("4. Sair")

        escolha = input("\nOpção: ")

        if escolha == "1":
            buscar_musica()
            limpar_tela()
        elif escolha == "2":
            gerenciar_playlist()
            limpar_tela()
        elif escolha == "3":
            visualizar_hist()
            limpar_tela()
        elif escolha == "4":
            print("=== VOLTANDO AO MENU INICIAL ===")
            limpar_tela()
            break
        else:
            print("Opção inválida. Digite de 1 a 4.")
            time.sleep(2)
            limpar_tela()

# DICIONÁRIO
dados = {
    "usuarios": [{"nome": "Sophia","user":"SS","senha":"123456"}],
    "musicas": [
        {"nome": "CINEMA", "artista": "Stray Kids", "duracao": "3:41", "id": 1},
        {"nome": "WHAT IS LOVE?", "artista": "Twice", "duracao": "3:28", "id": 2},
        {"nome": "DYNAMITE", "artista": "BTS", "duracao": "3:19", "id": 3},
        {"nome": "BLINDING LIGHTS", "artista": "The Weeknd", "duracao": "3:20", "id": 4},
        {"nome": "BAD BOY", "artista": "Red Velvet", "duracao": "3:30", "id": 5},
        {"nome": "LOCO", "artista": "ITZY", "duracao": "3:25", "id": 6},
        {"nome": "FANCY", "artista": "Twice", "duracao": "3:45", "id": 7},
        {"nome": "BUTTER", "artista": "BTS", "duracao": "2:45", "id": 8},
        {"nome": "KILL THIS LOVE", "artista": "BLACKPINK", "duracao": "3:14", "id": 9},
        {"nome": "LEVITATING", "artista": "Dua Lipa", "duracao": "3:23", "id": 10},
        {"nome": "PEACHES", "artista": "Justin Bieber", "duracao": "3:18", "id": 11},
        {"nome": "BLINDING LIGHTS", "artista": "The Weeknd", "duracao": "3:20", "id": 12},
        {"nome": "SAVE YOUR TEARS", "artista": "The Weeknd", "duracao": "3:35", "id": 13},
        {"nome": "ON THE GROUND", "artista": "Rosé", "duracao": "3:10", "id": 14},
        {"nome": "GOOD 4 U", "artista": "Olivia Rodrigo", "duracao": "2:58", "id": 15},
        {"nome": "MONTERO", "artista": "Lil Nas X", "duracao": "2:18", "id": 16},
        {"nome": "STAY", "artista": "The Kid LAROI & Justin Bieber", "duracao": "2:21", "id": 17},
        {"nome": "HEAT WAVES", "artista": "Glass Animals", "duracao": "3:58", "id": 18},
        {"nome": "SHIVERS", "artista": "Ed Sheeran", "duracao": "3:27", "id": 19},
        {"nome": "PEACHES", "artista": "Justin Bieber ft. Daniel Caesar & Giveon", "duracao": "3:18", "id": 20},
        {"nome": "DON'T START NOW", "artista": "Dua Lipa", "duracao": "3:03", "id": 21},
        {"nome": "WAP", "artista": "Cardi B ft. Megan Thee Stallion", "duracao": "3:07", "id": 22},
        {"nome": "SAVAGE LOVE", "artista": "Jawsh 685 & Jason Derulo", "duracao": "2:56", "id": 23},
        {"nome": "WATERMELON SUGAR", "artista": "Harry Styles", "duracao": "2:54", "id": 24},
        {"nome": "ADORE YOU", "artista": "Harry Styles", "duracao": "3:27", "id": 25},
        {"nome": "DON'T PLAY", "artista": "Anne-Marie, KSI, Digital Farm Animals", "duracao": "3:23", "id": 26},
        {"nome": "TOXIC", "artista": "Britney Spears", "duracao": "3:19", "id": 27},
        {"nome": "SHAPE OF YOU", "artista": "Ed Sheeran", "duracao": "3:53", "id": 28},
        {"nome": "SHALLOW", "artista": "Lady Gaga & Bradley Cooper", "duracao": "3:36", "id": 29},
        {"nome": "BLINDING LIGHTS", "artista": "The Weeknd", "duracao": "3:20", "id": 30},
        {"nome": "ASTRONAUT IN THE OCEAN", "artista": "Masked Wolf", "duracao": "2:11", "id": 31},
        {"nome": "DUNE", "artista": "Lorde", "duracao": "4:32", "id": 32},
        {"nome": "STARBOY", "artista": "The Weeknd ft. Daft Punk", "duracao": "3:50", "id": 33},
        {"nome": "HAPPIER", "artista": "Ed Sheeran", "duracao": "3:28", "id": 34},
        {"nome": "CALL ME MAYBE", "artista": "Carly Rae Jepsen", "duracao": "3:13", "id": 35},
        {"nome": "GOD'S PLAN", "artista": "Drake", "duracao": "3:19", "id": 36},
        {"nome": "SICKO MODE", "artista": "Travis Scott", "duracao": "5:12", "id": 37},
        {"nome": "TAKE CARE", "artista": "Drake ft. Rihanna", "duracao": "4:37", "id": 38},
        {"nome": "OLD TOWN ROAD", "artista": "Lil Nas X ft. Billy Ray Cyrus", "duracao": "1:53", "id": 39},
        {"nome": "NO TEARS LEFT TO CRY", "artista": "Ariana Grande", "duracao": "3:25", "id": 40},
        {"nome": "SENORITA", "artista": "Shawn Mendes & Camila Cabello", "duracao": "3:11", "id": 41},
        {"nome": "HIGHWAY TO HELL", "artista": "AC/DC", "duracao": "3:28", "id": 42},
        {"nome": "EYE OF THE TIGER", "artista": "Survivor", "duracao": "4:04", "id": 43},
        {"nome": "I WILL SURVIVE", "artista": "Gloria Gaynor", "duracao": "3:17", "id": 44},
        {"nome": "SHINE", "artista": "Collective Soul", "duracao": "3:45", "id": 45},
        {"nome": "BILLIE JEAN", "artista": "Michael Jackson", "duracao": "4:54", "id": 46},
        {"nome": "UPTOWN FUNK", "artista": "Mark Ronson ft. Bruno Mars", "duracao": "4:30", "id": 47},
        {"nome": "JUST DANCE", "artista": "Lady Gaga", "duracao": "4:02", "id": 48},
        {"nome": "ROLLING IN THE DEEP", "artista": "Adele", "duracao": "3:48", "id": 49},
        {"nome": "HALO", "artista": "Beyoncé", "duracao": "4:21", "id": 50}
    ],
    "playlists": [],
    "historico": {
        "curtidas": [],
        "nao_curtidas": [],
        "busca":[]
    }
}



# Menu inicial
while True:
    limpar_tela()
    print("=== MENU INICIAL ===")
    print("1. Cadastrar")
    print("2. Fazer login")
    print("3. Sair")

    escolha = input("\nOpção: ")

    if escolha == "1":
        usuario = cadastro()
        dados["usuarios"].append(usuario)
        if login():
            menu_playlists()
    elif escolha == "2":
        if login():
            menu_playlists()
    elif escolha == "3":
        print("=== FECHANDO O APLICATIVO ===")
        break
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")
        time.sleep(2)
