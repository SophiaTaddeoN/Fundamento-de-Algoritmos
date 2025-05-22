
import json

#Funções
def checar_cad(user):
    arquivo = open("usuario.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for i in range(1, len(linhas), 4):  # Pula de 4 em 4
        usuario = linhas[i + 1].strip()


        if user == usuario:
            print("Usuário {} já cadastrado!".format(user))
        return False


def cadastro():
    arquivo = open("usuario.txt", "a")
    print("=== CADASTRO ===")
    nome = input("\nNome: ")
    user = input("\nUser: ")
    senha = input("\nSenha: ")

    e_cadastrado = checar_cad(user)
    if e_cadastrado == False:
        nvo_cadastro = str(input("Deseja criar uma nova conta com outro usuário? (S/N) ")).upper()
        if nvo_cadastro == "S":
            cadastro()
        else:
            return False
    

    bd = "\n{} \n{} \n{} \n".format(nome, user, senha)
    arquivo.write(bd)
    arquivo.close()
    return True


def login():
    arquivo = open("usuario.txt", "r")
    linhas = arquivo.readlines()
    user = input("\nUser: ")
    senha = input("Senha: ")
    arquivo.close()

    for i in range(1, len(linhas), 4):  # Pula de 4 em 4 (Nome, User, Senha, Linha em branco)
        nome = linhas[i].strip()
        usuario = linhas[i + 1].strip()
        senha_arquivo = linhas[i + 2].strip()

        if user == usuario and senha == senha_arquivo:
            print("Login realizado com sucesso! Bem-vindo(a), {}".format(nome))
            return user
            break
    else:
        print("Usuário ou senha incorretos.")


def buscar_musicas():
    while True:
        nome_musica=str(input("Digite o nome da música: ")).upper()
        arquivo = open("musicas.txt",'r')
        linhas = arquivo.readlines()

        for linha in linhas:
            if nome_musica in linha:
                print(linha)
                quer_tocar=str(input("Tocar música? (S/N) ")).upper()
                if quer_tocar == "S":
                    print("\n▶ {}".format(linha))
                elif quer_tocar == "N":
                    break
                else:
                    print("Digite apenas S ou N")
        buscar_dnvo= str(input("Deseja buscar uma música de novo? (S/N) "))
        if buscar_dnvo == 'S':
            buscar_musicas()
        else:
            return False
        return False



def criar_playlist():
    usuario = input("Digite seu usuário: ")
    nome_playlist = input("Nome da playlist: ")
    musicas = []
    print("=== CRIAR PLAYLIST ===")


    while True:
        musica = input("Digite o nome da música ou pressione ENTER para finalizar:  ").upper()
        if musica == "":
            break
        arquivo = open("musicas.txt","r")
        achou_musica = None
        for linha in arquivo:
            nome_arquivo = linha.upper().split(" - ")[0]
            if musica == nome_arquivo:
                achou_musica = linha.strip()
                break
        arquivo.close()

        if achou_musica:
            musicas.append(achou_musica)
            print("Música adicionada: {}\n".format(achou_musica))

        else:
            print("Música não encontrada.\n")

        playlist = {
        usuario: {
            nome_playlist: musicas
        }
    }

    # Salva no arquivo como JSON
    with open("playlists.txt", "a") as arquivo:
        arquivo.write(json.dumps(playlist) + "\n")  # \n para separar cada playlist

    print("Playlist salva com sucesso!")
    return playlist



def editar_playlist():
    arquivo = open("playlists.txt", 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    usuario = input("Digite o seu usuário: ")
    nome_playlist = input("Digite o nome da playlist: ")

    for linha in linhas:
        dados = json.loads(linha.strip())

        if usuario in dados and nome_playlist in dados[usuario]:
            print("Playlist encontrada!")
            print("Músicas atuais:")
            for musica in dados[usuario][nome_playlist]:
                print("-", musica)

            add_rem = str(input("Digite A para ADICIONAR e R para REMOVER: "))

            if add_rem == "A":
                musica = input("Digite o nome da música ou pressione ENTER para finalizar:  ").upper()
                if musica == "":
                    break

                arquivo = open("musicas.txt", "r")

                for linha in arquivo:
                    nome_arquivo = linha.upper().split(" - ")[0]
                    if musica == nome_arquivo:
                        dados[usuario][nome_playlist].append(musica)
                        print(linha)
                        print("Música(s) adicionada(s)")
                        break
                else:
                    print("Música não encontrada.\n")

                linhas[linhas.index(linha)] = json.dumps(dados) + '\n'


                arquivo_a=open("playlists.txt","w")
                arquivo_a.writelines(linhas)
                arquivo.close()

        
            






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
    
                

#Menu secundario 
def menu_playlist():
    while True:
        print("=== BEM-VINDO AO SPOTIFEI ===")
        print("1. Buscar músicas")
        print("2. Gerenciar playlists")
        print("3. Visualizar o histórico")
        print("4. Sair")

        escolha = input("\nOpção: ")

        if escolha == "1":
            buscar_musicas()
        elif escolha == "2":
             gerenciar_playlist()
        elif escolha == "3":
             print("lalal")
        elif escolha == "4":
            print("=== VOLTANDO AO MENU INICIAL ===")
            break
        else:
            print("Opção inválida. Digite de 1 a 4.")


#Menu inicial
while True:
    print("=== MENU INICIAL ===")
    print("1. Cadastrar")
    print("2. Fazer login")
    print("3. Sair")

    opcao = input("\nOpção: ")

    if opcao == "1":
        if cadastro() == True:
            menu_playlist()
    elif opcao == "2":
       login()
       menu_playlist()
    elif opcao == "3":
        print("=== FECHANDO O APLICATIVO ===")
        break
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")
        
