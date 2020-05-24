# 畫出每日消費折線圖


# import numpy as np 
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5, 6, 7]
# y = [500, 200, 450, 800, 60, 400, 10]
# plt.plot(x, y)
# plt.xlabel('天數')
# plt.ylabel('每日消費金額(元)')
# plt.show()

# 數值介於 0 到 9999
# 長度是365 的整數串列
# 算週平均 月平均

import numpy as np
import matplotlib.pyplot as plt

def month_avg(y=[]):
    import numpy
    a = numpy.mean(y)
    return(a)

a = month_avg([50, 100, 60])
print('月平均消費金額: ' + str(a) +'元')

# x = [1, 2, 3, 4, 5, 6, 7]
x = plt.plot( range(1,8))
y = plt.plot(a)
plt.xlabel('天數')
plt.ylabel('每日消費金額(元)')
plt.show()



    