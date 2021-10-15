import pdb

class SinglyLinkedList:
  def __init__(self, head=None):
    self.head = head

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

  def find_loop_node(self):
    if self.head == None:
      return False

    node1 = self.head
    node2 = self.head.next

    steps = 1

    while node2 and node1 != node2:
      node1 = self.step_n_nodes(1, node1)
      node2 = self.step_n_nodes(2, node2)
      steps += 1

    if not node2:
      return None

    node1 = self.step_n_nodes(1)
    node2 = self.step_n_nodes(steps + 1)

    # pdb.set_trace()
    while node1 != node2:
      node1 = self.step_n_nodes(1, node1)
      node2 = self.step_n_nodes(steps + 1, node2)

    return node1

  def step_n_nodes(self, n, node=None):
    if node:
      for i in range(0, n):
        node = node.next
    else:
      node = self.head
      for i in range(0, n - 1):
        node = node.next
    return node

  class NodeNotInListError(Exception):
    def __init__(self, data):
      self.data = data
      super().__init__('Data not in list: {}'.format(data))

