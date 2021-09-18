def remove_key(arr: list, key) -> int:
  read_index = 0
  write_index = 0

  while write_index < len(arr):

    if arr[write_index] != key:
      arr[read_index] = arr[write_index]
      read_index += 1

    write_index += 1

  return read_index
