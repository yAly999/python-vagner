import webbrowser

print("-"*10 + " crie sua conta " + "-"*10)

nome_usuario = input("Crie seu usuario: ")
senha_correta = input("Crie sua senha: ")  

print("-"*36)

print(" "*36)
print("-"*10 + " entre sua conta " + "-"*10)
tentativa_login = input("coloque seu nome de usuario: ")
tentativa_senha = input("Coloque sua senha: ")

if nome_usuario == tentativa_login and senha_correta == tentativa_senha: 
    print("Bem-vindo!")
    webbrowser.open("https://www.youtube.com/watch?v=m3GGBttKMyw")*10
else:
    print("usuario ou senha incorretas!")