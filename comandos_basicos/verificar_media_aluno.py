nome = str(input('Nome do aluno: '))
nota1 = float(input('Digite 1º nota: '))
nota2 = float(input('Digite 2º Nota: '))

media = (nota1 + nota2) / 2

if media >= 60:
    resultado = ('APROVADO')
else:
    resultado = ('REPROVADO')

print('ALUNO {}, NOME: {}, MÉDIA: {}'.format(resultado, nome, media))