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


class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_node):
    new_node.next = self.head
    self.head = new_node

  def insert_after(self, prev_node, new_node):
    new_node.next = prev_node.next
    prev_node.next = new_node

  def append(self, node):
    if self.head:
      self.end_node().next = node
    else:
      self.head = node

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

  def is_palindrome(self, length):
    return self.head.is_palindromic_from_position(1, length)

  def intersecting_node(self, other):
    if self.head == None or other.head == None:
      return None

    def count_to_intersection(list1, list2):
      difference = abs(self_length - other_length)
      position = 0
      list1_node, list2_node = list1.head, list2.head
      while position < difference:
        # Move to same distance from end
        list2_node = list2_node.next
        position += 1
      while list2_node != list1_node:
        list1_node = list1_node.next
        list2_node = list2_node.next
      return list1_node

    self_length, self_last = self.length_and_last_node()
    other_length, other_last = other.length_and_last_node()

    if self_last != other_last:
      # If they ever intersect they'll become the same sub-list til the end
      return None

    if self_length <= other_length:
      return count_to_intersection(self, other)
    return count_to_intersection(other, self)

  def length_and_last_node(self):
    length = 1
    node = self.head
    while node.next:
      length += 1
      node = node.next
    return (length, node)


  class NodeNotInListError(Exception):
    def __init__(self, data):
      self.data = data
      super().__init__('Data not in list: {}'.format(data))

