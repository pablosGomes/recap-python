def salvar_usuario(nome, idade, email):
    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}, Idade: {idade}, Email: {email}\n")

def ler_usuarios():
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("\nDados salvos:")
            print(conteudo)
    except FileNotFoundError:
        print("esse arquivo ainda não existe!")

print("-- Cadastro de Usuário --")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
email = input("Digite seu email: \n")

salvar_usuario(nome, idade, email)

ler_usuarios()
