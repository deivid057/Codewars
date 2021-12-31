def descending_order(num):
  lst = [int(i) for i in str(num)]
  lst.sort(reverse=True)
  x = sum(d * 10 ** i for i, d in enumerate(lst[::-1]))
  return x
