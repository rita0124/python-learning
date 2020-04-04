# 重量百分率濃度(wt%)
# 溶質重w2(g), 溶劑重w1(g)

def weight_percentage_concentration(w1, w2):
    wt = ( w2/( w1 + w2 )) * 100
    return wt

wt = weight_percentage_concentration(99, 1)
print('重量百分率濃度: ' + str(wt) + ' wt%')

# 體積百分率濃度(v%)
# 溶液體積v(ml), 溶質體積v2(ml)

def volume_percentage_concentration(v, v2):
    v = ( v2 / v) * 100
    return v

v = volume_percentage_concentration(100, 1)
print('體積百分率濃度: ' + str(v) + ' v%')

# 百萬分數(ppm)
# 溶質重w2(g), 溶劑重w1(g)

def ppm_water_solution(w1, w2):
    ppm_w = ( w2 / (w1+w2 )) * ( 10**6 )
    return ppm_w

ppm_w = ppm_water_solution(950, 50)
print('百萬分濃度: ' + str(ppm_w) + ' ppm')

# 百萬分數(ppm)
# 莫爾數n1, 莫爾數n2

def ppm_gas_mixture(n1, n2):
    ppm_g = ( n2 / ( n1 + n2)) * ( 10**6)
    return ppm_g

ppm_g = ppm_gas_mixture(1, 99)
print('百萬分濃度: ' + str(ppm_g) + ' ppm')

# 體積莫爾濃度(M)
# 溶質重w2, 溶質分子量F, 溶液體積v

def molarity(w2, F, v):
    molarity = ( ( w2 / F ) / ( v / 1000 ))
    return molarity
molarity = molarity (80, 40, 100)
print('體積莫爾濃度:' + str(molarity) + ' M')
