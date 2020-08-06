salario= float(input('Qual o salario do funcionário R$'))
aumento= int(input('Quanto voce quer dar de aumeno em %'))
novosalario= (salario + (salario* (aumento/100)))
print('PARABÉNS seu novo salario com {}% de aumento é {}'.format(aumento, novosalario))