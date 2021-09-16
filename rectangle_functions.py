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

def is_rectangle(point_1, point_2, point_3, point_4):
  x_sorted = sorted([point_1, point_2, point_3, point_4], key=x)
  left_gradient  = ((x_sorted[1].y - x_sorted[0].y)/
                    (x_sorted[1].x - x_sorted[0].x))

  right_gradient = ((x_sorted[2].y - x_sorted[3].y)/
                    (x_sorted[2].x - x_sorted[3].x))
  if left_gradient != right_gradient:
    return False

  y_sorted_1 = sorted([x_sorted[0], x_sorted[1]], key=y)
  y_sorted_2 = sorted([x_sorted[2], x_sorted[3]], key=y)

  north_gradient = ((y_sorted_1[1].y - y_sorted_2[1].y)/
                    (y_sorted_1[1].x - y_sorted_2[1].x))

  south_gradient = ((y_sorted_1[0].y - y_sorted_2[0].y)/
                    (y_sorted_1[0].x - y_sorted_2[0].x))

  return north_gradient == south_gradient
