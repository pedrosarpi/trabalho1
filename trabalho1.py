import json
import os
from enum import Enum


# Tarefa 13: Enumerações
class StatusAtivo(Enum):
    ATIVO = 1
    INATIVO = 2
    EM_MANUTENCAO = 3


class NivelCriticidade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4


class SeveridadeVulnerabilidade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4


class StatusTratamento(Enum):
    ABERTA = 1
    EM_TRATAMENTO = 2
    CORRIGIDA = 3
    ACEITA_COMO_RISCO = 4


# Tarefa 14: Persistência de dados
ARQUIVO_VULN = 'vulnerabilidades.json'


def carregar_vulnerabilidades():
    if os.path.exists(ARQUIVO_VULN):
        with open(ARQUIVO_VULN, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            if isinstance(dados, dict):
                return dados
    return {}


def salvar_vulnerabilidades(vulnerabilidades):
    with open(ARQUIVO_VULN, 'w', encoding='utf-8') as arquivo:
        json.dump(vulnerabilidades, arquivo, ensure_ascii=False, indent=4)


def mostrar_cabecalho(titulo):
    print(f'\n{"@" * 66}')
    print(f'\n{titulo}\n')
    print('@' * 66)


def mostrar_status_ativo():
    print('\nSelecione o Status do ativo: ')
    for status in StatusAtivo:
        print(f'{status.value} - {status.name}')


def mostrar_criticidade():
    print('\nSelecione o Nível de Criticidade do ativo: ')
    for criticidade in NivelCriticidade:
        print(f'{criticidade.value} - {criticidade.name}')


def mostrar_severidades():
    print('\nSelecione a severidade da vulnerabilidade:\n')
    for severidade in SeveridadeVulnerabilidade:
        print(f'{severidade.value} - {severidade.name}')


def mostrar_status_tratamento():
    print('\nSelecione o status do tratamento da vulnerabilidade:\n')
    for status in StatusTratamento:
        print(f'{status.value} - {status.name}')


def listar_vulnerabilidades(vulnerabilidades):
    if not vulnerabilidades:
        print('\nNenhuma vulnerabilidade cadastrada.\n')
        return

    print('\nVulnerabilidades cadastradas:\n')
    for nome_ativo, lista in vulnerabilidades.items():
        if not lista:
            continue
        print(f'Ativo: {nome_ativo}')
        for indice, vulnerabilidade in enumerate(lista, start=1):
            print(
                f"  {indice} - Descrição: {vulnerabilidade['descricao']} | "
                f"Categoria: {vulnerabilidade['categoria']} | "
                f"Severidade: {vulnerabilidade['severidade']} | "
                f"Status: {vulnerabilidade['status']}"
            )


def cadastrar_vulnerabilidade(vulnerabilidades, ativos):
    if not ativos:
        print('\nCadastre um ativo antes de cadastrar vulnerabilidades.\n')
        return

    nomes_ativos = list(ativos.keys())
    print('\nSelecione o ativo para cadastrar a vulnerabilidade:\n')
    for indice, nome in enumerate(nomes_ativos, start=1):
        print(f'{indice} - {nome}')

    try:
        opcao_ativo = int(input('\nDigite o número do ativo: '))
        nome_ativo = nomes_ativos[opcao_ativo - 1]
    except (ValueError, IndexError):
        print('\nOpção de ativo inválida.\n')
        return

    descricao = input('Digite a descrição da vulnerabilidade: ').strip()
    categoria = input('Digite a categoria ou tipo da vulnerabilidade: ').strip()

    mostrar_severidades()
    severidade_digitada = int(input('\nDigite o número correspondente: '))
    if severidade_digitada not in [s.value for s in SeveridadeVulnerabilidade]:
        print('\nSeveridade inválida.\n')
        return
    severidade = SeveridadeVulnerabilidade(severidade_digitada).name

    mostrar_status_tratamento()
    status_digitado = int(input('\nDigite o número correspondente: '))
    if status_digitado not in [s.value for s in StatusTratamento]:
        print('\nStatus de tratamento inválido.\n')
        return
    status = StatusTratamento(status_digitado).name

    vulnerabilidades.setdefault(nome_ativo, [])
    vulnerabilidades[nome_ativo].append({
        'descricao': descricao,
        'categoria': categoria,
        'severidade': severidade,
        'status': status,
    })

    salvar_vulnerabilidades(vulnerabilidades)
    print(f'\nVulnerabilidade cadastrada com sucesso para o ativo {nome_ativo}.\n')


def comparar_vulnerabilidades(vulnerabilidades, ativos):
    if not ativos:
        print('\nNenhum ativo cadastrado.\n')
        return

    nomes_ativos = list(ativos.keys())
    print('\nEscolha dois ativos para comparar:\n')
    for indice, nome in enumerate(nomes_ativos, start=1):
        print(f'{indice} - {nome}')

    try:
        ativo1 = nomes_ativos[int(input('Digite o número do primeiro ativo: ')) - 1]
        ativo2 = nomes_ativos[int(input('Digite o número do segundo ativo: ')) - 1]
    except (ValueError, IndexError):
        print('\nAtivo inválido.\n')
        return

    if ativo1 == ativo2:
        print('\nEscolha ativos diferentes.\n')
        return

    if ativo1 not in vulnerabilidades:
        vulnerabilidades[ativo1] = []
    if ativo2 not in vulnerabilidades:
        vulnerabilidades[ativo2] = []

    descricoes_1 = {v['descricao'] for v in vulnerabilidades[ativo1]}
    descricoes_2 = {v['descricao'] for v in vulnerabilidades[ativo2]}

    print(f'\nVulnerabilidades do {ativo1}: {descricoes_1}\n')
    print(f'Vulnerabilidades do {ativo2}: {descricoes_2}\n')
    print(f'Vulnerabilidades em comum: {descricoes_1.intersection(descricoes_2)}\n')
    print(f'Todas as vulnerabilidades: {descricoes_1.union(descricoes_2)}\n')


def alterar_status_vulnerabilidade(vulnerabilidades):
    if not vulnerabilidades:
        print('\nNenhuma vulnerabilidade cadastrada para alterar.\n')
        return

    print('\nSelecione o ativo da vulnerabilidade:\n')
    nomes_ativos = list(vulnerabilidades.keys())
    for indice, nome in enumerate(nomes_ativos, start=1):
        print(f'{indice} - {nome}')

    try:
        opcao_ativo = int(input('\nDigite o número do ativo: '))
        nome_ativo = nomes_ativos[opcao_ativo - 1]
    except (ValueError, IndexError):
        print('\nAtivo inválido.\n')
        return

    if not vulnerabilidades[nome_ativo]:
        print(f'\nO ativo {nome_ativo} não possui vulnerabilidades cadastradas.\n')
        return

    print(f'\nVulnerabilidades de {nome_ativo}:')
    for indice, vulnerabilidade in enumerate(vulnerabilidades[nome_ativo], start=1):
        print(f'{indice} - {vulnerabilidade["descricao"]}')

    try:
        opcao_vuln = int(input('\nDigite o número da vulnerabilidade para alterar o status: '))
        vulnerabilidade = vulnerabilidades[nome_ativo][opcao_vuln - 1]
    except (ValueError, IndexError):
        print('\nVulnerabilidade inválida.\n')
        return

    mostrar_status_tratamento()
    novo_status = int(input('\nDigite o número do novo status: '))
    if novo_status not in [s.value for s in StatusTratamento]:
        print('\nStatus inválido.\n')
        return

    vulnerabilidade['status'] = StatusTratamento(novo_status).name
    salvar_vulnerabilidades(vulnerabilidades)
    print(f'\nStatus da vulnerabilidade atualizado para {vulnerabilidade["status"]}.\n')


def gerenciar_vulnerabilidades(vulnerabilidades, ativos):
    while True:
        print('\nGerenciamento de Vulnerabilidades\n')
        print('1 - Cadastrar vulnerabilidade')
        print('2 - Listar vulnerabilidades')
        print('3 - Comparar vulnerabilidades')
        print('4 - Alterar status da vulnerabilidade')
        print('5 - Voltar')

        try:
            opcao = int(input('\nDigite a opção: '))
        except ValueError:
            print('\nOpção inválida!\n')
            continue

        if opcao == 1:
            cadastrar_vulnerabilidade(vulnerabilidades, ativos)
        elif opcao == 2:
            listar_vulnerabilidades(vulnerabilidades)
        elif opcao == 3:
            comparar_vulnerabilidades(vulnerabilidades, ativos)
        elif opcao == 4:
            alterar_status_vulnerabilidade(vulnerabilidades)
        elif opcao == 5:
            break
        else:
            print('\nOpção inválida!\n')


# Tarefa 09: Funções
def ativos():
    ativos = {
        'Notebook': {'IP': '192.168.10.15', 'OS': 'Windows 11', 'Status': 'ATIVO', 'Criticidade': 'ALTA'},
        'Roteador': {'IP': '10.0.0.1', 'OS': 'Linux', 'Status': 'ATIVO', 'Criticidade': 'MEDIA'},
        'Servidor': {'IP': '172.16.0.22', 'OS': 'Ubuntu Server', 'Status': 'ATIVO', 'Criticidade': 'CRITICA'},
        'Impressora': {'IP': '192.168.20.30', 'OS': 'Embedded', 'Status': 'ATIVO', 'Criticidade': 'MEDIA'},
        'Software de segurança': {'IP': '10.10.10.55', 'OS': 'Windows Server', 'Status': 'ATIVO', 'Criticidade': 'ALTA'},
    }

    categorias = ('Eletrônico', 'Software', 'Hardware')
    vulnerabilidades = carregar_vulnerabilidades()

    while True:
        mostrar_cabecalho('Bem-vindo ao Sistema de Gerenciamento de Ativos e Vulnerabilidades')
        print('1 - Cadastrar ativo')
        print('2 - Listar ativos')
        print('3 - Remover ativo')
        print('4 - Pesquisar ativo')
        print('5 - Categorias')
        print('6 - Gerenciar vulnerabilidades')
        print('7 - Sair')

        try:
            opcao = int(input('\nDigite uma opção: '))
        except ValueError:
            print('\nDigite uma opção válida!\n')
            continue

        if opcao == 1:
            while True:
                nome = input('Digite o nome do ativo: ').strip()
                if not nome:
                    print('\nNome do ativo não pode ficar vazio.\n')
                    continue
                if nome in ativos:
                    print(f'\nO ativo {nome} já existe.\n')
                    break

                categoria = input('Digite a categoria do ativo: ').strip()
                if categoria not in categorias:
                    print(f'\nCategoria {categoria} não encontrada! Informe uma categoria existente\n')
                    continue

                sistema_operacional = input('Digite o sistema operacional do ativo: ').strip()
                ip = input('Digite o IP do ativo: ').strip()

                mostrar_status_ativo()
                status_selecionado = int(input('\nDigite o número correspondente ao status desejado: '))
                if status_selecionado not in [status.value for status in StatusAtivo]:
                    print('\nStatus inválido! Informe um status existente\n')
                    continue
                status = StatusAtivo(status_selecionado).name

                mostrar_criticidade()
                criticidade_selecionada = int(input('\nDigite o número correspondente ao nível de criticidade desejado: '))
                if criticidade_selecionada not in [criticidade.value for criticidade in NivelCriticidade]:
                    print('\nNível de criticidade inválido! Informe um nível existente\n')
                    continue
                criticidade = NivelCriticidade(criticidade_selecionada).name

                ativos[nome] = {
                    'IP': ip,
                    'OS': sistema_operacional,
                    'Status': status,
                    'Criticidade': criticidade,
                }
                vulnerabilidades.setdefault(nome, [])
                salvar_vulnerabilidades(vulnerabilidades)
                print(f'\nAtivo {nome} cadastrado com sucesso!\n')
                break

        elif opcao == 2:
            print('\nAtivos cadastrados:\n')
            for nome in ativos:
                print(nome)

        elif opcao == 3:
            nome = input('Digite o nome do ativo a ser removido: ').strip().capitalize()
            if nome in ativos:
                del ativos[nome]
                if nome in vulnerabilidades:
                    del vulnerabilidades[nome]
                salvar_vulnerabilidades(vulnerabilidades)
                print(f'\nAtivo {nome} removido com sucesso!\n')
            else:
                print(f'\nAtivo {nome} não encontrado!\n')

        elif opcao == 4:
            nome = input('Digite o nome do ativo a ser pesquisado: ').strip().capitalize()
            if nome in ativos:
                print(f'\nAtivo encontrado!\n')
                print(ativos[nome])
            else:
                print(f'\nAtivo não encontrado!\n')

        elif opcao == 5:
            print('\nCategorias de ativos:\n')
            for categoria in categorias:
                print(categoria)

            opcao_categoria = int(input('\nDigite a opção desejada: \n1 - Desempacotar categorias\n2 - Voltar\n\n'))
            if opcao_categoria == 1:
                print('\nCategorias desempacotadas:\n')
                cat1, cat2, cat3 = categorias
                print(f'Categoria 1: {cat1}\nCategoria 2: {cat2}\nCategoria 3: {cat3}\n')
            elif opcao_categoria != 2:
                print('\nDigite uma opção válida!\n')

        elif opcao == 6:
            gerenciar_vulnerabilidades(vulnerabilidades, ativos)

        elif opcao == 7:
            print('\nEspero te ver novamente!!\n')
            break

        else:
            print('\nDigite uma opção válida!\n')


if __name__ == '__main__':
    ativos()
