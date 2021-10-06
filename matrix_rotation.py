import pdb

def rotate(matrix, index=0, layer=0):
  if layer >= len(matrix)/2:
    return

  top  = matrix[layer][index]
  right = matrix[index][-1 - layer]
  bottom  = matrix[-1 -layer][-1 - index]
  left = matrix[-1 - index][layer]

  matrix[layer][index]          = left
  matrix[index][-1 - layer]     = top
  matrix[-1 -layer][-1 - index] = right
  matrix[-1 - index][layer]     = bottom

  if index < len(matrix) - layer - 2:
    rotate(matrix, index=index+1, layer=layer)
  else:
    layer += 1
    rotate(matrix, index=layer, layer=layer)

  return
