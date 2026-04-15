print(" --- media aluno ---")

media = float(input("Digite a media do aluno: "))

match media:
    case media  if media >= 9.0:
        print(f"Aprovado com Excelencia!(Média: {media})")
    case media if media >= 7.0:
        print(f"Aprovado! (Media: {media})")
    case media if media >= 5.0:
        print(f"Recuperação! (Media: {media})")        
    case _:
        print(f"Reprovado (Media: {media})")
    