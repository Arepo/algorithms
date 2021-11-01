from caller import Caller
import call_handler
from employee import Employee
import random
import pdb

# Simulate a call centre using singleton object pattern (not my choice!)

# Run this file to execute a call to the centre. You might have to run it a few times to get good service.

respondent_count = random.randint(0,3)
manager_count = random.randint(0,2)
director_count = random.randint(0,1)

print(f'Today we have {respondent_count} responders, {manager_count} managers, and {director_count} directors available')

for _ in range(respondent_count):
  call_handler.enqueue(Employee(1))

for _ in range(manager_count):
  call_handler.enqueue(Employee(2))

for _ in range(director_count):
  call_handler.enqueue(Employee(3))

caller = Caller('071234567')
call_handler.dispatch_call(caller)

