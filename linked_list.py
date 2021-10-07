import pdb

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return "Node <{}>".format(self.data)

  def __repr__(self):
    return "Node <{}>".format(self.data)

  def kth_from_end(self, k):
    if not self.next and k == 1:
      return self
    elif not self.next:
      return 1

    nth_or_target = self.next.kth_from_end(k)
    if isinstance(nth_or_target, Node):
      # Just pass the node up once we've found it
      return nth_or_target

    nth_of_this = nth_or_target + 1
    if nth_of_this == k:
      # We found our boy
      return self

    return nth_of_this

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_node):
    new_node.next = self.head
    self.head = new_node

  def insert_after(self, prev_node, new_node):
    new_node.next = prev_node.next
    prev_node.next = new_node

  def append(self, new_node):
    if self.head:
      self.end_node().next = new_node
    else:
      self.head = new_node

  def end_node(self):
    current = self.head
    while current.next:
      current = current.next
    return current

  def traverse_until(self, data):
    current = self.head
    while current.next and current.data != data:
      current = current.next
    if data != current.data:
      raise NodeNotInListError(data)
    else:
      return current

  def print_list(self):
    current = self.head
    while current:
      print(current)
      current = current.next

  def kth_from_end(self, k):
    return self.head.kth_from_end(k)

  class NodeNotInListError(Exception):
    def __init__(self, data):
      self.data = data
      super().__init__('Data not in list: {}'.format(data))

