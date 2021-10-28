import sys
from collections import deque
import pdb
from level import Level

this = sys.modules[__name__]

this.available_respondents = deque()
this.available_managers = deque()
this.available_directors = deque()

def dispatch_call(caller):
  """Find an available caller"""
  assign_call(caller, Level(1))

def assign_call(caller, level):
  """Pass the caller to an employee of the appropriate level and remove them from the queue"""
  if not available_employees_at_level(level):
    print("*Soothing hold muzak plays*")
    return
  available_employees_at_level(level).pop().take_call(caller)

def escalate(caller, employee):
  """Pass the caller up a level"""
  level = Level(employee.level.value + 1)
  print(f'Passing them up to a {level.name}')
  assign_call(caller, level)

def enqueue(employee):
  """Make the employee available again (at the back of the queue)"""
  queue = available_employees_at_level(employee.level)
  queue.appendleft(employee)

def available_employees_at_level(level) -> deque:
  """Return the relevant queue"""
  return {
    1: this.available_respondents,
    2: this.available_managers,
    3: this.available_directors
  }[level.value]

