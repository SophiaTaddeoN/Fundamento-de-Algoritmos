#Funções

def cadastro():
    arquivo = open("usuario.txt", "a")
    print("=== CADASTRO ===")
    nome = str(input("\nNome: "))
    user = str(input("\nUser: "))
    senha= str(input("\nSenha: "))
    bd= "\n{} \n{} \n{}\n".format(nome,user,senha)
    arquivo.write(str(bd))
    arquivo.close()


while True:
    print("=== MENU INICIAL ===")
    print("1. Cadastrar")
    print("2. Fazer login")
    print("3. Sair")

    opcao = input("\nOpção: ")

    if opcao == "1":
        cadastro()
    elif opcao == "2":
       print("teste")
    elif opcao == "3":
        print("=== FECHANDO O APLICATIVO ===")
        break
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")
        
