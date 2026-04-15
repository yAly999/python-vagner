while True:

    print("=== menu ===\n você deseja: salvar, carregar ou sair?")
    comando = input("Qual sua escolha: ")

    match comando:
        case "salvar":
            print("Salvando seu jogo!")
            break
        case "carregar":
            print("Carregando seu jogo")
            break
        case "sair":
            print("Saindo do jogo...")  
            break 
        case _:
            print("comando invalido")
            




    
    
        

    
                              