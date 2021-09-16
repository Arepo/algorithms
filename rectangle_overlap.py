import pdb
from collections import namedtuple
Rectangle = namedtuple('Rect', ('x', 'y', 'width', 'height'))

def overlapping_rectangle(rectangle_1, rectangle_2):
  x_sorted = sorted([rectangle_1, rectangle_2], key=x)
  y_sorted =  sorted([rectangle_1, rectangle_2], key=y)
  x3 = x_sorted[1].x
  y3 = y_sorted[1].y
  width3 =  min(x_sorted[1].width, abs(x_sorted[0].x - x_sorted[1].x + x_sorted[0].width))
  height3 = min(y_sorted[1].height, abs(y_sorted[0].y - y_sorted[1].y + y_sorted[0].height))
  if width3 > 0 and height3 > 0:
    return Rectangle(x3,y3,width3,height3)
  else:
    return None

def x(rectangle):
  return rectangle.x

def y(rectangle):
  return rectangle.y
