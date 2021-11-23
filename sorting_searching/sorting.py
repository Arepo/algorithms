import pdb
from itertools import cycle
from operator import lt, gt

def valleyise(numbers):
  """Sort list into 'valleys' and 'peaks', such that each ele is higher/
  lower respectively than its surrounding numbers
  """
  index1 = 0
  index2 = 1
  length = len(numbers)
  operators = cycle([gt, lt])

  while index2 < length:
    operator = operators.__next__()
    if not operator(numbers[index1], numbers[index2]):
      numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    index1 += 1
    index2 += 1



