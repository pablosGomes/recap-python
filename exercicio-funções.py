#exercicio 1

def fatorial(n):
    if n < 0:
        return 
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(fatorial(5))    
print(primo(13))  
print(primo(12))   

#exercicio 2

import math

def area_quadrado(lado):
    return lado ** 2

def perimetro_quadrado(lado):
    return 4 * lado

def area_circulo(raio):
    return math.pi * raio ** 2

def perimetro_circulo(raio):
    return 2 * math.pi * raio

def area_triangulo(base, altura):
    return (base * altura) / 2

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

print("-- CALCULADORA GEOMÉTRICA --")
print("Escolha a forma geométrica:")
print("1 - Quadrado")
print("2 - Círculo")
print("3 - Triângulo")
opcao = input("Digite o número da opção: ")

if opcao == "1":
    lado = float(input("Digite o lado do quadrado: "))
    print(f"Área: {area_quadrado(lado)}")
    print(f"Perímetro: {perimetro_quadrado(lado)}")

elif opcao == "2":
    raio = float(input("Digite o raio do círculo: "))
    print(f"Área: {area_circulo(raio):.2f}")
    print(f"Perímetro (circunferência): {perimetro_circulo(raio):.2f}")

elif opcao == "3":
    print("Você quer calcular:")
    print("1 - Área (base e altura)")
    print("2 - Perímetro (3 lados)")
    escolha = input("Digite 1 ou 2: ")
    
    if escolha == "1":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        print(f"Área: {area_triangulo(base, altura)}")
    elif escolha == "2":
        l1 = float(input("Lado 1: "))
        l2 = float(input("Lado 2: "))
        l3 = float(input("Lado 3: "))
        print(f"Perímetro: {perimetro_triangulo(l1, l2, l3)}")
    else:
        print("Opção inválida")

else:
    print("Opção inválida")


#exercicio 3 

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [int(x) for x in entrada.split()]

pares = filtrar_pares(numeros)
print("Números pares:", pares)
