# This is one line comment
# Write a temperature transformation program
# C -> F
# F = 9/5 C + 32

degC = int(input('輸入攝氏溫度: '))
print('所輸入的攝氏溫度為 {} 度'.format(degC))

degF = degC * 9 / 5 + 32
print('華氏溫度 = {}'.format(degF))