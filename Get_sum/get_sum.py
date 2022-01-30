def get_sum(a,b):
    
    if a == b:
      return a

    x = 0
    for y in range(min(a,b), max(a,b) + 1):
      x += y

    return x