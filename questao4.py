nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media > 6.00:
    print('Aluno aprovado!')
elif 4.00 <= media <= 6.00:
    print('Aluno de recuperção!')
else:
    print('Aluno reprovado!')