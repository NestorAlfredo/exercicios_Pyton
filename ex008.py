m= float(input('Digite uma distância em metros'))
cm = float(m*100)
mm = float(m*1000)
km = float(m/1000)
print('A medida {} em metros corresponde a {:.0f}cm e a {:.0f}mm'
      ' e a {}km'.format(m, cm, mm, km))
