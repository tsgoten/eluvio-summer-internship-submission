Applicant: Tarang Srivatava - tarang.sriv@berkeley.edu

## Answer: 
longest bit strand length is `27648`
Files it appears in `sample.2` and `sample.3` only 
`sample.2` offset is `3072`
`sample.3` offset is `17408`

## Runtime Analysis: 
O(MN^2). We note that finding given N files and with each file of length M_1, M_2, ..., M_N
denote M = max(M_1, ..., M_N). Assuming that logical bit operations are O(1), 
finding the longest consecutive sequence of 1s is O(M). Then doing this for 
some fraction of the M runs is a constant scale with respect to M. So finding 
the longest bit strand between two files is O(M) and we are left to evaluate 
this for N files and each pairing which is O(MN^2). Amazingly for reasonable number of files and since M is so much larger than N in most cases the implementation is O(M). 

## Approach:
I used the subproblem of the longest consecutive sequence of 1s in a bit string. Then calling this on the xor values of each of the file and the logical not gives us all the positions that the files differ. We can count the longest sequence where the files are the same. 

### Small improvements
We can definitely memoize the bit string if the file size is roughly the same but number of files increases. If the file size increases drastically the approach still works, but just have to be careful in using a stream to read the files and a stream that XORs on each bit. Runtime is same either ways. Using C or C++ would certainly have improved runtime a decent amount, but the optimization from numpy does compensate and the complexity does remain unchanged. 
My program does take advantage of parallel processes, but it could be improved so multiple files can run in parallel and at the end of all the runs do we collect all the results. 


## Program Output: 
```
tarang@tarang sol % python final_solution.py
File sample.1 has length: 17408. File sample.2 has length: 30720
RESULT for 0 and 1: (8192, 9216, 5120)
File sample.1 has length: 17408. File sample.3 has length: 45056
RESULT for 0 and 2: (8192, 9216, 19456)
File sample.1 has length: 17408. File sample.4 has length: 30720
RESULT for 0 and 3: (8195, 9213, 5120)
File sample.1 has length: 17408. File sample.5 has length: 23552
RESULT for 0 and 4: (8589, 8058, 0)
File sample.1 has length: 17408. File sample.6 has length: 27648
RESULT for 0 and 5: (7434, 9213, 4096)
File sample.1 has length: 17408. File sample.7 has length: 21504
RESULT for 0 and 6: (3117, 0, 0)
File sample.1 has length: 17408. File sample.8 has length: 20480
RESULT for 0 and 7: (7452, 9213, 0)
File sample.1 has length: 17408. File sample.9 has length: 13312
RESULT for 0 and 8: (1524, 10870, 2412)
File sample.1 has length: 17408. File sample.10 has length: 14336
RESULT for 0 and 9: (1524, 11894, 1388)
File sample.2 has length: 30720. File sample.3 has length: 45056
RESULT for 1 and 2: (27648, 3072, 14336)
File sample.2 has length: 30720. File sample.4 has length: 30720
RESULT for 1 and 3: (16384, 14336, 0)
File sample.2 has length: 30720. File sample.5 has length: 23552
RESULT for 1 and 4: (7431, 9216, 5120)
File sample.2 has length: 30720. File sample.6 has length: 27648
RESULT for 1 and 5: (7431, 13312, 1024)
File sample.2 has length: 30720. File sample.7 has length: 21504
RESULT for 1 and 6: (8419, 6144, 8192)
File sample.2 has length: 30720. File sample.8 has length: 20480
RESULT for 1 and 7: (7449, 9216, 5120)
File sample.2 has length: 30720. File sample.9 has length: 13312
RESULT for 1 and 8: (7449, 2048, 12288)
File sample.2 has length: 30720. File sample.10 has length: 14336
RESULT for 1 and 9: (1555, 11186, 13832)
File sample.3 has length: 45056. File sample.4 has length: 30720
RESULT for 2 and 3: (16384, 14336, 14336)
File sample.3 has length: 45056. File sample.5 has length: 23552
RESULT for 2 and 4: (7431, 9216, 19456)
File sample.3 has length: 45056. File sample.6 has length: 27648
RESULT for 2 and 5: (7431, 13312, 15360)
File sample.3 has length: 45056. File sample.7 has length: 21504
RESULT for 2 and 6: (8419, 6144, 22528)
File sample.3 has length: 45056. File sample.8 has length: 20480
RESULT for 2 and 7: (7449, 9216, 19456)
File sample.3 has length: 45056. File sample.9 has length: 13312
RESULT for 2 and 8: (7449, 2048, 26624)
File sample.3 has length: 45056. File sample.10 has length: 14336
RESULT for 2 and 9: (3208, 1021, 2048)
File sample.4 has length: 30720. File sample.5 has length: 23552
RESULT for 3 and 4: (7434, 9213, 5120)
File sample.4 has length: 30720. File sample.6 has length: 27648
RESULT for 3 and 5: (14602, 6141, 1024)
File sample.4 has length: 30720. File sample.7 has length: 21504
RESULT for 3 and 6: (8660, 5903, 8192)
File sample.4 has length: 30720. File sample.8 has length: 20480
RESULT for 3 and 7: (15644, 1021, 5120)
File sample.4 has length: 30720. File sample.9 has length: 13312
RESULT for 3 and 8: (8422, 1021, 5120)
File sample.4 has length: 30720. File sample.10 has length: 14336
RESULT for 3 and 9: (3198, 1021, 2048)
File sample.5 has length: 23552. File sample.6 has length: 27648
RESULT for 4 and 5: (14339, 9213, 4096)
File sample.5 has length: 23552. File sample.7 has length: 21504
RESULT for 4 and 6: (6267, 0, 0)
File sample.5 has length: 23552. File sample.8 has length: 20480
RESULT for 4 and 7: (7434, 9213, 0)
File sample.5 has length: 23552. File sample.9 has length: 13312
RESULT for 4 and 8: (8458, 1021, 7168)
File sample.5 has length: 23552. File sample.10 has length: 14336
RESULT for 4 and 9: (3198, 1021, 2048)
File sample.6 has length: 27648. File sample.7 has length: 21504
RESULT for 5 and 6: (13539, 0, 0)
File sample.6 has length: 27648. File sample.8 has length: 20480
RESULT for 5 and 7: (14602, 2045, 4096)
File sample.6 has length: 27648. File sample.9 has length: 13312
RESULT for 5 and 8: (7434, 2045, 11264)
File sample.6 has length: 27648. File sample.10 has length: 14336
RESULT for 5 and 9: (3302, 1021, 2048)
File sample.7 has length: 21504. File sample.8 has length: 20480
RESULT for 6 and 7: (1524, 18038, 364)
File sample.7 has length: 21504. File sample.9 has length: 13312
RESULT for 6 and 8: (7452, 2045, 4096)
File sample.7 has length: 21504. File sample.10 has length: 14336
RESULT for 6 and 9: (3302, 1021, 2048)
File sample.8 has length: 20480. File sample.9 has length: 13312
RESULT for 7 and 8: (11267, 2045, 7168)
File sample.8 has length: 20480. File sample.10 has length: 14336
RESULT for 7 and 9: (4337, 9999, 6144)
File sample.9 has length: 13312. File sample.10 has length: 14336
RESULT for 8 and 9: (4337, 8975, 1024)```
