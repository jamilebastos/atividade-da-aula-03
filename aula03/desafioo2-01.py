
numero1 = int(input("Digite o primeiro número do intervalo: "))
numero2 = int(input("Digite o segundo número do intervalo: "))

if numero1 % 2 != 0:
    numero1 += 1

while numero1 <= numero2:
    print(numero1)
    numero1+= 2 
