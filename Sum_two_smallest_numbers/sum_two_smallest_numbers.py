def sum_two_smallest_numbers(numbers):
  p = min(numbers)
  if p == min(numbers):
    numbers.remove(p)
  return p + min(numbers)