def classificar_risco():

  grau=int(input('Grau de vulnerabilidade: '))

  print('\n---CLASSIFICAÇÃO---\n')

  if grau >= 9:
    print ('Risco crítico')
  elif grau >= 7:
    print ('Risco alto')
  elif grau >= 4:
    print ('Risco médio')
  else:
    print ('Risco baixo')

ativo=input('Nome da vulnerabilidade: ')

if ativo == ('notebook'):
  classificar_risco()
else:
  print('Ativo não encontrado.')