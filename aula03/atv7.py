
numero = int(input("Digite um número para a tabuada: "))
multiplo = 3

while multiplo <= 10:
    resultado = numero * multiplo
    if resultado % 3 ==0:
     print (f'{numero} * {multiplo} = {resultado}')
    multiplo += 1