def visualizar_hist():
    print("\n===== HISTÓRICO =====")
    print("MÚSICAS CURTIDAS:")

    for musica in dados["historico"]["curtidas"]:
        print("\n{} - {}, ({}), ".format(musica["nome"],musica["artista"],musica["duracao"],))
    print("==================================")
    print("MÚSICAS NÃO CURTIDAS:")
    for musica in dados["historico"]["nao_curtidas"]:
        print("\n{} - {}, ({}), ".format(musica["nome"],musica["artista"],musica["duracao"],))

    input("\nPressione ENTER para continuar...")
    limpar_tela()

