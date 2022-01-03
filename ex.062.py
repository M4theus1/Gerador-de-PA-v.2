c = 0
mais = 10
total = 0
print('GERADOR DE PA')
print('=~'*15)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n
while mais != 0:
    total = total + mais
    while c < total:
        print('{} -> '.format(termo), end=' ')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer? '))
print('FIM')
