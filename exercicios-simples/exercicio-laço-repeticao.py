#exercicio 1

print("-- TABUADA --")

try:
    numero = int(input("Digite um número inteiro pra ver a tabuada: "))

    print(f"\n Tabuada do {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("Digita um número inteiro válido!")

#exercicio 2

print("-- NÚMEROS DIVISÍVEIS POR 3 E 5 (1 a 100) --\n")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#exercicio 3

import random

print("-- JOGO DE ADIVINHAÇÃO --")
print("Tente adivinhar o número entre 1 e 100!\n")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        chute = int(input("Digite seu palpite: "))
        tentativas += 1

        if chute < 1 or chute > 100:
            print("O número tem que estar entre 1 e 100, animal!")
        elif chute < numero_secreto:
            print("Muito baixo! Tenta um maior.\n")
        elif chute > numero_secreto:
            print("Muito alto! Tenta um menor.\n")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

    except ValueError:
        print("Digita um número inteiro\n")
