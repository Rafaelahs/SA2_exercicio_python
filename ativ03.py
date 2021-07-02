#3
soma = 0
maior = 0
menor = 0
quant= 0

for i in range(20):
  valor = int(input('Digite um valor: '))
  soma = soma + valor
  quant +=1
  if quant == 1:
      maior=menor=valor
  else:
      if valor>maior:
          maior = valor
      if valor <menor:
          menor = valor
  
  med = soma/20
print('a média é: ', med)
print ('o maior valor é: {} e o menor valor é: {}'.format(maior,menor))
