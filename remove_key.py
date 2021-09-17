import pdb

def remove_key(arr: list, key) -> int:
  if len(arr) == 0:
    return 0

  candidate_index = 0
  replacement_index = 0

  while replacement_index < len(arr):

    while replacement_index < len(arr) and arr[replacement_index] == key:
      replacement_index += 1

    if replacement_index == len(arr):
      break

    arr[candidate_index] = arr[replacement_index]
    replacement_index += 1
    candidate_index += 1

  return candidate_index
