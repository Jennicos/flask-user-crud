usuarios = {}

while True:
    print("Opções:")
    print("1- Cadastro")
    print("2- Login")
    opcoes = int(input("Escolha uma opção: "))

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
