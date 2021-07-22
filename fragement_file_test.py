import time
from fragement_file import open_fragement


with open_fragement("test.txt", "w", interval=3) as f:
    i = 0
    while True:
        i += 1
        f.write(str(i))
        time.sleep(1)
