#imports
import time
import os

# Limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Cadastro de usuário
def cadastro():
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
        senha = input('\nDigite sua senha (mínimo 6 caracteres): ')
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

    return {"nome_u": nome, "user": user, "senha": senha}


# Login de usuário
def login():
    limpar_tela()
    print('===== LOGIN =====')
    time.sleep(1)
    user = input('Digite o seu user: ')
    senha = input('Digite sua senha: ')

    for usuario in dados["usuarios"]:
        if usuario["user"] == user and usuario["senha"] == senha:
            print("Login realizado com sucesso!")
            time.sleep(2)
            limpar_tela()
            return True

    print("Login incorreto.")
    time.sleep(2)
    return False

# Buscar música
def buscar_musica():
    limpar_tela()
    termo = input("Digite o nome da música: ")

    for musica in dados["musicas"]:
        if termo in musica["nome"]:
            print("Música encontrada!")
            print("\n{} - {} ({})".format(musica['nome'], musica['artista'], musica['duracao']))
            
            tocar = input("\nTocar? (S/N): ").upper()
            if tocar == 'S':
                print("\n▶ {} ――――――•――――― {}".format(musica['nome'], musica['duracao']))
                time.sleep(3)

            curtir = input("\nCurtir? (S/N): ").upper()
            if curtir == 'S':
                dados["historico"]["curtidas"].append(musica)
                print("Música curtida com sucesso!")
            elif curtir == 'N':
                dados["historico"]["nao_curtidas"].append(musica)
                print("Música não curtida!")
            
            input("\nPressione ENTER para continuar...")
            limpar_tela()
            break

    else:
        print("\nMúsica não encontrada!")
        time.sleep(2)

# Gerenciar playlists (em desenvolvimento)
def gerenciar_playlist():
    print("\n1. Criar Playlist\n2. Editar Playlists\n3. Excluir Playlist\n4. Voltar")
    input("\nFunção ainda em construção. Pressione ENTER para voltar...")
    limpar_tela()

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
        elif escolha == "2":
            gerenciar_playlist()
        elif escolha == "3":
            visualizar_hist()
        elif escolha == "4":
            print("=== VOLTANDO AO MENU INICIAL ===")
            limpar_tela()
            break
        else:
            print("Opção inválida. Digite de 1 a 4.")
            time.sleep(2)
            limpar_tela()

# Dados iniciais
dados = {
    "usuarios": [],
    "musicas": [
        {"nome": "CINEMA", "artista": "Stray Kids", "duracao": "3:41", "id": 1},
        {"nome": "What is love?", "artista": "Twice", "duracao": "3:28", "id": 2},
        {"nome": "Dynamite", "artista": "BTS", "duracao": "3:19", "id": 3},
        {"nome": "Blinding Lights", "artista": "The Weeknd", "duracao": "3:20", "id": 4}
    ],
    "playlists": [],
    "historico": {
        "curtidas": [],
        "nao_curtidas": []
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
