def number(bus_stop):
  entry = []
  exit = []

  for i in bus_stop:
    entry.append(i[0])
    exit.append(i[1])
  return sum(entry) - sum(exit)