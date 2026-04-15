import random

print("="*45)
print(" EXERCICIO - A Playlist do fudencio")


playlist = [
    "Evidências",
    "Garota de Ipanema",
    "Tempo Perdido",
    "Anna Júlia",
    "Mas Que Nada"
]

random.shuffle(playlist)

while True:
    print("="*45)
    print("você deseja remover, adicionar, ver ou sair?")
    escolha = input("Qual sua escolha: ").lower()

    match escolha:
        case "remover":
            remover = input("Qual musica você deseja remover: ")
            if remover in playlist:
                playlist.remove(remover)
            else:
                print("Música não encontrada na playlist")

        case "adicionar":
            adicionar = input("Qual musica você deseja adicionar: ")
            playlist.append(adicionar)

        case "ver":
            print("Sua playlist:")
            for musica in playlist:
                print("-", musica)

        case "sair":
            print("Obrigado por usar a playlist")
            break  

        case _:
            print("Informe uma opção válida")