numero = int(input("Digite um número a tabuada: "))


contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
