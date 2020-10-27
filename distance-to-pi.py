import sys
import math

min,max = input().strip().split(' ')
min,max = [int(min),int(max)]

pi = 314159265358979323846264338327950288419716939937515
rmin = 0
rmax = 0
for i in range(min, max + 1):
    q, r = divmod(i * pi, 10 ** 50)
    if rmin == 0 or r < rmin:
        rmin = r
        denom = i
        numerat = q
    r = 10 ** 50 - r
    if rmin == 0 or r < rmin:
        rmin = r
        denom = i
        numerat = q + 1
#print("{}/{}".format(nd1[0], nd1[1]))
print(str(numerat) + '/' + str(denom))
