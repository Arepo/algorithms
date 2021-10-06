import pdb

def rotate(matrix, index=0, layer=0):
  if layer >= len(matrix)/2:
    return

  first  = matrix[layer][index]
  second = matrix[index][-1 - layer]
  third  = matrix[-1 -layer][-1 - index]
  fourth = matrix[-1 - index][layer]

  matrix[layer][index]          = fourth
  matrix[index][-1 - layer]     = first
  matrix[-1 -layer][-1 - index] = second
  matrix[-1 - index][layer]     = third

  if index < len(matrix) - layer - 2:
    rotate(matrix, index=index+1, layer=layer)
  else:
    layer += 1
    rotate(matrix, index=layer, layer=layer)

  return
