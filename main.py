# Solicitar informações do usuário
nome_completo = input("Digite seu nome completo: ")
email = input("Digite seu email: ")
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Armazenar as informações em um dicionário
dados_usuario = {
    "Nome Completo": nome_completo,
    "Email": email,
    "Data de Nascimento": data_nascimento
}

# Exibir os dados armazenados
print("\nDados cadastrados:")
print("Nome Completo:", dados_usuario["Nome Completo"])
print("Email:", dados_usuario["Email"])
print("Data de Nascimento:", dados_usuario["Data de Nascimento"])
