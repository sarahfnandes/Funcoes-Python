def autenticar(login, senha):
    usuarios = [
        {"username": "teste", "password": "admin"},
        {"username": "teste2", "password": "admin2"},
        {"username": "teste3", "password": "admin3"},
        {"username": "teste4", "password": "admin4"},
    ]
    for usuario in usuarios:
        if usuario["username"] == login and usuario["password"] == senha:
            return True
    return False

# Teste
login = input("Digite o login: ")
senha = input("Digite a senha: ")
if autenticar(login, senha):
    print("Login bem-sucedido")
else:
    print("Login ou senha incorretos")
