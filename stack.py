class Stack:
  def __init__(self):
    self.head = None

  def push(self, new_node):
    node.next = self.old_head
    self.head = node

  def pop(self):
    # pops from start
    old_head = self.head
    self.head = self.head.next
    old_head.next = None
    return old_head

  def peek(self):
    self.head

  def is_empty(self):
    not not self.head
