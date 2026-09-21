ativos = {}


def cadastrar_ativo():
    nome = input("Digite o nome do ativo: ").strip()
    if not nome:
        print("O nome do ativo não pode ficar vazio.")
        return

    if nome in ativos:
        print(f"O ativo '{nome}' já está cadastrado.")
        return

    ip = input("Digite o IP do ativo: ").strip()
    os = input("Digite o sistema operacional: ").strip()
    criticidade = input("Digite a criticidade: ").strip()

    ativos[nome] = {
        "IP": ip,
        "OS": os,
        "Criticidade": criticidade,
        "Vulnerabilidades": []
    }

    print(f"Ativo '{nome}' cadastrado com sucesso!")


def listar_ativos():
    if not ativos:
        print("Nenhum ativo cadastrado.")
        return

    print("\n--- ATIVOS CADASTRADOS ---")
    for nome, dados in ativos.items():
        print(f"\nNome: {nome}")
        print(f"IP: {dados['IP']}")
        print(f"OS: {dados['OS']}")
        print(f"Criticidade: {dados['Criticidade']}")
        print(f"Vulnerabilidades: {dados['Vulnerabilidades'] if dados['Vulnerabilidades'] else 'Nenhuma'}")


def atribuir_vulnerabilidade():
    nome = input("Digite o nome do ativo: ").strip()
    if nome not in ativos:
        print(f"Ativo '{nome}' não encontrado.")
        return

    vulnerabilidade = input("Digite a vulnerabilidade a ser atribuída: ").strip()
    if not vulnerabilidade:
        print("A vulnerabilidade não pode ficar vazia.")
        return

    ativos[nome]["Vulnerabilidades"].append(vulnerabilidade)
    print(f"Vulnerabilidade atribuída ao ativo '{nome}'!")


def atualizar_vulnerabilidade():
    nome = input("Digite o nome do ativo: ").strip()
    if nome not in ativos:
        print(f"Ativo '{nome}' não encontrado.")
        return

    lista = ativos[nome]["Vulnerabilidades"]
    if not lista:
        print(f"O ativo '{nome}' ainda não possui vulnerabilidades.")
        return

    print(f"\nVulnerabilidades de '{nome}':")
    for i, vulnerabilidade in enumerate(lista, start=1):
        print(f"{i} - {vulnerabilidade}")

    try:
        indice = int(input("Digite o número da vulnerabilidade que deseja atualizar: ")) - 1
    except ValueError:
        print("Digite um número válido.")
        return

    if indice < 0 or indice >= len(lista):
        print("Número inválido.")
        return

    nova_vulnerabilidade = input("Digite a nova vulnerabilidade: ").strip()
    if not nova_vulnerabilidade:
        print("A nova vulnerabilidade não pode ficar vazia.")
        return

    lista[indice] = nova_vulnerabilidade
    print("Vulnerabilidade atualizada com sucesso!")


while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar ativo")
    print("2 - Listar ativos")
    print("3 - Atribuir vulnerabilidade")
    print("4 - Atualizar vulnerabilidade")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_ativo()
    elif opcao == "2":
        listar_ativos()
    elif opcao == "3":
        atribuir_vulnerabilidade()
    elif opcao == "4":
        atualizar_vulnerabilidade()
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
