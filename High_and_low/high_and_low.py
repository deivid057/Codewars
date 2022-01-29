def high_and_low(numbers):

    num = numbers.split()
    lista = [int(i) for i in num]

    max = 0
    min = 0

    for f in range(0, len(lista)):
      if f == 0:
        max = min = lista[f]
      else:
        if lista[f] > max:
          max = lista[f]
        elif lista[f] < min:
          min = lista[f]
    
    return(f'{max} {min}')