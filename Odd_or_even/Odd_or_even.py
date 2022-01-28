def odd_or_even(arr):
  soma = 0
  for num in arr:
    soma += num
  resto = soma % 2
  if resto == 0:
    p = ('even')
    return p
  else:
    p1 = ('odd')
    return p1