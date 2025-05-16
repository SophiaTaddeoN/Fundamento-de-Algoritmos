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