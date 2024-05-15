import os, funcoes
from funcoes import votos, mais_votado, menos_votado, votantes, media_idade
CS2 = ["CS2", 0,0]; DOTA2= ["DOTA2", 0,0];LOL = ["LOL", 0,0]; VALORANT = ["VALORANT",0,0];MAIOR = [0,0,0,0];MENOR = [0,0,0,0];lista_jogos = [CS2, DOTA2, LOL, VALORANT]
while True:
    os.system("cls")
    voto = votos()
    if voto[0] == 1:
        CS2[1] += 1; CS2[2] += voto[1]; MAIOR[0] += 1
    elif voto[0] == 2:
        DOTA2[1] += 1; DOTA2[2] += voto[1]; MAIOR[1] += 1
    elif voto[0] == 3:
        LOL[1] += 1; LOL[2] += voto[1]; MAIOR[2] += 1
    elif voto[0] == 4:
        VALORANT[1] += 1; VALORANT[2] += voto[1]; MAIOR[3] += 1
    elif voto[0] == 5:
        print("\n")
        for i in lista_jogos:
            print(i)
        #RECEBER O INDICE
        maior = MAIOR.index(max(MAIOR)); mais_pontos = maior; menor = MAIOR.index(min(MAIOR)); menos_pontos = menor
        print(f"\nMais votado: {mais_votado(maior)} com {(lista_jogos[mais_pontos])[1]} pontos\nMenos votado: {menos_votado(menor)} com {(lista_jogos[menos_pontos])[1]} pontos\nTotal de votantes: {votantes(CS2, DOTA2, LOL, VALORANT)}, média de idade {media_idade(CS2, DOTA2, LOL, VALORANT)}\nSaindo do programa...\n\n")
        break