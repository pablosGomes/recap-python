import math

print("-- DISTÂNCIA DE PONTOS ATÉ A ORIGEM --")

coordenadas = []

for i in range(5):
    try:
        x = float(input(f"Digite o valor de x do ponto {i+1}: "))
        y = float(input(f"Digite o valor de y do ponto {i+1}: "))
        coordenadas.append((x, y))
    except ValueError:
        print("Entrada inválida! Digite números reais.")
        exit()
i
print("\nDistâncias até a origem (0,0):")
for i, (x, y) in enumerate(coordenadas, start=1):
    distancia = math.sqrt(x**2 + y**2)
    print(f"Ponto {i} ({x}, {y}) → Distância: {distancia:.2f}")


#exercicio 2

print("-- CADASTRO DE FUNCIONÁRIOS --")

funcionarios = []

for i in range(3):
    print(f"\nFuncionário {i+1}")
    nome = input("Nome: ").strip()
    cargo = input("Cargo: ").strip()
    try:
        salario = float(input("Salário: R$ "))
    except ValueError:
        print("Valor inválido! Salário deve ser um número.")
        exit()

    funcionario = (nome, cargo, salario)
    funcionarios.append(funcionario)

print("\nLISTA DE FUNCIONÁRIOS:\n")
print(f"{'NOME':<20}{'CARGO':<20}{'SALÁRIO (R$)':>15}")
print("-" * 55)

for nome, cargo, salario in funcionarios:
    print(f"{nome:<20}{cargo:<20}{salario:>15.2f}")
