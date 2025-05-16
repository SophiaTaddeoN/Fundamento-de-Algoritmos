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