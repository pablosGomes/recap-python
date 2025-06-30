#exercicio 1

def contar_caracteres(frase):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    total_vogais = 0
    total_consoantes = 0
    total_espacos = 0

    for letra in frase:
        if letra in vogais:
            total_vogais += 1
        elif letra in consoantes:
            total_consoantes += 1
        elif letra == " ":
            total_espacos += 1

    return total_vogais, total_consoantes, total_espacos

frase = input("Digite uma frase: ")

vogais, consoantes, espacos = contar_caracteres(frase)

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
print(f"Espaços: {espacos}")

#exercico 2

def palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

palavra = input("Digite uma palavra ou frase: ")

if palindromo(palavra):
    print("É um palíndromo! 🔁✅")
else:
    print("Não é um palíndromo. ❌")

#exercicio 3

import re

def analisar_texto(texto):
    total_caracteres = len(texto)
    total_caracteres_sem_espaco = len(texto.replace(" ", ""))
    
    palavras = texto.split()
    total_palavras = len(palavras)

    frases = re.split(r'[.!?]+', texto)
    frases = [f for f in frases if f.strip() != '']
    total_frases = len(frases)

    return {
        "caracteres_com_espaco": total_caracteres,
        "caracteres_sem_espaco": total_caracteres_sem_espaco,
        "palavras": total_palavras,
        "frases": total_frases
    }

texto = input("Digite o texto para análise:\n")

estatisticas = analisar_texto(texto)

print("\nEstatísticas do Texto:")
print(f"- Total de caracteres (com espaço): {estatisticas['caracteres_com_espaco']}")
print(f"- Total de caracteres (sem espaço): {estatisticas['caracteres_sem_espaco']}")
print(f"- Total de palavras: {estatisticas['palavras']}")
print(f"- Total de frases: {estatisticas['frases']}")
