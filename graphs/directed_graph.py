from datetime import datetime
from queue import Queue

class DGNode:
  def __init__(self, data=None):
    self.data = data
    self.children = []
    self.mark = None

  def __str__(self):
    return "Node <{}>".format(self.data)

  def __repr__(self):
    return "Node <{}>".format(self.data)

  def has_path_to(self, destination):
    if self == destination:
      return True

    current_mark = datetime.now()
    q = Queue()

    q.put(self)

    while not q.empty():
      node = q.get()
      if node == destination:
        return True
      node.mark = current_mark
      for child in node.children:
        if child.mark != current_mark:
          q.put(child)

    return False







