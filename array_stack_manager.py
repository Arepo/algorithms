class ArrayStackManager:
  def __init__(self):
    self.stack = [3,3,3]

  def push(self, *, stack, value):
    self.check_stack_exists(stack)

    stack_top_index = self.stack[stack]
    self.stack.insert(stack_top_index, value)
    for i in range(stack, 3):
      self.stack[i] += 1

  def is_empty(self, stack):
    self.check_stack_exists(stack)

    stack_top_index = self.stack[stack]
    if stack == 0:
      return stack_top_index == 3

    previous_stack_top_index = self.stack[stack - 1]
    return stack_top_index == previous_stack_top_index

  def peek(self, *, stack):
    self.check_stack_exists(stack)

    if self.is_empty(stack):
      return None

    stack_top_index = self.stack[stack]
    return self.stack[stack_top_index - 1]

  def pop(self, *, stack):
    self.check_stack_exists(stack)

    if self.is_empty(stack):
      raise EmptyStackError

    stack_top_index = self.stack[stack]
    ele = self.stack[stack_top_index - 1]
    del self.stack[stack_top_index - 1]
    for i in range(stack, 3):
      self.stack[i] -= 1
    return ele

  def check_stack_exists(_, stack):
    if stack not in [0,1,2]:
      raise NoSuchStackError

class EmptyStackError(Exception):
  pass

class NoSuchStackError(Exception):
  pass
