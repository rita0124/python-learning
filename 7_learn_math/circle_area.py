import math

# 輸入圓的半徑，計算圓面積
def area(r):
    a = math.pi * (r**2)
    return a

a = area(5)
print('圓面積: ' +str(a) + '(cm^2)')