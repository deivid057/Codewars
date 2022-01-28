def positive_sum(arr):
  positive = []    
  negative = []
  
  for i in arr:
    if i < 0:
      negative.append(i)
    else:
      positive.append(i)

  return(sum(positive))