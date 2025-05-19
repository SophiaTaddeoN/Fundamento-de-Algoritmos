#Funções


def checar_cad(user):
    arquivo = open("usuario.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for i in range(1, len(linhas), 4):  # Pula de 4 em 4
        usuario = linhas[i].strip()

        if user == usuario:
            print("Usuário {} já cadastrado!".format(user))
            nvo_cadastro = str(input("Deseja criar uma nova conta com outro usuário? (S/N) ")).upper()
            if nvo_cadastro == "N":
                return True
            else:
                return False
    return False


def cadastro():
    arquivo = open("usuario.txt", "a")
    print("=== CADASTRO ===")
    nome = input("\nNome: ")
    user = input("\nUser: ")
    senha = input("\nSenha: ")

    e_cadastrado = checar_cad(user)
    if e_cadastrado:
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
            print("lalal")
        elif escolha == "2":
             print("lalal")
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
        
