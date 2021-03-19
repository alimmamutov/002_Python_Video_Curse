import sys


print(sys.path)

for p in sys.path:
    print(p)

sys.path.append('D:')
import mymodule_on_d
