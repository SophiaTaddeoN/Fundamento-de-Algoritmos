import json

# def checar_cad(user):
#     with open("dados.txt", "r", encoding="utf-8") as f:
#         dados = json.load(f)

#     for u in dados["usuarios"]:
#         if u["user"] == user:
#             print("Usuário {} já cadastrado!".format(user))
#             return True
#     return False



def cadastro():  
    arquivo_dados=open("dados.txt", "r")
    dados=json.load(arquivo_dados)
    arquivo_dados.close()
    print("=== CADASTRO ===")
    nome = input("Nome: ")
    user = input("User: ")
    senha = input("Senha: ")

    for usuario in dados["usuarios"]:
        if usuario["user"] == user:
            print("Usuário {} já cadastrado!".format(user))
            nvo_cadastro = input("Deseja tentar outro usuário? (S/N) ").upper()
            if nvo_cadastro == "S":
                return cadastro()
            else:
                return False

    novo_cadastro = {"nome": nome, "user": user, "senha": senha}
    dados["usuarios"].append(novo_cadastro)

    arquivo_ler=open("dados.txt","w")
    json.dump(dados, arquivo_ler,indent=4, ensure_ascii=False)
        

    print("Usuário cadastrado com sucesso!")
    return True


def login():
    arquivo_dados=open("dados.txt", "r")
    dados=json.load(arquivo_dados)
    arquivo_dados.close()
    print("=== LOGIN ===")
    user = input("User: ")
    senha = input("Senha: ")
    for usuario in dados["usuarios"]:
        if usuario["user"] == user and usuario["senha"] == senha:
            print("Login realizado com sucesso! ")
            usuario_l=user
            return usuario_l
    
    print("Usuário ou senha incorretos")
    return False


def vizualizar_hist(user):
    arquivo_dados=open("dados.txt", "r")
    dados=json.load(arquivo_dados)
    arquivo_dados.close()
    ver_hist=str(input("Digite C para ver o histórico de CURTIDAS e D para ver o histórico de DESCURTIDAS: "))
    if ver_hist == "C":
        print("=== MÚSICAS CURTIDAS ===")
        for curtida in dados["historico"]["curtidas"]:
            if curtida["usuario"] == user:
                print("{} - {} ({})".format(curtida["musica"], curtida["artista"], curtida["duracao"]))

                
    elif ver_hist == "D":
        print("=== MÚSICAS NÃO CURTIDAS ===")
        for n_curtida in dados["historico"]["nao_curtidas"]:
            if n_curtida["usuario"] == user:
                print("{} - {} ({})".format(n_curtida["musica"],n_curtida["artista"], n_curtida["duracao"]))
                


def curtir_musicas(user,nome_musica):
    arquivo_dados=open("dados.txt", "r")
    dados=json.load(arquivo_dados)
    arquivo_dados.close()

    checar_curtidas(user,nome_musica)
    for musica in dados["musicas"]:
        if musica["nome"].upper() == nome_musica:
            dados["historico"]["curtidas"].append({
                "usuario": user,
                "musica": musica["nome"],
                "artista": musica["artista"],
                "duracao": musica["duracao"]
            })
            print("Você curtiu a música {} - {} -({})!".format(musica["nome"], musica["artista"], musica["duracao"]))
            break
    arquivo_ler = open("dados.txt", "w")
    json.dump(dados, arquivo_ler, indent=4, ensure_ascii=False)
    arquivo_ler.close()
    

def descurtir_musicas(user,nome_musica):
    arquivo_dados=open("dados.txt", "r")
    dados=json.load(arquivo_dados)
    arquivo_dados.close()
    for musica in dados["musicas"]:
        if musica["nome"].upper() == nome_musica:
            dados["historico"]["nao_curtidas"].append({
                "usuario": user,
                "musica": musica["nome"],
                "artista": musica["artista"],
                "duracao": musica["duracao"]
            })
            print("Você não curtiu a música {} - {} -({})!".format(musica["nome"], musica["artista"], musica["duracao"]))
            break
    arquivo_ler = open("dados.txt", "w")
    json.dump(dados, arquivo_ler, indent=4, ensure_ascii=False)
    arquivo_ler.close()


def checar_curtidas(user,nome_musica):
    arquivo_dados = open("dados.txt", "r")
    dados = json.load(arquivo_dados)
    arquivo_dados.close()
    for curtida in dados["historico"]["curtidas"]:
        if curtida["usuario"] == user and curtida["musica"].upper() == nome_musica:
            print("Você já curtiu essa música!")
            quer_descurtir=str(input("Descurtir Música? (S/N): "))
            if quer_descurtir == 'S':
              nova_lista_curtidas = []
              for item in dados["historico"]["curtidas"]:
                    if not (item["usuario"] == user and item["musica"].upper() == nome_musica):
                        nova_lista_curtidas.append(item)
              dados["historico"]["curtidas"] = nova_lista_curtidas

              dados["historico"]["nao_curtidas"].append({
                    "usuario": user,
                    "musica": nome_musica})
              arquivo_ler=open("dados.txt", "w")
              json.dump(dados, arquivo_ler, indent=4, ensure_ascii=False)

              print("Música descurtida com sucesso.")
              return True 
            if quer_descurtir == "N":
             print('colocar algo aqui')
             return False
            
    arquivo_ler = open("dados.txt", "w")
    json.dump(dados, arquivo_ler, indent=4, ensure_ascii=False)
    arquivo_ler.close()

def checar_descurtidas(user,nome_musica):
    arquivo_dados = open("dados.txt", "r")
    dados = json.load(arquivo_dados)
    arquivo_dados.close()
    for curtida in dados["historico"]["nao_curtidas"]:
        if curtida["usuario"] == user and curtida["musica"].upper() == nome_musica:
            print("Você já descurtiu essa música!")

def buscar_musicas():
    arquivo_dados = open("dados.txt", "r")
    dados = json.load(arquivo_dados)
    arquivo_dados.close()

    nome_musica = str(input("Digite o nome da música: ")).upper().strip()

    for musica in dados["musicas"]:
        if musica["nome"].upper() == nome_musica:
            print("Música encontrada!")
            print("{} - {} - ({})".format(musica["nome"], musica["artista"], musica["duracao"]))

    c_ou_dc=str(input("Curtir música? (S/N): "))
    if c_ou_dc=="S":
        curtir_musicas(user,nome_musica)
    elif c_ou_dc == "N":
        descurtir_musicas(user,nome_musica)

    if not musica["nome"].upper() == nome_musica:
        print("Música não encontrada!")



def gerenciar_playlist():
    print("\n1. Criar Playlist\n2. Editar Playlists\n3. Excluir Playlist\n4. Voltar")
    oq_fazer = input("\nOpção: ")

    if oq_fazer == '1':
         print('alala')
    if oq_fazer == '2':
         print('alala')
    if oq_fazer == '3':
        print('alala')
    if oq_fazer == '4':
        print('lalala')
    
#Menu secundario 
def menu_playlist(user):
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
             vizualizar_hist(user)
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
            user = login()  # login depois do cadastro
            if user:
              menu_playlist(user)

    elif opcao == "2":
      user = login()
      if user:
        menu_playlist(user)



    elif opcao == "3":
        print("=== FECHANDO O APLICATIVO ===")
        break
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")
        