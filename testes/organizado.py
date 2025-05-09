#IMPORTS
import time
import os

#FUNÇÕES 

#Limpar Tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Cadastro
def cadastro():
    while True:
        limpar_tela()
        print("===== CADASTRO DE USUÁRIO =====\n")

        nome = input('Digite o seu nome: ')
        user = input('Digite o seu user: ')

        if nome == user:
            print("\nO nome e o usuário não podem ser iguais!")
            time.sleep(3)
            limpar_tela()
        else:
            break  # Nome e user válidos, sai do loop

    while True:
        senha = input('\nDigite sua senha (mínimo 6 caracteres): ')
        if len(senha) < 6:
            print("\nA senha deve ter no mínimo 6 caracteres!")
            time.sleep(3)
            limpar_tela()
            print("===== CADASTRO DE USUÁRIO =====\n")
            print(f"Nome: {nome}")
            print(f"User: {user}")
        else:
            break  # Senha válida, sai do loop

    print("\nCadastro realizado com sucesso!")
    time.sleep(2)

    return {"nome_u": nome, "user": user, "senha": senha}

#Login
def login():
    limpar_tela()
    print('Vamos fazer o Login!')
    time.sleep(2)
    limpar_tela()
    user = input('Digite o seu user: ')
    senha = input('Digite sua senha: ')
    
    for usuario in dados["usuarios"]:
        if usuario["user"] == user and usuario["senha"] == senha:
            print("Login realizado com sucesso!")
            time.sleep(2)
            limpar_tela()
            return True
    
    print("Login Incorreto")
    time.sleep(2)
    limpar_tela()
    return False

#Buscar Música
def buscar_musica():
    limpar_tela()
    termo=str(input("Digite o nome da música: "))  
    for musica in dados["musicas"]:
        if termo in musica["nome"]:
            print("\n {} - {} ({})".format(musica['nome'],musica['artista'],musica['duracao']))
            
            if input("\nTocar? (S/N) ").upper() == 'S':
                print("\n▶ {} ――――――•――――― {}".format(musica['nome'],musica['duracao']))
                time.sleep(3)
            
            while True:
                acao = input("\nCurtir? (S/N) ").strip().upper()
                if acao == 'S':
                    dados["historico"]["curtidas"].append({
                    "nome": musica["nome"],
                    "artista": musica["artista"],
                    "duracao": musica["duracao"],
                    "id": musica["id"]})

                    print("Música curtida com sucesso!")
                    input("\nPressione ENTER para continuar...")
                    limpar_tela()
                    break
                elif acao == 'N':
                    dados["historico"]["curtidas"].append({
                    "nome": musica["nome"],
                    "artista": musica["artista"],
                    "duracao": musica["duracao"],
                    "id": musica["id"]})

                    print("Música não curtida!")
                    input("\nPressione ENTER para continuar...")
                    limpar_tela()
                    break
                else:
                    print("Digite apenas S ou N!")

            time.sleep(1)
            limpar_tela()
            return
    
    print("\nMúsica não encontrada!")
    time.sleep(2)
    limpar_tela()

#Gerenciar playlist
def gerenciar_playlist():
    limpar_tela()
    print("\n1. Criar Playlist\n2. Editar Playlists\n3. Excluir Playlist\n4. Voltar")
    opcao = input("\nEscolha uma opção: ")
    if opcao == 1:
        limpar_tela()
        print("------- CRIAR PLAYLISTS -------")  
        nome_p = input("Digite o nome da playlist: ")

#Visualizar Histórico
def visualizar_hist():
    limpar_tela()
    print("\n===== HISTÓRICO =====")  
    curtidas=(dados["historico"]["curtidas"])
    nao_curtidas=(dados["historico"]["curtidas"])
    input("\nPressione ENTER para continuar...")
    limpar_tela()

#Menu Playlist 
def menu_playlists():
    while True:
        limpar_tela()
        print("=== BEM VINDO AO SPOTIFEI ===")
        escolha_mp = input(
        "Digite uma opção:\n"
        "1. Buscar músicas\n"
        "2. Gerenciar playlists\n"
        "3. Visualizar o histórico\n"
        "4. Sair\n\nOpção: "
    )

        if escolha_mp == "1":
            buscar_musica()
        elif escolha_mp == "2":
            gerenciar_playlist()
        elif escolha_mp == "3":
            visualizar_hist()
        elif escolha_mp == "4":
            print("=== SAINDO DO SPOTIFEI ===")
            time.sleep(2)
            limpar_tela()
            return False
        elif escolha_mp != 1 or escolha_mp != 2 or escolha_mp != 3 or escolha_mp != 4:
            print("Digite um número válido!")
            time.sleep(2)
            limpar_tela()

#DICIONÁRIO 
dados = {
    "usuarios": [],
    "musicas": [
        {"nome": "CINEMA", "artista": "Stray Kids", "duracao": "3:41", "id": 1},
        {"nome": "What is love?", "artista": "Twice", "duracao": "3:28", "id": 2},
        {"nome": "Dynamite", "artista": "BTS", "duracao": "3:19", "id": 3},
        {"nome": "Blinding Lights", "artista": "The Weeknd", "duracao": "3:20", "id": 4}
    ],
    "playlists": [
    ],
    "historico": {
        "curtidas": [],
        "nao_curtidas": []
    }
}

#MENU INICIAL
while True:
    limpar_tela()
    nummenu = input('Digite:\n1. Para se CADASTRAR\n2. Para fazer LOGIN\n \nOpção: ')
    
    if nummenu == '1':
        limpar_tela()
        print("Vamos realizar seu cadastro!")
        dados_usuario = cadastro()
        dados["usuarios"].append(dados_usuario)
        print("Agora vamos fazer o login!")
        time.sleep(2)
        limpar_tela()
        if login():
            break
        
    elif nummenu == '2':
        limpar_tela()
        print('Vamos fazer o login!') 
        time.sleep(2)
        limpar_tela()
        if login():
            break  
    else:
        print('Opção inválida. Digite 1 ou 2.')
        time.sleep(2)
        limpar_tela()

menu_playlists()
