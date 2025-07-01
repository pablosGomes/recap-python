#exercicio 1
print("-- CALCULADORA --")

while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite um numero!\n")
        continue

    print("""
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[0] Sair
""")
    try:
        operacao = int(input("Escolha a operação: "))
    except ValueError:
        print("Tem que ser um número de 0 a 4!\n")
        continue

    if operacao == 0:
        print("Até logo")
        break
    elif operacao == 1:
        print("Resultado:", numero1 + numero2, "\n")
    elif operacao == 2:
        print("Resultado:", numero1 - numero2, "\n")
    elif operacao == 3:
        print("Resultado:", numero1 * numero2, "\n")
    elif operacao == 4:
        if numero2 == 0:
            print("Divisão por zero , parça!\n")
        else:
            print("Resultado:", numero1 / numero2, "\n")
    else:
        print(" Opção inválida, tenta de novo.\n")

#exercicio 2

print("-- CÁLCULO DE RETÂNGULO --")

try:
    base = float(input("Digite a base do retângulo (em cm): "))
    altura = float(input("Digite a altura do retângulo (em cm): "))

    area = base * altura
    perimetro = 2 * (base + altura)

    print(f"\nÁrea: {area} cm²")
    print(f"Perímetro: {perimetro} cm")

except ValueError:
    print("Digita um número!")

#exercicio 3 

print("-- VERIFICADOR DE PAR OU ÍMPAR --")

try:
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print(f"O número {numero} é PAR ")
    else:
        print(f"O número {numero} é ÍMPAR ")

except ValueError:
    print("Você precisa digitar um número inteiro!")
