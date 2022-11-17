def alphabet_position(text):
  dic = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14,
             "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

  characters = ['!', '.', ',', '+', '*', '/', '-', '(', ')', '&', '%', '$', '#', '@',"'", ' ']
  text = text.translate(str.maketrans('', '', ''.join(characters)))
  text_list = list(text.lower())

  list_positions = []
  counter = 0
  size = len(text_list)

  for i in text_list:
    if counter <= size:
      list_positions.append(dic[str(text_list[counter])])
    counter += 1

  result = ' '.join(map(str, list_positions))
  return result