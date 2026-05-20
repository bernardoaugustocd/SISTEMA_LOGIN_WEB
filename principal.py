import webbrowser

print("Sistema de login web")
usuario_valido = "Bernardo"
senha_valida = "1234"
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_valido and senha == senha_valida:
    print("Login realizado com sucesso!")
    webbrowser.open("https://www.mg.senac.br")
    
else:
    print("Usuário ou senha incorretos, tente novamente.")