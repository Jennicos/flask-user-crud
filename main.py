usuarios = {}

while True:
    print("Opções:")
    print("1- Cadastro")
    print("2- Login")
    
    try:
        opcoes = int(input("Escolha uma opção: "))
    except ValueError:
        print("\n[ERRO] Entrada inválida! Digite apenas os números das opções.")
        continue
    
    match opcoes:
        case 1:
            novo_usuario = input("Crie um nome de usuario: ").strip()

            if novo_usuario in usuarios:
                print("Este usuario já existe. Tente novamente.")
            else:
                senha = input("Crie uma senha: ").strip()
                usuarios[novo_usuario] = senha
                print("Cadastro realizado com sucesso!")
                nome_login = novo_usuario
        case 2:
            nome_login = input("Digite seu nome de usuario: ")
            if nome_login not in usuarios:
                print("Este usuario não existe.")
            else:
                senha_login = input("Digite a sua senha: ")
                if senha_login == usuarios[nome_login]:
                    print(f"Login realizado com sucesso! Bem-vindo(a), {nome_login}!")

                    while True:
                        print(f"\n--- ÁREA DO USUÁRIO ({nome_login}) ---")
                        print("1- Acessar usuários")    
                        print("2- Acessar meu perfil")
                        print("3- Sair")

                        submenu = input("Escolha uma opção: ")

                        match submenu:
                            case "1":
                                while True:
                                    print("\n--- LISTA DE USUÁRIOS ---")
                                    for i, nome in enumerate(usuarios, start=1):
                                        print(f"{i}. {nome}")

                                    print("\n[1] Procurar usuário")
                                    print("[2] Voltar")
                                    escolha_acesso = input("Escolha uma opção: ")

                                    if escolha_acesso == "1":
                                        while True:
                                            busca = input("Digite o nome do usuário: ")
                                            if busca in usuarios:
                                                print(f"Usuário '{busca}' encontrado!")
                                            else:
                                                print(f"Usuário '{busca}' NÃO encontrado.")

                                            print("\n[1] Procurar outro usuário")
                                            print("[2] Voltar")
                                            proxima_acao = input("Escolha uma opção: ")

                                            if proxima_acao == "2":
                                                break
                                    elif escolha_acesso == "2":
                                        break
                            case "2":
                                while True:
                                    print(f"\n--- PERFIL DE {nome_login} ---")
                                    print(f"Nome de usuário: {nome_login}")
                                    print(f"Senha: {senha_login}")
                                    print("\n[1] Apagar perfil")
                                    print("[2] Voltar")

                                    opcoes_perfil = input("Escolha uma opção: ")
                                    
                                    if opcoes_perfil == "1":
                                        senha_confirmacao = input("Digite sua senha: ").strip()
                                        if senha_confirmacao == usuarios[nome_login]:
                                            del usuarios[nome_login]
                                            print("perfil deletado com sucesso.")
                                            break
                                        else:
                                            print("Senha incorreta.")
                                    elif opcoes_perfil == "2":
                                        break
                            case "3":
                                    print("Saindo...")
                                    break
                    else:
                        print("Senha incorreta.")
