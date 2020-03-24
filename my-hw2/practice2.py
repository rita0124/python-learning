# Write a program that count discount
# When you go to a foodstand and buy looway
# There are many kinds of looway
# if you buy more than 200 NTD, than you can get discount 20 NTD
# 如果折20元後超過300元再打8折

ingredientsPrices = { 'princeNoodles':15, 'chickenHeart':20, 'driedTofu':10,
                      'tempura':15, 'hotPotIngredients':15, 'waterSpinach':30 }

# for k, v in ingredientsPrices.items():
#     print('單價 - {} : {} 元/個'.format(k,v))

basket = {}

basket['princeNoodles'] = 1
basket['chickenHeart'] = 1
basket['driedTofu'] = 2
basket['tempura'] = 3
basket['hotPotIngredients'] = 5
basket['waterSpinach'] = 5
sum = 0
for k,v in basket.items():
    print ( '單價: {} 元, 總數: {} 個, 總額: {} 元'.format(k, v, 
             ingredientsPrices[k] * v ))
    sum = sum + ingredientsPrices[k] * v
print ( '總金額: {} 元'.format(sum))

if sum >= 200:
    sum = sum - 20
    print('滿200元折扣20元')
else:
    print('未滿200元不折扣')

if sum >= 300:
    sum = sum * 0.8  
    print('如果折20元後超過300元再打8折')    
print(sum)