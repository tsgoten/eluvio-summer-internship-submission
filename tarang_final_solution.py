import numpy as np
import multiprocessing as mp

results = []
def streak(arr, n, strt):
  """ Given a bitstring ARR with length N, returns the 
  longest consecutive sequence of 1s. STRT is just a helper
  for the parrallelized implementation. 
  """
  count, result, res_ind = 0, 0, 0
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
  """ Simple callback. Takes in RESULT from streak()"""
  global results
  results.append(result)

def pair_strand(file1, file2):
  """Given two binary files FILE1 and FILE2, returns the 
  longest common binary strand. 
  """
  global results
  pool = mp.Pool(mp.cpu_count())
  s1 = np.fromfile(file1, dtype=bool)
  s2 = np.fromfile(file2, dtype=bool)
  l1, l2 = len(s1), len(s2)

  # Output the length of each file. 
  print('File {0} has length: {1}. File {2} has length: {3}'.format(file1, l1, file2, l2))
  if l1 > l2:
    l2, l1 = l1, l2
    s2, s1 = s1, s2

  for i in range(l2 - l1 + 1):
    temp = np.logical_not(np.logical_xor(s1, s2[i : l1 + i]))
    pool.apply_async(streak, args=(temp, l1, i), callback=collect_result)

  pool.close()
  pool.join()
  leng, small_ind, big_ind = max(results, key=lambda x: x[0])
  results = []
  return leng, small_ind, big_ind 

if __name__ == '__main__':
  files = ['sample.{0}'.format(i) for i in range(1, 11)] 
  for i in range(10):
    for j in range(i + 1, 10):
      print('RESULT for {0} and {1}: {2}'.format(i, j, pair_strand(files[i], files[j])))
  