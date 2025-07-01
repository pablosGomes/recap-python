import csv
from collections import defaultdict

def calcular_total_vendas_por_produto(arquivo_csv):
    totais = defaultdict(int)

    with open(arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            produto = linha["produto"]
            quantidade = int(linha["quantidade"])
            totais[produto] += quantidade

    return totais

arquivo = "vendas.csv"

vendas = calcular_total_vendas_por_produto(arquivo)
print("\nTotal de Vendas por Produto:")
for produto, total in vendas.items():
    print(f"- {produto}: {total} unidades")
