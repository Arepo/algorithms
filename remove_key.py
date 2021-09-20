def remove_key(arr: list, key) -> int:
  write_index = 0
  read_index = 0

  while read_index < len(arr):

    if arr[read_index] != key:
      arr[write_index] = arr[read_index]
      write_index += 1

    read_index += 1

  return write_index
