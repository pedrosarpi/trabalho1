while True:
    print("**************")
    print('    MENU      ')
    print('**************')
    print('1 - Opção 1')
    print('2 - Opção 2')
    print('0 - Sair')
    
    opt=input('Digite uma opção: ')
 
    if opt==('1'):
     print('\nVocê escolheu a opção 1\n')
    elif opt=='2':
     print('\nVocê escolheu a opção 2\n')
    elif opt=='0':
     print('\nVocê escolheu sair\n')
     break
    else:
     print('\nDigite uma opção válida\n')