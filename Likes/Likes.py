def likes(names)->list:
  length = len(names)
  new_length = length - 2
  
 
  p = 'no one likes this'
  

  if length == 0:
    return p
  elif length == 1:
    p1 = (f'{names[0]} likes this')
    return p1
  elif length == 2:
    p2= (f'{names[0]} and {names[1]} likes this')
    return p2
  elif length == 3:
    p3 = (f'{names[0]}, {names[1]} and {names[2]} likes this')
    return
  elif length > 3:
    p4 = (f'{names[0]}, {names[1]} and {new_length} others likes this')
    return
  else:
    return 
