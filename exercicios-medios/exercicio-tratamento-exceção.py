def dividir_numeros():
    try:
        numerador = float(input("Digite o primeiro número: "))
        denominador = float(input("Digite o segundo número: "))

        resultado = numerador / denominador
        print(f"Resultado da divisão: {resultado}")

    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")

    except ValueError:
        print("Erro: entrada inválida. Digite apenas números.")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")

if __name__ == "__main__":
    dividir_numeros()
