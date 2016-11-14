'''
Created on 2016年11月14日

@author: Administrator
'''
import keyword
#  python关键字
keys = keyword.kwlist
for k in keys:
    print(k)
    
if True:
    print("this is a if-else statement if module")
    print("this is a if-else statement else module second")
else:
    print("this is a if-else statement else module")
print("this is a if-else statement end............")

sum = 2 + \
      3 + \
      4
print(sum)

#input("\n\n按下enter后退出")

import sys; x="running man"; sys.stdout.write(x + '\n')

data1 = 100
data2 = 20.02
data3 = 2.03E7
data4 = 2+3j
print("data1=%d,data2=%f,data3=%s,data4=%s" % (data1,data2,data3,data4))
print("data1=%d,data2=%f,data3=%s,data4=%s" % (data1,data2,format(data3,'.2e'),data4))


 

    