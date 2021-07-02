#1a)
l = [5,7,2,9,4,1,3]
print ('O tamanho da lista é: ' , len(l))


#1b)
primeiro = 5
segundo = 7
terceiro = 2
quarto = 9
quinto = 4
sexto = 1
setimo = 3
maior = primeiro
if (segundo>maior):
	maior=segundo


if (terceiro>maior):
        maior=terceiro


if (quarto>maior):
	maior=quarto

if (quinto>maior):
	maior=quinto

if (sexto>maior):
	maior=sexto

if (setimo>maior):
	maior=setimo


print('Maior valor da lista é: ', maior)



#1c)
menor = primeiro
if (segundo<menor):
	menor=segundo


if (terceiro<menor):
       menor=terceiro


if (quarto<menor):
	menor=quarto

if (quinto<menor):
	menor=quinto

if (sexto<menor):
	menor=sexto

if (setimo<menor):
	menor=setimo

print('Menor valor da lista é: ', menor)



#1d)
soma = 0
for i in l:
    soma = soma + i

print('A soma dos valores da lista é: ', soma)

#1e)
if sexto<terceiro<setimo<quinto<primeiro<segundo<quarto:
	print('lista em ordem crescente',sexto,terceiro,setimo,quinto,primeiro,segundo,quarto)


#1d)

if quarto>segundo>primeiro>quinto>setimo>terceiro>sexto:
	print('lista em ordem decrescente',quarto,segundo,primeiro,quinto,setimo,terceiro,sexto)#decrescente
	
	
 

	







	    
