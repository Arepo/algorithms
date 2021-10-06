import pdb

def rotate(matrix, i=0, j=0):
  if j > len(matrix)/2:
    return

  first  = matrix[j][i]
  second = matrix[i][-1 - j]
  third  = matrix[-1 -j][-1 - i]
  fourth = matrix[-1 - i][j]
  pdb.set_trace()

  return
