#variaveis 

nome = "Maria"       # string
idade = 25           # int
altura = 1.68        # float
ativo = True         # bool

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Ativo: {ativo}")

#aritméticos e lógicos

a, b = 10, 3

soma      = a + b     # 13
divisao   = a / b     # 3.333...
modulo    = a % b     # 1  (resto)
comparado = a > b and b < 5  # True

#condicionais

print(soma, divisao, modulo, comparado)

idade = int(input("Idade: "))

if idade >= 18:
    print("Maior de idade 😎")
elif idade >= 16:
    print("Pode votar, mas não dirigir ainda!")
else:
    print("De menor, vai jogar videogame 🎮")
    
#laço de repetição
    
# for simples
for i in range(3):
    print(f"For → {i}")

# while simples
x = 0
while x < 3:
    print(f"While → {x}")
    x += 1
    
#função

def saudacao(nome="Mundo"):
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}!"

print(saudacao("Lucas"))

#litas, tuplas e dicionarios

frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")   # adiciona
frutas.remove("banana")    # remove

for fruta in frutas:
    print(f"Temos {fruta}")

print(frutas)  # ['maçã', 'uva', 'laranja']

cliente = {
    "nome": "Carlos",
    "idade": 30,
    "ativo": True
}

# Acessando e alterando
print(cliente["nome"])
cliente["idade"] += 1
print(cliente)

cores = ("vermelho", "verde", "azul")

print(cores[0])  # vermelho
