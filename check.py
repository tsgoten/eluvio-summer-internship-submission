import numpy as np

s1 = np.fromfile('sample.2', dtype=bool)
s2 = np.fromfile('sample.3', dtype=bool)

l1, l2 = len(s1), len(s2)

# ind = 9216
res = 27648
# strt = 3072

o1 = s1[3072: 3072 + res]
o2 = s2[17408: 17408 + res]

diff = np.logical_xor(o1, o2)

print(np.sum(diff))
print(len(diff))
