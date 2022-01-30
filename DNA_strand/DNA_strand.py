def DNA_strand(dna):
  lista = list(dna)
  l = []

  for m in lista:
    if m == 'A':
      l.append("T")
    elif m == 'T':
      l.append("A")
    elif m == 'G':
      l.append("C")
    elif m == 'C':
      l.append("G")
  return "".join(l)