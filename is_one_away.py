def is_one_away(string1, string2):
  if len(string1) < len(string2):
    first = string1
    second = string2
  else:
    first = string2
    second = string1

  if len(second) - len(first) > 1:
    return False

  same_length = True if len(first) == len(second) else False

  short_str_index = 0
  long_str_index = 0
  discrepancies = 0

  while short_str_index < len(first):
    # If the characters don't match
    if first[short_str_index] != second[long_str_index]:

      discrepancies += 1

      if discrepancies > 1:
        return False

      if same_length:
        short_str_index += 1

    else:
      short_str_index += 1

    long_str_index += 1

  return True
