import numpy as np

def longest_substring(s1, s2):
  l1, l2 = len(s1), len(s2)
  lcs = [[0 for i in range(l2)] for j in range(l1)]

  max_len = 0
  row, col = 0, 0
  print('worked')
  for i in range(l1):
    for j in range(l2):
      print('on', i, j)
      if i == 0 or j == 0:
        lcs[i][j] = 0
      elif s1[i-1] == s2[j-1]:
        lcs[i][j] = lcs[i-1][j-1] + 1
        if max_len < lcs[i][j]:
          max_len = lcs[i][j]
          row, col = i, j
      else:
        lcs[i][j] = 0
  s1_offset = row
  s2_offset = col
  

  result = '_' * max_len

  length = max_len
  while lcs[row][col] != 0:
    length -= 1
    result[length] = s1[row - 1]

    row -= 1
    col -= 1

  return result, s1_offset, s2_offset

s1 = np.fromfile('sample.1', dtype=bool)
s2 = np.fromfile('sample.2', dtype=bool)
r, r1, r2 = longest_substring(s1, s2)

print(r)
