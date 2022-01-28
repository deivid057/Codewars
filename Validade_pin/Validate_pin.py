def validate_pin(pin):
  if len(pin) == 4 and pin.isdecimal() == True:
    return True
  elif len(pin) == 6 and pin.isdecimal() == True:
    return True
  else:
    return False
