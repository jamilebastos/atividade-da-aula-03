
numero = int(input("Digite um número para iniciar a sequência de Collatz: "))

while numero != 1:
    print(numero, end=" -> ")
    if numero % 2 == 0:
        numero //= 2 
    else:
        numero = 3 * numero + 1  


print(1)
