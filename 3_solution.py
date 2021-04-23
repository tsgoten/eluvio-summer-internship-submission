import numpy as np
import multiprocessing as mp

results = []

def streak(arr, n, strt):
  count = 0 
  result = 0 
  res_ind = 0
  for i in range(0, n):
    if (arr[i] == 0):
      count = 0
    else:
      count+= 1 
      if count > result:
        result = count
        res_ind = i
  return result, res_ind - result + 1, strt


def collect_result(result):
    global results
    results.append(result)

if __name__ == '__main__':
  pool = mp.Pool(mp.cpu_count())

  s1 = np.fromfile('sample.1', dtype=bool)
  s2 = np.fromfile('sample.2', dtype=bool)

  l1, l2 = len(s1), len(s2)

  most = 0
  res = 0
  ind = 0

  pool = mp.Pool(mp.cpu_count())

  alls = []

  for i in range(l2 - l1 + 1):
    temp = np.logical_not(np.logical_xor(s1, s2[i : l1 + i]))
    pool.apply_async(streak, args=(temp, l1, i), callback=collect_result)

  pool.close()
  pool.join()

  print('RESULT: ', max(results, key=lambda x: x[0]))
