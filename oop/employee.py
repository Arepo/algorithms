import call_handler
from level import Level

class Employee:
  def __init__(self, level=1):
    self.level = Level(level)

  def take_call(self, caller):
    """Use keyboard input to determine the call outcome"""
    outcome = ' '
    while not outcome or not outcome in 'yn' or outcome == 'n' and self.level.value == 3:
      outcome = input(f'Caller {caller.phone_number} is on the line, monsieur {self.level.name}. Can you help them on your own? (y/n) ').lower()
      if outcome == 'y':
        caller.resolved = True
        call_handler.enqueue(self)
        print(f'Call resolved by a {self.level.name}')
      elif self.level.value == 3:
        print('Well you better figure out how, pilgrim')
      elif outcome == 'n':
        call_handler.escalate(caller, self)
        call_handler.enqueue(self)

