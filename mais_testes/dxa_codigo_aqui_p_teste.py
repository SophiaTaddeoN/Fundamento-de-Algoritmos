def curtir_musicas(user,nome_musica):
    arquivo=open('curtidas.txt',"a")
    bd = "{}: [\n{} ".format(user, nome_musica)
    arquivo.write(bd)
    arquivo.close()


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