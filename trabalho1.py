
import json
import os

from tkinter.ttk import Notebook

# Tarefa 13: Enumerações

from enum import Enum

class StatusAtivo(Enum):
    ATIVO = 1
    INATIVO = 2
    EM_MANUTENCAO = 3

class NivelCriticidade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4

# Tarefa 14: Persistência de dados

ARQUIVO_VULN = 'vulnerabilidades.json'

def carregar_vulnerabilidades():
    if os.path.exists(ARQUIVO_VULN):
        with open(ARQUIVO_VULN, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_vulnerabilidades(vulnerabilidades):
    with open(ARQUIVO_VULN, 'w', encoding='utf-8') as f:
        json.dump(vulnerabilidades, f, ensure_ascii=False, indent=4)

# Tarefa 09: Funções

def ativos():
  # Tarefa 10: Listas
  ativo = [
    'Notebook', 
    'Roteador', 
    'Servidor', 
    'Impressora', 
    'Software de segurança',
  ]
  # Tarefa 12: Dicionário
  ativos = {
    1: {"Nome": "Notebook",
      "IP": "192.168.10.15",
      "OS": "Windows 11",
      "Criticidade": "Alta"
        },
    2: {"Nome": "Roteador",
      "IP": "10.0.0.1",
      "OS": "Linux",
      "Criticidade": "Média"
        },
    3: {"Nome": "Servidor",
      "IP": "172.16.0.22",
      "OS": "Ubuntu Server",
      "Criticidade": "Crítica"
        },
    4: {"Nome": "Impressora",
      "IP": "192.168.20.30",
      "OS": "Embedded",
      "Criticidade": "Média"
        },
    5: {"Nome": "Software de segurança",
      "IP": "10.10.10.55",
      "OS": "Windows Server",
      "Criticidade": "Alta"}
  }

  # Tarefa 11 = Tuplas e Sets

  categorias = ('Eletrônico', 'Software', 'Hardware')

  vulnerabilidades = carregar_vulnerabilidades()

  # Tarefa 08: Repetição
  while True:
   print(f'\n{"@"* 66}')
   print('\nBem-vindo ao Sistema de Gerenciamento de Ativos e Vulnerabilidades\n')
   print('@'* 66)
   print(f'\n1 - Cadastrar ativo\n2 - Listar ativos\n3 - Remover ativo\n4 - Pesquisar ativo\n5 - Categorias\n6 - Comparar Vulnerabilidades\n7 - Sair\n')

   opt=int(input('\nDigite uma opção: '))

   if opt==1:
    while True:
     nome=input('Digite o nome do ativo: ')
     ativo.append(nome)
     cat_cadastro=input('Digite a categoria do ativo: ')
     if cat_cadastro not in categorias:
       print(f'\nCategoria {cat_cadastro} não encontrada! Informe uma categoria existente\n')
       continue 
     else:
      os=input('Digite o sistema operacional do ativo: ')
      ip=input('Digite o IP do ativo: ')
      print('\nSelecione o Status do ativo: ')
      for status in StatusAtivo:
        print(f'{status.value} - {status.name}')
      status_selecionado = int(input('\nDigite o número correspondente ao status desejado: '))
      if status_selecionado not in [status.value for status in StatusAtivo]:
            print('\nStatus inválido! Informe um status existente\n')
            continue
      else:
        status = StatusAtivo(status_selecionado).name
      print('\nSelecione o Nível de Criticidade do ativo: ')
      for criticidade in NivelCriticidade:
        print(f'{criticidade.value} - {criticidade.name}')
      criticidade_selecionada = int(input('\nDigite o número correspondente ao nível de criticidade desejado: '))
      if criticidade_selecionada not in [criticidade.value for criticidade in NivelCriticidade]:
            print('\nNível de criticidade inválido! Informe um nível existente\n')
            continue
      else:
        criticidade = NivelCriticidade(criticidade_selecionada).name
      ativos[nome] = {
        "IP": ip,
        "OS": os,
        "Status": status,
        "Criticidade": criticidade,
      }
      print(f'\nAtivo {nome} cadastrado com sucesso!\n')
      break

   elif opt==2:
    print('\nAtivos cadastrados:\n')
    for atv in ativo:
      print(atv)

   elif opt==3:
    nome=input('Digite o nome do ativo a ser removido: ').capitalize()
    if nome in ativo:
      ativo.remove(nome)
      print(f'\nAtivo {nome} removido com sucesso!\n')
    else:
      print(f'\nAtivo {nome} não encontrado!\n')

   elif opt==4:
    nome=input('Digite o nome do ativo a ser pesquisado: ').capitalize()
    if nome in ativo:
      print(f'\nAtivo encontrado!\n')
    else:
      print(f'\nAtivo não encontrado!\n')

   elif opt==5:
     
     # Tarefa 11: Tuplas

     print('\nCategorias de ativos:\n')
     for categoria in categorias:
       print(categoria)
     opt_categoria=int(input('\nDigite a opção desejada: \n1 - Desempacotar categorias\n2 - Voltar\n\n'))
     if opt_categoria==1:
       print('\nCategorias desempacotadas:\n')
       cat1, cat2, cat3 = categorias
       print(f'Categoria 1: {cat1}\nCategoria 2: {cat2}\nCategoria 3: {cat3}\n')
      
     elif opt_categoria==2:
       continue
     else:
       print('\nDigite uma opção válida!\n')

   elif opt==6:
     
     # Tarefa 11: Sets
     
     print(f'\nEscolha dois ativos para comparar suas vulnerabilidades:\n')
     vuln1 = input('Digite o nome do primeiro ativo: ')
     vuln2 = input('Digite o nome do segundo ativo: ')

     if vuln1 == vuln2:
       print('\nDigite ativos diferentes!\n')
       continue

     if vuln1 not in vulnerabilidades or vuln2 not in vulnerabilidades:
       print('\nUm ou ambos os ativos não estão cadastrados na base de vulnerabilidades.\n')
       continue

     vulnerabilidades1 = vulnerabilidades[vuln1]
     vulnerabilidades2 = vulnerabilidades[vuln2]

     # Abaixo foi feito o uso de sets para encontrar vulnerabilidades em comum e todas as vulnerabilidades entre os dois ativos
     # como foi proposto no exercício 2 e 3 da tarefa 11.

     print(f'\nVulnerabilidades do {vuln1}: {vulnerabilidades1}\n')
     print(f'Vulnerabilidades do {vuln2}: {vulnerabilidades2}\n')
     print(f'Vulnerabilidades em comum: {vulnerabilidades1.intersection(vulnerabilidades2)}\n')
     print(f'Todas as vulnerabilidades: {vulnerabilidades1.union(vulnerabilidades2)}\n')

   elif opt==7:
     print('\nEspero te ver novamente!!\n')
     break  
   else:
    print('\nDigite uma opção válida!\n')
    
ativos()
  