
numero = int(input("Digite um número: "))

def soma_digitos(n):
    soma = 0
    while n > 0:
        soma += n % 10 
        n = n // 10  
    return soma


while numero >= 10:
    numero = soma_digitos(numero)  

print(f"resultado é: {numero}")
