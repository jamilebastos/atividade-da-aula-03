notas = 0
soma = 0

nota = float (input("Digite sua nota e pressione -1 para obter resultado:"))
while nota > 0:
    notas = notas +1
    soma = soma + nota
    nota = float (input("Digite sua nota e pressione -1 para obter resultado:"))
print (f"resultado soma : {soma}")
media = soma/notas
print (f" o resultado é :{media}")