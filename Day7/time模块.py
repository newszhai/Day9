# from time import time
# a=time()
# # print(a)
# # for x in range(1000):
# #     pass
# # b=time()-a
# # print(b)
from time import time,sleep,perf_counter,gmtime,localtime
'''a=time()
print(a)
sleep(10)
b=time()
print(b)
print(b-a)
'''
print(perf_counter())
sleep(3)
print(perf_counter())
print(gmtime())
print(localtime())

from calendar import *
thismoth=month(2024,6,2)
print(thismoth)
print(isleap(2024))
