import time

import gc

class C:
    def __init__(self):
        self.money = 0

c = C()
lst1 = [c]
lst2 = [c]

print(lst1)
print(lst2)

c = None

gc.collect()
time.sleep(10)
# Accessing the instance from either list should now raise an error
print(lst1[0].money)  # This line should now raise an error
print(lst2[0].money)  # This line should now raise an error
