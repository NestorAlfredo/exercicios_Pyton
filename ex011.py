l=float(input('Qual a largura da sua parede em m '))
h=float(input('Qual a altura da sua parede em m '))
area= l*h
print('Sua parede tem a dimensão de {} x {}, e a área é de {}m'.format(l, h, area))
print('Você vai gastar {}l de tinta para pintar a parede'.format(area/2))
