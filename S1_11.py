
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
    "Notebook": {
      "IP": "192.168.10.15",
      "OS": "Windows 11",
      "Criticidade": "Alta"
        },
    "Roteador": {
      "IP": "10.0.0.1",
      "OS": "Linux",
      "Criticidade": "Média"
        },
    "Servidor": {
      "IP": "172.16.0.22",
      "OS": "Ubuntu Server",
      "Criticidade": "Crítica"
        },
    "Impressora": {
      "IP": "192.168.20.30",
      "OS": "Embedded",
      "Criticidade": "Média"
        },
    "Software de segurança": {
      "IP": "10.10.10.55",
      "OS": "Windows Server",
      "Criticidade": "Alta"}
  }

  # Tarefa 11 = Tuplas e Sets

  categorias = ('Eletrônico', 'Software', 'Hardware')

  vuln_notebook = {'Sistema operacional desatualizado', 'Antivírus desativado', 'Senha fraca'}
  vuln_roteador = {'Firmware desatualizado', 'Senha padrão', 'Portas abertas'}
  vuln_servidor = {'Sistema operacional desatualizado', 'Serviços desnecessários', 'Falta de backup'}
  vuln_impressora = {'Firmware desatualizado', 'Senha padrão', 'Portas abertas'}  
  vuln_software = {'Vulnerabilidade de segurança conhecida', 'Falta de atualização', 'Configuração insegura'}

  # Dicionário para mapear ativos às suas vulnerabilidades

  vulnerabilidades = {
    'Notebook': vuln_notebook,
    'Roteador': vuln_roteador,
    'Servidor': vuln_servidor,
    'Impressora': vuln_impressora,
    'Software de segurança': vuln_software,
  }

  # Tarefa 08: Repetição
  while True:
   print('\n---ATIVOS---\n')
   print(f'1 - Cadastrar ativo\n2 - Listar ativos\n3 - Remover ativo\n4 - Pesquisar ativo\n5 - Categorias\n6 - Comparar Vulnerabilidades\n7 - Sair\n')

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
      criticidade=input('Digite a criticidade do ativo (Baixa, Média, Alta, Crítica): ')
      ativos[nome] = {
        "IP": ip,
        "OS": os,
        "Criticidade": criticidade
      }
      print(f'\nAtivo {nome} cadastrado com sucesso!\n')
      break

   elif opt==2:
    print('\nAtivos cadastrados:\n')
    for atv in ativo:
      print(atv)

   elif opt==3:
    nome=input('Digite o nome do ativo a ser removido: ')
    if nome in ativo:
      ativo.remove(nome)
      print(f'\nAtivo {nome} removido com sucesso!\n')
    else:
      print(f'\nAtivo {nome} não encontrado!\n')

   elif opt==4:
    nome=input('Digite o nome do ativo a ser pesquisado: ')
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
  