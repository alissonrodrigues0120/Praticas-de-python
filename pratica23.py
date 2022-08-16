ficha={}

ficha['nome']=str(input('nome do aluno: '))
ficha['nota']=float(input('nota: '))


if(ficha.get('nota')>=7.0) :
    ficha['situação']='aprovado'
elif (ficha.get('nota')<7) and (ficha.get('nota')>=4):
    ficha['situação']='recuperação'
else:
    ficha['situação']='reprovado'


print('\n'[1:])
fmt='{} é {}'
for k in ficha.keys():
    print(fmt.format(k, ficha.get(k)))