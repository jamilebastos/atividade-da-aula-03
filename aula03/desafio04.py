
numero = int(input("Digite um número para calcular o fatorial: "))


fatorial = 1

contador = numero

while contador > 0:
    fatorial *= contador
    print(f"{contador}! = {fatorial}")
    contador -= 1
