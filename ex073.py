times = ('Flamengo','Santos','Palmeiras','Grêmio','Paranaense','São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco da Gama','Atlético Mineiro','Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')
print('LISTA DE TIMES DO BRASILEIRÃO')
print('-=' * 34)
print(f'Os times do brasileirão são {times}.')
print('-=' * 34)
print(f'Os cinco primeiros times são {times[0:5]}.')
print('-=' * 34)
print(f'Os quatro últimos times são {times[16:21]}.')
print('-=' * 34)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-=' * 34)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')