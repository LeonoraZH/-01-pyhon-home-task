# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите число от 1 до 4: '))

if number > 0 and number < 5:
  if number == 1:
    print('x > 0 and y > 0')
  elif number == 2:
    print('x < 0 and y > 0')
  elif number == 3:
    print('x < 0 and y < 0')
  else:
    print('x > 0 and y < 0')
else:
  print('Вы ввели неверное значение')