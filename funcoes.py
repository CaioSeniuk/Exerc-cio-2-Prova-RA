def votos():
    while True:
        voto = int(input("\nEscolha um jogo para votar:\n1- CS2\n2- DOTA 2\n3- LOL\n4- VALORANT\n5- SAIR\n\n--> "))
        if voto <0 or voto >5:
            print("\nErro! insira um valor válido")
            continue
        else:
            if voto == 5:
                idade = 0
                return voto, idade
            else:
                idade = int(input("\nInsira a sua idade: "))
                return voto, idade

def mais_votado(maior):
    if maior == 0:
        return "CS2"
    elif maior == 1:
        return "DOTA 2"
    elif maior == 2:
        return "LOL"
    else:
        return "VALORANT"
    
def menos_votado(menor):
    if menor == 0:
        return "CS2"
    elif menor == 1:
        return "DOTA 2"
    elif menor == 2:
        return "LOL"
    elif menor == 3:
        return "VALORANT"
    
def votantes(CS2, DOTA2, LOL, VALORANT):
    return CS2[1] + DOTA2[1] + LOL[1] + VALORANT[1]

def media_idade(CS2, DOTA2, LOL, VALORANT):
    return ((CS2[2] + DOTA2[2] + LOL[2] + VALORANT[2])/4)