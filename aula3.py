import webbrowser


nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))

if idade >= 18:
    webbrowser.open("https://www.youtube.com/watch?v=qxWqt4R8y6A")
elif idade < 18:
    webbrowser.open("https://www.youtube.com/watch?v=mHJ3l18YqNM")    
else:
    print("sla")

