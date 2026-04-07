print("="*37)
print(" ")
num1 = float(input("Primeiro numero: "))
num2 = float(input("Segundo numero: "))
print(" ")
print("="*37)
print(" 1 | soma \n 2 | subtração \n 3 | divisao \n 4 | multiplica \n 5 | para sair  ")
print(" ")
opr = int(input("Qual operação vocé deseja fazer: "))
print("="*37)
print(" ")
soma = int()
if opr == 1:
    soma = num1 + num2
    print(f"A soma dos numeros é : {soma}")
    print(" ")
    print("="*37)
elif opr == 2:
    soma = num1 - num2
    print(f"A subtração dos numeros é: {soma}")
    print(" ")
    print("="*37)
elif opr == 3:
    soma = num1 / num2
    print(f"a divisão dos numeros são: {soma}")
    print(" ")
    print("="*37)
elif opr == 4:
    soma = num1 * num2
    print(f"a multiplicação dos numeros é: {soma}") 
    print(" ")
    print("="*37)
elif opr == 5:
    print("obrigado por usar a calculadora")
    print(" ")
    print("="*37)
else:
    print("escolha de operação invalida")
    print(" ")
    print("="*37)

