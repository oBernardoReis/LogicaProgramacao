usuario_correto = "admin"
senha_correta = "1234"

tentativas = 3

for tentativa in range(1, tentativas + 1):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo ao sistema!")
        break
    else:
        restantes = tentativas - tentativa
        if restantes > 0:
            print(f"Credenciais incorretas. Tentativas restantes: {restantes}")
        else:
            for _ in range(3):
                print("Acesso bloqueado")
