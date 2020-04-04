# 寫一支程式計算水果價格
# dict (Dictionary)
# dict = { 'key1': value1, 'key2': value2 }
fruitPrice = { 'apple': 30, 'banana': 10, 'lemon': 8, 'tomato': 25,
               'mango': 15 }

for k, v in fruitPrice.items():
    print('水果 - {} : {} 元/個'.format(k, v))


# 假設有個人來買三樣水果結帳
basket = {}     # 空的購物籃
basket['apple'] = 5     # BUY 5 APPLES
basket['mango'] = 10
basket['lemon'] = 3
basket['iphone11'] = 1

sum = 0
for k, v in basket.items():     # 取出購物欄內的物品和數值
    if k in fruitPrice.keys():  # 如果這項物品是水果店架上的水果
        print('購買的項目 - {} 共 {} 個, 價格 {} 元'.format(
                k, basket[k], fruitPrice[k] * basket[k]))
        sum = sum + fruitPrice[k] * basket[k]
        
print('總共金額: {} 元'.format(sum))