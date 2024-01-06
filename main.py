# Importamos random para que el programa elija cartas aleatorias.
import random

# Le preguntamos al usuario su nombre.
nombre_jugador = input("Ingrese su nombre: ")
while nombre_jugador == '':
  nombre_jugador = input("Por favor, ingrese su nombre: ")
nombre_jugador = nombre_jugador.title()
print('')

# Iniciamos un bucle while para que el juego se repita en caso de que el usuario quiera jugar otra ronda.
while True:
  # Creamos una lista con las cartas que se van a utilizar en el juego.
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

  # Creamos dos variables para almacenar el puntaje de cada jugador.
  puntos_jugador = 0
  puntos_crupier = 0

  # Creamos dos variables para almacenar la cantidad de ases que el jugador y el crupier tienen.
  ases_en_mano_jugador = 0
  ases_en_mano_crupier = 0

  # Creamos una lista para almacenar las cartas que el jugador y el crupier tienen.
  mano_jugador = []
  mano_crupier = []

  # Creamos dos variables para guardar las cartas del jugador utilizando random.choise.
  carta1 = random.choice(mazo)
  carta2 = random.choice(mazo)

  # Mostramos al usuario sus cartas.
  mano_jugador.extend([carta1, carta2])
  print('\n     Tus cartas  ')
  print('*' * 20, '\n')

  for carta in mano_jugador:
    print(carta[1])

  # Elegimos dos cartas aleatorias para el crupier.
  carta3 = random.choice(mazo)
  carta4 = random.choice(mazo)
  
  mano_crupier.extend([carta3, carta4])

  # Sumamos las cartas de los jugadores para ver el total de ellas y contamos la cantidad de Ases que hay.
  for carta in mano_jugador:
    puntos_jugador += carta[0]
    if carta[1] == 'As':
      ases_en_mano_jugador += 1
  
  for carta in mano_crupier:
    puntos_crupier += carta[0]
    if carta[1] == 'As':
      ases_en_mano_crupier += 1

  # Bucle while para calcular el valor del As del jugador.
  while puntos_jugador > 21 and ases_en_mano_jugador:
    puntos_jugador -= 10
    ases_en_mano_jugador -= 1
  
  # Imprimios el puntaje del jugador.
  print('\nTus puntos:', puntos_jugador, '\n')

  # Imprimimos la primera carta del crupier.
  print('\n Cartas del crupier  ')
  print('*' * 20, '\n')
  
  print(carta3[1])

  # Opción que tiene el usuario para decidir si se planta con los puntos que tiene o agarra otra carta.
  print('\n     ¿Qué deseas hacer?')
  print('1. Plantarse | 2. Pedir carta')
  opcion = int(input('Ingrese una opción: '))
  while opcion != 2 and opcion != 1: # Si la opción es diferente a 1 o 2, se le pide que ingrese una opción válida.
    opcion = int(input('Opción invalida. Por favor, ingrese "1" si deseas plantarte o ingrese "2" para pedir una carta '))

  # Bucle while para que el jugador pueda pedir cartas hasta que se planta o se pase de 21.
  while opcion == 2 and puntos_jugador < 21:
    carta5 = random.choice(mazo)
    mano_jugador.append(carta5)
    puntos_jugador += carta5[0]
    
    print('\n     Tus cartas  ')
    print('*' * 20, '\n')
    
    for carta in mano_jugador:
      print(carta[1])
    
    print('\nTus puntos:', puntos_jugador, '\n')
    
    if puntos_jugador < 21:
      print('     ¿Qué deseas hacer?')
      print('1. Plantarse | 2. Pedir carta')
      opcion = int(input('Ingrese una opción: '))
      while opcion != 2 and opcion != 1:
        opcion = int(input('Opción invalida. Por favor, ingrese "1" si deseas plantarte o ingrese "2" para pedir una carta '))
        
    elif puntos_jugador > 21: # Si el jugador se pasa de 21, se le informa que perdió.
        print('¡Te pasaste de 21! Has perdido.')

  # Bucle while para que el crupier agarre cartas hasta que tenga 17 o más puntos.
  while puntos_crupier < 17:
    carta6 = random.choice(mazo)
    mano_crupier.append(carta6)
    puntos_crupier += carta6[0]
    if carta6[1] == 'As':
      ases_en_mano_crupier += 1
  
    while puntos_crupier > 21 and ases_en_mano_crupier:
      puntos_crupier -= 10
      ases_en_mano_crupier -= 1
      
  print('\n Cartas del crupier  ')
  print('*' * 20, '\n')
  
  for carta in mano_crupier:
    print(carta[1])
  
  print('\nPuntos del crupier:', puntos_crupier, '\n')
  
  # Condicionales que le informan al usuario si ganó, perdió o empató.
  if puntos_crupier > 21:
    print(f'El crupier se ha pasado de 21. ¡Felicidades {nombre_jugador}! Has ganado.')
  elif puntos_crupier == 21:
    print('El crupier ha obtenido 21. ¡Lo siento! Has perdido.')
  elif puntos_jugador == puntos_crupier:
      print('¡Empate!')
  elif puntos_jugador > puntos_crupier and puntos_jugador < 21:
      print(f'¡Felicidades {nombre_jugador}! Has ganado.')
  elif puntos_crupier > puntos_jugador and puntos_crupier < 21:
    print('El crupier ha ganado por más puntos. ¡Lo siento!')
  else:
      print('El crupier ha ganado.')

  # Preguntamos al usuario si quiere jugar otra ronda.
  otra_ronda = input(f'\n¿Deseas jugar otra ronda {nombre_jugador}? (s/n): ')
  if otra_ronda.lower() != 's':
    print('\nGracias por jugar. ¡Hasta luego!')
    break