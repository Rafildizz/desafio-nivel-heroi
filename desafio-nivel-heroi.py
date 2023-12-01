nomeHerio = (input())
nivelHeroi = int(input())

def fraseFinal(nivel):
    print(f'O Herói de nome {nomeHerio} está no nível de {nivel}')

if nivelHeroi <= 1000:
    fraseFinal('Ferro')
elif 1000 < nivelHeroi <= 2000:
    fraseFinal('Bronze')
elif 2000 < nivelHeroi <= 5000:
    fraseFinal('Prata')
elif 5000 < nivelHeroi <= 7000:
    fraseFinal('Ouro')
elif 7000 < nivelHeroi <= 8000:
    fraseFinal('Platina')
elif 8000 < nivelHeroi <= 9000:
    fraseFinal('Ascendente')
elif 9000 < nivelHeroi <= 10000:
    fraseFinal('Imortal')
elif nivelHeroi > 10000:
    fraseFinal('Radiante')