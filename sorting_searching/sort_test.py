import pdb
from sorting import valleyise

def test_valleyise():
  # Sort list into 'valleys' and 'peaks', such that each ele is higher/
  # lower respectively than its surrounding numbers
  numbers = [1,2,3,4,5,6,7,8,9,0]
  valleyise(numbers)
  assert numbers == [2,1,4,3,6,5,8,7,9,0]
