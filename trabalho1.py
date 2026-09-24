import json
import os
from enum import Enum


class TipoAtivo(Enum):
    EQUIPAMENTO = 1
    SISTEMA = 2
    SERVICO = 3
    DISPOSITIVO_DE_REDE = 4
    BANCO_DE_DADOS = 5


class StatusAtivo(Enum):
    ATIVO = 1
    INATIVO = 2
    EM_MANUTENCAO = 3


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


ARQUIVO_DADOS = 'vulnerabilidades.json'


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return {'ativos': {}, 'vulnerabilidades': {}}
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except (OSError, json.JSONDecodeError):
        print('\nNão foi possível ler o arquivo de dados.\n')
        return {'ativos': {}, 'vulnerabilidades': {}}
    if isinstance(dados, dict) and 'ativos' in dados and 'vulnerabilidades' in dados:
        return dados
    return {'ativos': {}, 'vulnerabilidades': dados if isinstance(dados, dict) else {}}


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def ler_texto(mensagem, obrigatorio=True):
    while True:
        valor = input(mensagem).strip()
        if valor or not obrigatorio:
            return valor
        print('\nEste campo não pode ficar vazio.\n')


def ler_inteiro(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is None or valor >= minimo:
                return valor
        except ValueError:
            pass
        print('\nDigite um número inteiro válido.\n')


def ler_id_ativo():
    while True:
        valor = input('Digite o identificador do ativo (6 algarismos, por exemplo 000000): ').strip()
        if len(valor) == 6 and all('0' <= caractere <= '9' for caractere in valor):
            return valor
        print('\nO identificador deve conter exatamente 6 algarismos numéricos.\n')


def escolher_enum(mensagem, enum_classe):
    print(f'\n{mensagem}')
    for item in enum_classe:
        print(f'{item.value} - {item.name}')
    valores = [item.value for item in enum_classe]
    while True:
        escolha = ler_inteiro('\nDigite o número correspondente: ')
        if escolha in valores:
            return enum_classe(escolha).name
        print('\nOpção inválida.\n')


def cabecalho(titulo):
    print(f'\n{"@" * 66}\n\n{titulo}\n\n{"@" * 66}\n')


def selecionar_ativo(ativos, mensagem):
    if not ativos:
        print('\nNenhum ativo cadastrado.\n')
        return None
    print(f'\n{mensagem}\n')
    ids = list(ativos)
    for indice, ativo_id in enumerate(ids, 1):
        print(f'{indice} - {ativos[ativo_id]["nome"]}')
    opcao = ler_inteiro('\nDigite o número do ativo: ')
    if not 1 <= opcao <= len(ids):
        print('\nOpção de ativo inválida.\n')
        return None
    return ids[opcao - 1]


def cadastrar_ativo(dados):
    ativo_id = ler_id_ativo()
    if ativo_id in dados['ativos']:
        print('\nJá existe um ativo com esse identificador.\n')
        return
    nome = ler_texto('Digite o nome ou hostname do ativo: ')
    if any(a['nome'].casefold() == nome.casefold() for a in dados['ativos'].values()):
        print('\nJá existe um ativo com esse nome ou hostname.\n')
        return
    dados['ativos'][ativo_id] = {
        'nome': nome,
        'responsavel': ler_texto('Digite o responsável: '),
        'setor_localizacao': ler_texto('Digite o setor ou localização: '),
        'tipo': escolher_enum('Selecione o tipo geral do ativo:', TipoAtivo),
        'status': escolher_enum('Selecione o status do ativo:', StatusAtivo),
        'descricao': ler_texto('Digite a descrição do ativo (opcional): ', False),
    }
    dados['vulnerabilidades'].setdefault(ativo_id, [])
    salvar_dados(dados)
    print(f'\nAtivo {nome} cadastrado com sucesso.\n')


def listar_ativos(dados):
    if not dados['ativos']:
        print('\nNenhum ativo cadastrado.\n')
        return
    print('\nAtivos cadastrados:\n')
    for ativo_id, ativo in dados['ativos'].items():
        tipo = ativo.get('tipo', 'NAO_INFORMADO')
        print(f'{ativo_id} - {ativo["nome"]} | Tipo: {tipo} | Status: {ativo["status"]}')


def exibir_ativo(ativo_id, ativo, vulnerabilidades):
    print(f'\nID: {ativo_id}')
    print(f'Nome/hostname: {ativo["nome"]}')
    print(f'Responsável: {ativo["responsavel"]}')
    print(f'Setor/localização: {ativo["setor_localizacao"]}')
    print(f'Tipo: {ativo.get("tipo", "NAO_INFORMADO")}')
    print(f'Status: {ativo["status"]}')
    print(f'Descrição: {ativo["descricao"] or "Não informada"}')
    print(f'Vulnerabilidades: {len(vulnerabilidades.get(str(ativo_id), []))}\n')


def pesquisar_ativo(dados):
    termo = ler_texto('Digite o ID ou nome/hostname do ativo: ')
    resultado = [(chave, ativo) for chave, ativo in dados['ativos'].items()
                 if chave == termo or termo.casefold() in ativo['nome'].casefold()]
    if not resultado:
        print('\nAtivo não encontrado.\n')
    elif len(resultado) > 1:
        print('\nMais de um ativo corresponde à busca:\n')
        for chave, ativo in resultado:
            print(f'{chave} - {ativo["nome"]}')
    else:
        exibir_ativo(resultado[0][0], resultado[0][1], dados['vulnerabilidades'])


def atualizar_ativo(dados):
    ativo_id = selecionar_ativo(dados['ativos'], 'Selecione o ativo para atualizar:')
    if ativo_id is None:
        return
    ativo = dados['ativos'][ativo_id]
    print('\nPressione Enter para manter o valor atual.\n')
    for campo, rotulo in [('nome', 'Nome/hostname'), ('responsavel', 'Responsável'),
                          ('setor_localizacao', 'Setor/localização'), ('descricao', 'Descrição')]:
        novo = input(f'{rotulo} [{ativo[campo]}]: ').strip()
        if novo:
            ativo[campo] = novo
    for campo, classe in [('tipo', TipoAtivo), ('status', StatusAtivo)]:
        valor_atual = ativo.get(campo, 'NAO_INFORMADO')
        if input(f'Alterar {campo} ({valor_atual})? [s/N]: ').strip().casefold() == 's':
            ativo[campo] = escolher_enum(f'Selecione o novo {campo}:', classe)
    salvar_dados(dados)
    print('\nAtivo atualizado com sucesso.\n')


def remover_ativo(dados):
    ativo_id = selecionar_ativo(dados['ativos'], 'Selecione o ativo para remover:')
    if ativo_id is None:
        return
    nome = dados['ativos'][ativo_id]['nome']
    if input(f'Remover {nome} e suas vulnerabilidades? [s/N]: ').strip().casefold() != 's':
        print('\nRemoção cancelada.\n')
        return
    del dados['ativos'][ativo_id]
    dados['vulnerabilidades'].pop(ativo_id, None)
    salvar_dados(dados)
    print(f'\nAtivo {nome} e suas vulnerabilidades foram removidos.\n')


def cadastrar_vulnerabilidade(dados):
    ativo_id = selecionar_ativo(dados['ativos'], 'Selecione o ativo para cadastrar a vulnerabilidade:')
    if ativo_id is None:
        return
    vulnerabilidade = {
        'descricao': ler_texto('Digite a descrição da vulnerabilidade: '),
        'categoria': ler_texto('Digite a categoria ou tipo da vulnerabilidade: '),
        'severidade': escolher_enum('Selecione a severidade:', SeveridadeVulnerabilidade),
        'status': escolher_enum('Selecione o status do tratamento:', StatusTratamento),
    }
    dados['vulnerabilidades'].setdefault(ativo_id, []).append(vulnerabilidade)
    salvar_dados(dados)
    print('\nVulnerabilidade cadastrada com sucesso.\n')


def listar_vulnerabilidades(dados):
    encontradas = False
    print('\nVulnerabilidades cadastradas:\n')
    for ativo_id, lista in dados['vulnerabilidades'].items():
        if not lista:
            continue
        encontradas = True
        nome = dados['ativos'].get(str(ativo_id), {}).get('nome', 'Ativo removido')
        print(f'Ativo {ativo_id} - {nome}')
        for indice, vuln in enumerate(lista, 1):
            print(f'  {indice} - Descrição: {vuln["descricao"]} | Categoria: {vuln["categoria"]} | '
                  f'Severidade: {vuln["severidade"]} | Status: {vuln["status"]}')
    if not encontradas:
        print('Nenhuma vulnerabilidade cadastrada.\n')


def visualizar_vulnerabilidades(dados):
    ativo_id = selecionar_ativo(dados['ativos'], 'Selecione o ativo:')
    if ativo_id is None:
        return
    lista = dados['vulnerabilidades'].get(ativo_id, [])
    if not lista:
        print('\nO ativo está sem vulnerabilidades registradas.\n')
        return
    print(f'\nVulnerabilidades de {dados["ativos"][ativo_id]["nome"]}:\n')
    for indice, vuln in enumerate(lista, 1):
        print(f'{indice} - Descrição: {vuln["descricao"]} | Severidade: {vuln["severidade"]} | Status: {vuln["status"]}')


def alterar_status_vulnerabilidade(dados):
    ativo_id = selecionar_ativo(dados['ativos'], 'Selecione o ativo da vulnerabilidade:')
    if ativo_id is None:
        return
    lista = dados['vulnerabilidades'].get(ativo_id, [])
    if not lista:
        print('\nEsse ativo não possui vulnerabilidades cadastradas.\n')
        return
    for indice, vuln in enumerate(lista, 1):
        print(f'{indice} - {vuln["descricao"]}')
    opcao = ler_inteiro('Digite o número da vulnerabilidade: ')
    if not 1 <= opcao <= len(lista):
        print('\nVulnerabilidade inválida.\n')
        return
    lista[opcao - 1]['status'] = escolher_enum('Selecione o novo status:', StatusTratamento)
    salvar_dados(dados)
    print('\nStatus atualizado com sucesso.\n')


def remover_vulnerabilidade(dados):
    ativo_id = selecionar_ativo(dados['ativos'], 'Selecione o ativo da vulnerabilidade:')
    if ativo_id is None:
        return
    lista = dados['vulnerabilidades'].get(ativo_id, [])
    if not lista:
        print('\nEsse ativo não possui vulnerabilidades cadastradas.\n')
        return
    for indice, vuln in enumerate(lista, 1):
        print(f'{indice} - {vuln["descricao"]}')
    opcao = ler_inteiro('Digite o número da vulnerabilidade para remover: ')
    if not 1 <= opcao <= len(lista):
        print('\nVulnerabilidade inválida.\n')
        return
    lista.pop(opcao - 1)
    salvar_dados(dados)
    print('\nVulnerabilidade removida com sucesso.\n')


def gerenciar_vulnerabilidades(dados):
    while True:
        print('\nGerenciamento de Vulnerabilidades\n1 - Cadastrar vulnerabilidade\n2 - Listar vulnerabilidades\n'
              '3 - Visualizar vulnerabilidades de um ativo\n4 - Alterar status\n5 - Remover vulnerabilidade\n6 - Voltar')
        opcao = ler_inteiro('\nDigite a opção: ')
        if opcao == 1:
            cadastrar_vulnerabilidade(dados)
        elif opcao == 2:
            listar_vulnerabilidades(dados)
        elif opcao == 3:
            visualizar_vulnerabilidades(dados)
        elif opcao == 4:
            alterar_status_vulnerabilidade(dados)
        elif opcao == 5:
            remover_vulnerabilidade(dados)
        elif opcao == 6:
            return
        else:
            print('\nOpção inválida.\n')


def ativos():
    dados = carregar_dados()
    while True:
        cabecalho('Sistema de Gerenciamento de Ativos e Vulnerabilidades')
        print('1 - Cadastrar ativo\n2 - Listar ativos\n3 - Pesquisar ativo por ID ou nome\n'
              '4 - Atualizar ativo\n5 - Remover ativo\n6 - Gerenciar vulnerabilidades\n7 - Sair')
        opcao = ler_inteiro('\nDigite uma opção: ')
        if opcao == 1:
            cadastrar_ativo(dados)
        elif opcao == 2:
            listar_ativos(dados)
        elif opcao == 3:
            pesquisar_ativo(dados)
        elif opcao == 4:
            atualizar_ativo(dados)
        elif opcao == 5:
            remover_ativo(dados)
        elif opcao == 6:
            gerenciar_vulnerabilidades(dados)
        elif opcao == 7:
            print('\nEspero te ver novamente!\n')
            return
        else:
            print('\nDigite uma opção válida!\n')


if __name__ == '__main__':
    ativos()
