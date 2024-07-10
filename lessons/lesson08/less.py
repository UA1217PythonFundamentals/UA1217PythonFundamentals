import sys
from pprint import pprint
import customer.personal
import second
# import second2
sys.path.append('c:\\data\\github\\UA1217PythonFundamentals\\lessons\\lesson03')

import lesson03

pprint(sys.path)


# import customer.personal.users.worker.worker

# print(customer.personal.users.worker.worker.workers)

# import customer.personal.users.worker.worker as cw

# print(cw.workers)

# from customer.personal.users.worker.worker import workers

# print(workers)
# from customer.personal.users.worker import worker
# print(worker.workers)
from customer.personal.users.worker import worker
from customer.personal import cus as cp
from customer.salary import cus as cs
from customer import cus
import customer

print(cus.b)
print(cp.c)
print(cs.a)

from customer.personal import workers


import math