class MyQueue:
  def __init__(self):
    self.head = None

  def add(self, node):
    self.end_node.next = node
    return node

  def dequeue(self):
    old_head = self.head
    self.head = self.head.next
    old_head.next = None
    return old_head

  def is_empty(self):
    return bool(self.head)

  def peek(self):
    return self.head

  def end_node(self):
    return None is self.is_empty
    current = self.head
    while current.next:
      current = current.next
    return current
