import numpy as np


def streak(arr, n):
  count = 0 
  result = 0 
  for i in range(0, n):
    if (arr[i] == 0):
      count = 0
    else:
      count+= 1 
      result = max(result, count) 
  return result   

if __name__ == '__main__':

  s1 = np.fromfile('sample.1', dtype=bool)
  s2 = np.fromfile('sample.2', dtype=bool)

  s11 = ''.join(map(lambda x: str(int(x)), s1))
  i1 = int(s11, 2)

  s22 = ''.join(map(lambda x: str(int(x)), s2))
  i2 = int(s22, 2)

  l1 = len(s1)
  l2 = len(s2)

  most = 0
  res = 0
  ind = 0

  for i in range(l2 - l1):
    temp = np.logical_not(np.logical_xor(s1, s2[i : l1 + i]))
    t = streak(temp, l1)
    if t > res:
      res = t
      ind = i



print(temp, res, ind)
print(l1, l2)