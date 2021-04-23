import numpy as np
import resource

def getDecimal(s):
    lenn = len(s)
    ans = 0
    j = 0
    for i in range(lenn - 1, -1, -1):
        if (s[i] == '1'):
            ans += pow(2, j)
        j += 1
    return ans
  
# Utility function which convert decimal
# number to its binary representation
def convertToBinary(n):
  
    return bin(n)[2:]
  
# utility function to check all the
# substrings and get the longest substring.
def longestCommon(n, m):
    mx = -10**9 # maximum lenngth
    s1 = convertToBinary(n)
    s2 = convertToBinary(m)
    #print(s1,s2)
  
    res="" # final resultant string
    lenn = len(s1)
    l = lenn
  
    # for every subof s1,
    # check if its lenngth is greater than
    # previously found string
    # and also it is present in s2
    while (lenn > 0):
  
        for i in range(l - lenn + 1):
  
            temp = s1[i:lenn + 1]
            # print(temp)
  
            tlenn = len(temp)
  
            if (tlenn > mx and( s2.find(temp) != -1)):
                res = temp
                mx = tlenn
  
        lenn = lenn - 1
  
    # If there is no common string
    if (res == ""):
        return -1
  
    return getDecimal(res)
  
  


s1 = np.fromfile('sample.1', dtype=bool)
s2 = np.fromfile('sample.2', dtype=bool)

s11 = ''.join(map(lambda x: str(int(x)), s1))
i1 = int(s11, 2)

s22 = ''.join(map(lambda x: str(int(x)), s2))
i2 = int(s22, 2)


# print(i1)
# print(i2)

# Driver Code
n = i1
m = i2
print("longest common decimal value : ",
                    longestCommon(m, n))

# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)