def perguntar():
    return input("MENU:\n" +
            "<I> - Para Inserir um usuário\n"+
            "<P> - Para Pesquisar um usuário\n"+
            "<E> - Para Excluir um usuário\n"+
            "<L> - Para Listar um usuário\n"+
            "<S> - Para Sair do menu\n"+
            "O que deseja realizar? ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a última data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]

def procurar(dicionario):
    print("\nSegue abaixo os dados do usuário solicitado:\n", dicionario.get(input("Digite o login: ").upper()), "\n")