def is_sorted_and_how(arr):
  ascending = sorted(arr, key=int)
  descending = sorted(arr, key=int, reverse=True)

  if arr == ascending:
    return ("yes, ascending")
  elif arr == descending:
    return ("yes, descending")
  else:
    return ("no")