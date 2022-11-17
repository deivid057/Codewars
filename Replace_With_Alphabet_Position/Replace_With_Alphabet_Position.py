def alphabet_position(text):
  dic = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14,
             "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

  caracteres = ['!', '.', ',', '+', '*', '/', '-', '(', ')', '&', '%', '$', '#', '@',"'", ' ']
  frase = text.translate(str.maketrans('', '', ''.join(caracteres)))
  frase_list = list(frase.lower())

  list_positions = []
  contador = 0
  tamanho = len(frase_list)

  for i in frase_list:
    if contador <= tamanho:
      list_positions.append(dic[str(frase_list[contador])])
    contador += 1

  r = ' '.join(map(str, list_positions))
  return r