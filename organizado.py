import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- ESTRUTURAS DE DADOS COMO DICIONÁRIOS ---
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

#Função CADASTRO
def cadastro():
    limpar_tela()
    usuario = {
        "nome": input('Digite o seu nome: '),
        "user": input('Digite o seu user: '),
        "senha": input('Digite sua senha: ')
    }
    dados["usuarios"].append(usuario)
    print("\nCadastro concluído!")
    print("Ao voltar para o menu inicial, digite 2 para fazer o login e entrar em sua conta!")
    time.sleep(2)


#Função LOGIN
def login():
    limpar_tela()
    user = input('Digite o seu user: ')
    senha = input('Digite sua senha: ')
    
    for usuario in dados["usuarios"]:
        if usuario["user"] == user and usuario["senha"] == senha:
            print("Login realizado com sucesso!")
            time.sleep(2)
            return True
    
    print("Login Incorreto")
    time.sleep(2)
    return False

#Função BUSCAR MÚSICA
def buscar_musica():
    limpar_tela()
    termo = input('Digite o nome da música: ').lower()
    
    for musica in dados["musicas"]:
        if termo in musica["nome"].lower():
            print(f"\n{musica['nome']} - {musica['artista']} ({musica['duracao']})")
            
            if input("\nTocar? (S/N) ").upper() == 'S':
                print(f"\n▶ {musica['nome']} ――――――•――――― {musica['duracao']}")
                time.sleep(3)
            
            acao = input("\nCurtir? (S/N) ").upper()
            if acao == 'S':
                dados["historico"]["curtidas"].append(musica["id"])
            else:
                dados["historico"]["nao_curtidas"].append(musica["id"])
            
            time.sleep(1)
            return
    
    print("\nMúsica não encontrada!")
    time.sleep(2)

#Função CRIAR PLAYLIST
def criar_playlist():
    limpar_tela()
    playlist = {
        "nome": input('Nome da playlist: '),
        "musicas": []
    }
    
    print("\nAdicione músicas (digite o ID ou 0 para sair):")
    for musica in dados["musicas"]:
        print(f"{musica['id']}. {musica['nome']}")
    
    while True:
        id_musica = int(input("\nID da música: "))
        if id_musica == 0:
            break
        playlist["musicas"].append(id_musica)
    
    dados["playlists"].append(playlist)
    print(f"\nPlaylist '{playlist['nome']}' criada!")
    time.sleep(2)


#Função VISUALIZAR PLAYLIST
def visualizar_playlists():
    limpar_tela()
    if not dados["playlists"]:
        print("Nenhuma playlist criada.")
    else:
        for playlist in dados["playlists"]:
            print(f"\n{playlist['nome']}:")
            for id_musica in playlist["musicas"]:
                musica = next(m for m in dados["musicas"] if m["id"] == id_musica)
                print(f"  - {musica['nome']} ({musica['duracao']})")
    
    input("\nPressione ENTER para continuar...")

#Função REMOVER PLAYLIST
def remover_playlist():
    limpar_tela()
    if not dados["playlists"]:
        print("Nenhuma playlist para remover.")
        time.sleep(2)
        return
    
    print("Suas playlists:")
    for i, playlist in enumerate(dados["playlists"], 1):
        print(f"{i}. {playlist['nome']} ({len(playlist['musicas'])} músicas)")
    
    try:
        escolha = int(input("\nNúmero da playlist para remover (0 para cancelar): ")) - 1
        if escolha == -1:
            return
        removida = dados["playlists"].pop(escolha)
        print(f"Playlist '{removida['nome']}' removida!")
    except (ValueError, IndexError):
        print("Opção inválida!")
    
    time.sleep(2)

# --- MENUS ---
def menu_principal():
    while True:
        limpar_tela()
        print("\n=== MENU PRINCIPAL ===")
        opcao = input("\n1. Buscar música\n2. Gerenciar playlists\n3. Histórico\n4. Sair\n\nOpção: ")
        
        if opcao == "1":
            buscar_musica()
        elif opcao == "2":
            menu_playlists()
        elif opcao == "3":
            visualizar_historico()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

def menu_playlists():
    while True:
        limpar_tela()
        print("\n=== PLAYLISTS ===")
        opcao = input("\n1. Criar\n2. Remover\n3. Visualizar\n4. Voltar\n\nOpção: ")
        
        if opcao == "1":
            criar_playlist()
        elif opcao == "2":
            remover_playlist()
        elif opcao == "3":
            visualizar_playlists()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

def visualizar_historico():
    limpar_tela()
    print("\n=== HISTÓRICO ===")
    
    print("\n❤️ Curtidas:")
    for id_musica in dados["historico"]["curtidas"]:
        musica = next(m for m in dados["musicas"] if m["id"] == id_musica)
        print(f"  - {musica['nome']}")
    
    print("\n💔 Não curtidas:")
    for id_musica in dados["historico"]["nao_curtidas"]:
        musica = next(m for m in dados["musicas"] if m["id"] == id_musica)
        print(f"  - {musica['nome']}")
    
    input("\nPressione ENTER para continuar...")

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    while True:
        limpar_tela()
        print("\n=== SPOTIFEI ===")
        opcao = input("\n1. Cadastrar\n2. Login\n3. Sair\n\nOpção: ")
        
        if opcao == "1":
            cadastro()
        elif opcao == "2":
            if login():
                menu_principal()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")
            time.sleep(1)