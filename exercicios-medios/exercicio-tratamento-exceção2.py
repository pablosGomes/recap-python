import re

ARQUIVO_SAIDA = "cadastros.txt"

EMAIL_RE   = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
TELEFONE_RE = re.compile(r"^\+?\d{8,15}$")   


def obter_nome() -> str:
    nome = input("Nome completo: ").strip()
    if not nome:
        raise ValueError("Nome não pode ficar em branco.")
    return nome


def obter_idade() -> int:
    idade_str = input("Idade: ").strip()
    if not idade_str.isdigit():
        raise ValueError("Idade deve conter apenas dígitos.")
    idade = int(idade_str)
    if idade <= 0 or idade > 120:
        raise ValueError("Idade deve estar entre 1 e 120 anos.")
    return idade


def obter_email() -> str:
    email = input("E‑mail: ").strip()
    if not EMAIL_RE.fullmatch(email):
        raise ValueError("Formato de e‑mail inválido.")
    return email


def obter_telefone() -> str:
    telefone = input("Telefone (somente dígitos, opcional '+'): ").strip()
    telefone_normalizado = re.sub(r"[^\d+]", "", telefone)
    if not TELEFONE_RE.fullmatch(telefone_normalizado):
        raise ValueError("Telefone deve ter de 8 a 15 dígitos; use apenas números e, opcionalmente, '+'.")
    return telefone_normalizado


def salvar_cadastro(nome: str, idade: int, email: str, telefone: str) -> None:
    with open(ARQUIVO_SAIDA, mode="a", encoding="utf-8") as arq:
        arq.write(f"{nome};{idade};{email};{telefone}\n")


def main() -> None:
    print("=== Cadastro de Usuário ===")
    try:
        nome      = obter_nome()
        idade     = obter_idade()
        email     = obter_email()
        telefone  = obter_telefone()
    except ValueError as erro:
        print(f"Erro: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    else:
        salvar_cadastro(nome, idade, email, telefone)
        print("Cadastro realizado com sucesso.")


if __name__ == "__main__":
    main()
