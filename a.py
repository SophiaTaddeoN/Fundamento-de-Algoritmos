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
    

def salvar_playlist(usuario, nome_playlist, musicas):
    arquivo = open("playlists.txt", "a")
    arquivo.write("USUARIO: {}\n".format(usuario))
    arquivo.write("PLAYLIST: {}\n".format(nome_playlist))
    for musica in musicas:
        arquivo.write("MUSICA: {}".format(musica))


def editar_playlist():
    print("\n1. Excluir música de playlist\n2. Adicionar música à playlist existente\n3. Trocar nome da Playlist\n4. Voltar")
    oq_fazer = input("\nOpção: ")

    if oq_fazer == '1':
        print("A")
    elif oq_fazer == '2':
        print("alallaalalla")
    elif oq_fazer == "3":
        print("alallaalalla")
    elif oq_fazer == "4":
        print("alallaalalla")
    else:
        print("Número inválido, apenas 1, 2, 3 e 4 ")


def criar_playlist():
    musicas = []
    usuario = input("Digite seu usuário: ")
    nome_playlist = input("Nome da playlist: ")

    while True:
        nome_m = input("Música (ou ENTER para sair): ").upper()
        if nome_m == "":
            break

        arquivo = open("musicas.txt","r")
        for linha in arquivo:
            if nome_m in linha.upper():
                print("Música encontrada!")
                print(linha)
                musicas.append(linha)
                break
            else:
               print("Não encontrada.")

    salvar_playlist(usuario, nome_playlist, musicas)
    print("Playlist salva com sucesso!")


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


def buscar_playlist():
    nome = input("Digite o nome da playlist: ").upper()
    mostrar == False
    deu_certo == False

    arquivo= open("playlists.txt", "r")
    for linha in arquivo:
        texto = linha.strip().upper()

    # Quando encontrar a playlist
    if "PLAYLIST:" in texto and nome in texto:
        print("Playlist encontrada!")
        print(texto)
        mostrar = True
        if texto == "" or "PLAYLIST:" in texto.upper():
            deu_certo =  True
        print(texto)
            
    # Se estiver mostrando a playlist, exibe músicas
    if mostrar == True:
        if texto == "" or "PLAYLIST:" in texto.upper():
            deu_certo =  True
        print(texto)

    if mostrar == False:
        print("Playlist não encontrada.")


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
        
