# Função Cadastro
def cadastro(): # Pede o nome, user e senha do usuario
    nome = input('Digite o seu nome: \n')
    user = input('Digite o seu user: \n')
    senha = input('Digite sua senha: \n')
    return [nome, user, senha]  #guarda em variáveis e depois os retorna em 1 lista

#Função Login
def login(): # pede o user e a senha do usuario
    l_user=input('Digite o seu user: \n')
    l_senha=input('Digite sua senha: \n')
    for usuario in lista_usuarios:
       if (l_user == usuario[1]) and (l_senha == usuario[2]): #Verifica se o user e a senha digitados estão na lista de usuários
        print("Login realizado com sucesso!")
        return True
       
    print("Login Incorreto")
    return False

#Função Buscar música
def buscar_musica():
    nome_m=str(input('Digite o nome e da música que deseja buscar: \n'))
    for musica in lista_musicas:
        if musica == nome_m:
            print("Música encontrada!")
            tocar=str(input("Deseja tocar a música? Digite SIM para tocar e NÃO para não tocar"))
            if tocar == "SIM":
                print("Tocando...")
                lista_hist_musicas.append(nome_m)
            if tocar == "NÃO":
                print("Música não tocada!")        
            return True
       
    print("Música não encontrada!")
    return False

#Função Gerenciar playlist
def gerenciar_musica():
 
    oq_da_playlist=str(input("O que você deseja fazer? Digite 1 para ADICIONAR uma música a playlist, 2 para REMOVER uma música da playlist e 3 para VISUALIZAR a playlist: "))
    if oq_da_playlist == "1":
        nova_m=str(input("Digite o nome da música á ser adionada: "))
        lista_musicas.append(nova_m)
    elif oq_da_playlist == "2":
        del_m=str(input('Digite o nome da música á ser removida: '))
        lista_musicas.remove(del_m)
    elif oq_da_playlist =="3":
            print(lista_musicas)


###############################################################################################################################################################
lista_usuarios = [['Sophia','S','123'],['Bia','B','123']]
lista_musicas = ["CINEMA"]
lista_hist_musicas=[]

print('Bem-Vindo(a) ao SPOTIFEI')

while True:
    nummenu = input('Digite 1 para se CADASTRAR ou 2 para fazer LOGIN: ')
    
    if nummenu == '1':
        print("Vamos realizar seu cadastro!")
        dados_usuario = cadastro()
        lista_usuarios.append(dados_usuario) #Adiciona a lista que foi retornada no cadastro em outra lista (listas dentro de listas )
        print("Agora vamos fazer o login!") #redireciona para o login imediatamente 
        if login():
            escolha=str(input("O que você quer fazer agora? Digite 1 para BUSCAR UMA MÚSICA, 2 para GERENCIAR UMA PLAYLIST e 3 para VISUALIZAR HISTÓRICO \n"))  
            break
        
        
    elif nummenu == '2':
        print('Vamos fazer o login!') 
        if login():
            escolha=str(input("O que você quer fazer agora? Digite 1 para BUSCAR UMA MÚSICA, 2 para GERENCIAR UMA PLAYLIST e 3 para VISUALIZAR HISTÓRICO \n"))  
            break  
        
    else:
        print('Opção inválida. Digite 1 ou 2.')




while True:
    if escolha == "1":
        buscar_musica()
        break

    if escolha =="2":
        gerenciar_musica()
        break
    if escolha =="3":
        print(lista_hist_musicas)
        break  
    else: 
        print('Opção inválida. Digite 1, 2 ou 3.')