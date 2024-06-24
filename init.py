# Inicialização das variáveis
prefeito1, prefeito2, prefeito3, prefeito4 = 0, 0, 0, 0
vereador1, vereador2, vereador3, vereador4, vereador5 = 0, 0, 0, 0, 0
vereador6, vereador7, vereador8, vereador9, vereador10 = 0, 0, 0, 0, 0
votos_nulos, votos_brancos = 0, 0
eleitores = 5

# Simulação da votação
while eleitores > 0:
    print("\n-----------------------------------")
    print("Bem-vindo à urna eletrônica!")
    print("Restam", eleitores, "eleitores para votar.")
    print("Digite 00 para fechar a urna.")
    print("-----------------------------------\n")

    compareceu = input("O eleitor compareceu? (s/n): ")
    if compareceu.lower() != "s":
        print("Eleitor não compareceu.")
        eleitores -= 1
        continue

    # Solicita o voto para prefeito
    while True:
        print("\nVotação para prefeito:")
        print(
            "1 - Prefeito 1\n2 - Prefeito 2\n3 - Prefeito 3\n4 - Prefeito 4\n0 - Nulo\n-1 - Branco"
        )
        voto_prefeito = input("Digite o número do seu voto: ")

        # Opção para fechar a urna
        if voto_prefeito == "00":
            fechar_urna = input("Deseja fechar a urna? (s/n): ")
            if fechar_urna.lower() == "s":
                print("A urna foi fechada.")
                exit()
            continue

        confirmar = input(f"Confirma voto em {voto_prefeito}? (s/n): ")
        if confirmar.lower() == "s":
            voto_prefeito = int(voto_prefeito)
            break

    # Contagem dos votos para prefeito
    if voto_prefeito == 1:
        prefeito1 += 1
    elif voto_prefeito == 2:
        prefeito2 += 1
    elif voto_prefeito == 3:
        prefeito3 += 1
    elif voto_prefeito == 4:
        prefeito4 += 1
    elif voto_prefeito == 0:
        votos_nulos += 1
    elif voto_prefeito == -1:
        votos_brancos += 1

    # Solicita o voto para vereador
    while True:
        print("\nVotação para vereador:")
        print(
            "1 - Vereador 1\n2 - Vereador 2\n3 - Vereador 3\n4 - Vereador 4\n5 - Vereador 5"
        )
        print(
            "6 - Vereador 6\n7 - Vereador 7\n8 - Vereador 8\n9 - Vereador 9\n10 - Vereador 10"
        )
        print("0 - Nulo\n-1 - Branco")
        voto_vereador = input("Digite o número do seu voto: ")

        # Opção para fechar a urna
        if voto_vereador == "00":
            fechar_urna = input("Deseja fechar a urna? (s/n): ")
            if fechar_urna.lower() == "s":
                print("A urna foi fechada.")
                exit()
            continue

        confirmar = input(f"Confirma voto em {voto_vereador}? (s/n): ")
        if confirmar.lower() == "s":
            voto_vereador = int(voto_vereador)
            break

    # Contagem dos votos para vereador
    if voto_vereador == 1:
        vereador1 += 1
    elif voto_vereador == 2:
        vereador2 += 1
    elif voto_vereador == 3:
        vereador3 += 1
    elif voto_vereador == 4:
        vereador4 += 1
    elif voto_vereador == 5:
        vereador5 += 1
    elif voto_vereador == 6:
        vereador6 += 1
    elif voto_vereador == 7:
        vereador7 += 1
    elif voto_vereador == 8:
        vereador8 += 1
    elif voto_vereador == 9:
        vereador9 += 1
    elif voto_vereador == 10:
        vereador10 += 1
    elif voto_vereador == 0:
        votos_nulos += 1
    elif voto_vereador == -1:
        votos_brancos += 1

    eleitores -= 1

# Exibição dos resultados
print("\n-----------------------------------")
print("Resultado da eleição:")
print("Prefeito 1: ", prefeito1)
print("Prefeito 2: ", prefeito2)
print("Prefeito 3: ", prefeito3)
print("Prefeito 4: ", prefeito4)
print("\n")
print("Vereador 1: ", vereador1)
print("Vereador 2: ", vereador2)
print("Vereador 3: ", vereador3)
print("Vereador 4: ", vereador4)
print("Vereador 5: ", vereador5)
print("Vereador 6: ", vereador6)
print("Vereador 7: ", vereador7)
print("Vereador 8: ", vereador8)
print("Vereador 9: ", vereador9)
print("Vereador 10: ", vereador10)
print("Votos nulos: ", votos_nulos)
print("Votos brancos: ", votos_brancos)
print("-----------------------------------")
