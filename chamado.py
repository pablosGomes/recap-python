chamados = []

def cadastrar_chamado():
    print("Novo chamado Linx (Cliente)")
    servico = input("Informe o serviço com problema (P2K, TEF): ").upper()
    problema = input("Descreva o problema: ")

    chamado = {
        "cliente": "LINX",
        "fornecedor": "ENG",
        "serviço": servico,
        "problema": problema,
        "resolvido": False
    }

    chamados.append(chamado)
    print("Chamado registrado com sucesso!")


def listar_chamados(filtrar_resolvido=False, servico_filtro=None):
    print("Lista de Chamados ENG & LINX:")
    
    chamados_filtrados = [
        (i, c) for i, c in enumerate(chamados)
        if (not filtrar_resolvido or not c["resolvido"])
        and (not servico_filtro or c["serviço"] == servico_filtro)
    ]

    if not chamados_filtrados:
        print("Nenhum chamado encontrado com esse filtro.")
        return

    for i, chamado in chamados_filtrados:
        status = "Resolvido" if chamado["resolvido"] else "Pendente"
        print(f"{i + 1}. [{status}] {chamado['cliente']} ⇄ {chamado['fornecedor']} - Serviço: {chamado['serviço']}")
        print(f"Problema: {chamado['problema']}\n")


def resolver_chamado():
    listar_chamados()

    if not chamados:
        return

    try:
        index = int(input("Digite o número do chamado a resolver: ")) - 1
        if 0 <= index < len(chamados):
            chamados[index]["resolvido"] = True
            print("Chamado marcado como resolvido!\n")
        else:
            print("Número de chamado inválido!\n")
    except ValueError:
        print("Entrada inválida!\n")


def filtrar_por_servico():
    servico = input("Filtrar chamados por serviço (ex: P2K): ").upper()
    listar_chamados(servico_filtro=servico)


def menu():
    while True:
        print("CENTRAL LINX & ENG ")
        print("1. Registrar novo chamado da LINX")
        print("2. Listar todos os chamados")
        print("3. Filtrar chamados por serviço")
        print("4. Resolver chamado")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_chamado()
        elif opcao == 2:
            listar_chamados()
        elif opcao == 3:
            filtrar_por_servico()
        elif opcao == 4:
            resolver_chamado()
        elif opcao == 5:
            print("Encerrando sistema LINX & ENG. Até logo!")
            break
        else:
            print("Opção inválida, tenta de novo!\n")

menu()
