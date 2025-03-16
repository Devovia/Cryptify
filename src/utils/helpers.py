def validate_key(key, algorithm):
  if algorithm == "Caesar":
    return key.isdigit()
  elif algorithm == "Affine":
    try:
      key_a, key_b = map(int, key.split(','))
      return True
    except ValueError:
      return False
  return False