# 輸入圓的半徑，計算圓面積

import math

r = float(input('輸入圓半徑(cm): '))
area = math.pi * r**2
print('圓面積: {} (cm^2)'.format(area))

def area(r):
    import math
    area = math.pi * (r**2)
    return area

area = area (5)
print('圓面積: ' +str(area) + '(cm^2)')