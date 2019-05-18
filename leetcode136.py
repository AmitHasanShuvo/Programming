from collections import Counter

for i in [k for k, v in Counter(nums).items() if v == 1]:
    return i
