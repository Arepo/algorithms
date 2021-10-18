class LinkedListNode:
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
    if isinstance(nth_or_target, LinkedListNode):
      # Just pass the node up once we've found it
      return nth_or_target

    nth_of_this = nth_or_target + 1
    if nth_of_this == k:
      # We found our boy
      return self

    return nth_of_this

  def end_node(self):
    current = self
    while current.next:
      current = current.next
    return current

  def append(self, node):
    self.end_node().next = node


  def is_palindromic_from_position(self, position, length):
    if position - 0.5 == length/2:
      # We're at the middle node
      return self.next

    if position > length/2:
      # We've just gone past the middle node
      return self

    node_or_false = self.next.is_palindromic_from_position(position + 1, length)

    if node_or_false and node_or_false.data == self.data:
      # If a sublist is false the whole stays false, else we compare to the next node
      return node_or_false.next or True

    return False
