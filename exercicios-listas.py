#exercicio 1

print("-- LISTA DE NOMES --")
nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ").strip()
    nomes.append(nome)

print("\nNomes cadastrados:", nomes)

busca = input("\nQual nome você quer procurar? ").strip()

if busca.lower() in (n.lower() for n in nomes):
    print(f"'{busca}' Está na lista!")
else:
    print(f"'{busca}' não foi encontrado. ")
    
#exercicio 2

print("-- LISTA DE 10 NÚMEROS --")
numeros = []

for i in range(10):
    while True:
        try:
            valor = float(input(f"Digite o {i+1}º número: "))
            numeros.append(valor)
            break
        except ValueError:
            print("Isso não é número, Tente de novo.")

maior  = max(numeros)
menor  = min(numeros)
media  = sum(numeros) / len(numeros)

print("\nResultados:")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média: {media:.2f}")

#exercicio 3

print("-- REMOVER DUPLICADOS E ORDENAR --")

# Lê os valores separados por espaço
entrada = input("Digite os elementos da lista, separados por espaço:\n>>> ")

# Quebra a string em lista
lista = entrada.strip().split()

# Remove duplicados com set e ordena com sorted
lista_sem_duplicados = sorted(set(lista))

print("\n Lista sem duplicados e ordenada:")
print(lista_sem_duplicados)


    
