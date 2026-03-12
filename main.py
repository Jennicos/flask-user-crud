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
            print("\n--- CADASTRO ---")
            novo_usuario = input("Crie um nome de usuario: ")
            if novo_usuario in usuarios:
                print("Este ususario já existe. Tente novamente.")
            else:
                senha = input("Crie uma senha: ")
                usuarios[novo_usuario] = senha 
                print("Cadatro rea lizado com sucesso!")               
        case 2:
            print("\n--- LOGIN ---")
            nome_login = input("Digite seu nome de usuario: ")

            if nome_login not in usuarios:
                print("Este usuario não existe.")
            else:
                senha_login = input("Digite a sua senha: ")

                if senha_login == ususarios[nome_login]:
                    print(f"Login realizado com sucesso! Bem-vindo(a), {nome_login}!")

                else:
                    print("senha incorreta.")             
