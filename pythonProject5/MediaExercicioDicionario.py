aluno = dict()

aluno ['nome'] = str(input('nome:'))
aluno ['media'] = float(input('media:'))

if aluno['media'] >=7:
    aluno['situação'] = 'aprovado'

else:
    aluno['situação'] = 'reprovado'


for x, y in aluno.items():
    print(f' -{x}é igual a {y}')

print(aluno.keys())
print (aluno.values())

