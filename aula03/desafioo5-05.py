import random


numero_secreto = random.randint(1, 100)

palpite = None

print("Bem-vindo ao jogo de adivinhação!")
print("Eu escolhi um número entre 1 e 100. Tente adivinhar qual é!")


while palpite != numero_secreto:
    palpite = int(input("Digite o seu palpite: "))
    
    
    if palpite < numero_secreto:
        print("O seu palpite é muito baixo! Tente um número maior.")
    elif palpite > numero_secreto:
        print("O seu palpite é muito alto! Tente um número menor.")
    
print(f"Parabéns! Você acertou! O número era {numero_secreto}.")
