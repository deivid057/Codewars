def sum_digits(number):
    u = str(abs(number))
    soma = 0
    for i in range(len(u)):
      soma += int(u[i])
    return soma