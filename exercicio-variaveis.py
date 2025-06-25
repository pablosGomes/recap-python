# 1 - Declarar variáveis de diferentes tipos e mostrar seus valores e tipos

nome = "Lucas"            # string
idade = 20                # int
altura = 1.75             # float
ativo = True              # bool

print(f"nome: {nome} → tipo: {type(nome)}")
print(f"idade: {idade} → tipo: {type(idade)}")
print(f"altura: {altura} → tipo: {type(altura)}")
print(f"ativo: {ativo} → tipo: {type(ativo)}")

# 2 - Recebe nome, idade e altura, e mostra frase formatada

nome1 = input("Digite seu nome: ")
idade1 = input("Digite sua idade: ")
altura1 = input("Digite sua altura (em metros): ")

print(f"{nome1} tem {idade1} anos e mede {altura1}m de altura.")


# 3 - Conversor entre Celsius e Fahrenheit

print("Conversor de Temperatura")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
opcao = input("Escolha a opção (1 ou 2): ")

valor = float(input("Digite o valor da temperatura: "))

if opcao == "1":
    resultado = (valor * 9/5) + 32
    print(f"{valor}°C = {resultado:.2f}°F")
elif opcao == "2":
    resultado = (valor - 32) * 5/9
    print(f"{valor}°F = {resultado:.2f}°C")
else:
    print("Opção inválida")

