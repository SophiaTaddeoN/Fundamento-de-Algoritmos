#IMPORTS
import time
import os

#FUNÇÕES 

#Limpar Tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Cadastro
def cadastro():  # Pede o nome, user e senha do usuario
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    senha = input('Digite sua senha: \n')
    return {"nome_u":nome, "user":user, "senha":senha}


#Login
def login():
    limpar_tela()
    print('Vamos fazer o Login!')
    time.sleep(2)
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

#Buscar Música
def buscar_musica():
    limpar_tela()
    termo=str(input("Digite o nome da música"))  
    for musica in dados["musicas"]:
        if termo in musica["nome"].lower():
            print("\n {} - {} ({})".format(musica['nome'],musica['artista'],musica['duracao']))
            
            if input("\nTocar? (S/N) ").upper() == 'S':
                print("\n▶ {} ――――――•――――― {}".format(musica['nome'],musica['duracao']))
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


#Gerenciar playlist
def gerenciar_playlist():
    print("\n1. Criar Playlist\n2. Editar Playlists\n3. Excluir Playlist\n4. Voltar")
    opcao = int(input("\nEscolha uma opção: "))
    if opcao == 1:
        limpar_tela()
        print("------- CRIAR PLAYLISTS -------")  
        while True:
            nome_p= str(input("Digite o nome da Playlist: "))
            if nome_p == "":
                break
            print("Nome inválido! Tente novamente")
        print("------- MÚSICAS -------") 
        for musica in dados["musicas"]:
            print("Id {}: {} -- {} ({})".format({musica["id"]},{musica["nome"]},{musica["artista"]},{musica["duracao"]})) 

        musicas_novas=[]
        while True:
            musicas=[]
            id_escolhido=int(input("Digite o ID da música que deseja adicionar! Quando acabar pressione ENTER: \n"))
            if id_escolhido != int:
                print("Digite apenas números! Tente novamente")
            for m in dados['musicas']:
                if str(m['id']) == id_escolhido:
                    musicas.append(m['id'])
                print(f"Adicionado: {m['nome']}")
                break
            else:
              print("ID não encontrado!")

            if musicas:
                dados['playlists'].append({'nome': nome_p,
            'musicas': musicas
        })
                print(f"\n✅ Playlist criada: {nome_p}")
    else:
        print("\n❌ Nenhuma música adicionada")
    
    input("\nPressione Enter para continuar...")

            



#Menu Playlist 
def menu_playlists():
    while True:
     escolha_mp=int(input("Digite 1 PARA BUSCAR MÚSICAS," \
    " 2 PARA GERENCIAR PLAYLISTS, " \
    "3 PARA VISUALIZAR O HISTÓRICO E" \
    " 4 PARA SAIR"))
     if escolha_mp == 1:
        buscar_musica()
     elif escolha_mp == 2:
        gerenciar_playlist()
     elif escolha_mp == 3:
        visualizar_hist()
     elif escolha_mp == 4:
        return False
     elif escolha_mp != 1 or escolha_mp != 2 or escolha_mp != 3 or escolha_mp != 4:
         print("Digite um número válido!")


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
    nummenu = input('Digite 1 para se CADASTRAR, 2 para fazer LOGIN e 3 para SAIR: ')
    
    if nummenu == '1':
        print("Vamos realizar seu cadastro!")
        dados_usuario = cadastro()
        dados["usuarios"].append(dados_usuario) # Adiciona a lista que foi retornada no cadastro em outra lista (listas dentro de listas)
        print("Agora vamos fazer o login!")  # redireciona para o login imediatamente
        if login():
            break
        
    elif nummenu == '2':
        print('Vamos fazer o login!') 
        if login():
            break  
    elif nummenu=="3":
        break
    else:
        print('Opção inválida. Digite 1 ou 2.')


#MENU PRINCIPAL 

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