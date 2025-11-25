import time
from calculator import add

print("Calculator deployed on Liara!")
print(add(2, 3))

# Keep app alive
while True:
    time.sleep(10)