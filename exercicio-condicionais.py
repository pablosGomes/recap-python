#exercicio 1

print("-- CLASSIFICADOR DE IDADE --")

try:
    idade = int(input("Digite sua idade: "))
    
    if idade >= 1 and idade <= 12:
        print("Você é uma criança!")
        
    elif idade >= 13 and idade <= 17:
        print("Você é um adolecente!")
        
    elif idade >= 18 and idade <= 59:
        print("Você é um aduldo!")
        
    elif idade > 60:
        print("Você é um idoso!")
        
except ValueError:
    print("Digite uma idade valida!")
    
#exercicio 2 

print("-- CONVERSOR DE NOTAS --")

try:
    nota = float(input("Digite a nota a ser convertida!"))
    
    if nota >= 0 and nota <= 2:
        print("Sua nota é F")
        
    elif nota >= 3 and nota <= 4:
        print("Sua nota é D")
        
    elif nota >= 5 and nota <= 6:
        print("Sua nota é C")
        
    elif nota >= 7 and nota <= 8:
        print("Sua nota é B")
        
    elif nota >= 9 and nota <= 10:
        print("Sua nota é A")
        
except ValueError:
    print("Digite uma nota valida!")
    
#exercicio 3 

print("-- CAIXA ELETRÔNICO SIMPLES --")

saldo = 1000.00 

while True:
    print(f"\nSaldo disponível: R$ {saldo:.2f}")
    try:
        saque = float(input("Digite o valor do saque (0 para sair): R$ "))

        if saque == 0:
            print("Encerrando operação... Até a próxima!")
            break

        if saque < 0:
            print("Valor negativo não rola, né irmão...")
        elif saque > saldo:
            print("Você não tem saldo suficiente pra isso!")
        else:
            saldo -= saque
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            print(f"Saldo restante: R$ {saldo:.2f}")

    except ValueError:
        print("Digita um valor numérico válido, por favor!")

    