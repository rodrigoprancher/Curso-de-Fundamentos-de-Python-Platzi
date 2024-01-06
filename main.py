import random

mazo = [
    (1, 'As'),
    (2, 'Dos'),
    (3, 'Tres'),
    (4, 'Cuatro'),
    (5, 'Cinco'),
    (6, 'Seis'),
    (7, 'Siete'),
    (8, 'Ocho'),
    (9, 'Nueve'),
    (10, 'Diez'),
    (10, 'Jota'),
    (10, 'Reina'),
    (10, 'Rey')
]

nombre_jugador = input("Ingrese su nombre: ")
print('')

puntos_jugador = 0
puntos_crupier = 0

ases_en_mano = 0

mano_jugador = []
mano_crupier = []

carta1 = random.choice(mazo)
carta2 = random.choice(mazo)

mano_jugador.extend([carta1, carta2])
print('     Tus cartas  ')
print('*' * 20)
print('')
for carta in mano_jugador:
  print(carta[1])

carta3 = random.choice(mazo)
carta4 = random.choice(mazo)

mano_crupier.extend([carta3, carta4])

for carta in mano_jugador:
  puntos_jugador += carta[0]

  if carta[1] == 'As':
    ases_en_mano += 1

while puntos_jugador > 21 and ases_en_mano:
  puntos_jugador -= 10
  ases_en_mano -= 1

print('')
print('Tus puntos:', puntos_jugador)
print('')
print(' Cartas del crupier  ')
print('*' * 20)
print('')
print(carta3[1])