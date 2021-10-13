import pdb

class Stackset:
  def __init__(self, max_stack):
    # Track stack size and head
    self.max_stack = max_stack
    self.stacks = [[0, None]]
    self.head = None
    self.position = 0

  def push(self, node):
    self.top_stack = self.stacks[-1]
    # Update the linked list
    old_head = self.head
    node.next = old_head
    self.head = node

    if self.max_stack > self.top_stack[0]:
      # Update the tracker
      self.top_stack[0] += 1
      self.top_stack[1] =  node
    else:
      self.stacks.append([1, node])

  def pop(self):
    # pops from start
    old_head = self.head
    self.head = self.head.next
    old_head.next = None
    if self.top_stack[0] == 1 and len(self.stacks > 1):
      self.stacks.pop()
    else:
      self.top_stack[0] -= 1
    self.top_stack[1] = self.peek()
    return old_head

  def pop_at(self, stack_index):
    stack = self.stacks[stack_index]
    # TODO deal with emptied stacks
    stack[0] -= 1
    old_head = stack[1]
    stack[1] = old_head.next
    prior_node = self.fetch_preceding_node(self.stacks[stack_index + 1][1], old_head)
    prior_node.next = stack[1]
    return old_head

  def fetch_preceding_node(self, origin, node):
    # TODO will this break when stacks get emptied?
    next_node = origin
    while next_node.next != node:
      next_node = next_node.next
    return next_node


  def peek(self):
    return self.head

  def top_stack(self):
    self.stacks[-1]


