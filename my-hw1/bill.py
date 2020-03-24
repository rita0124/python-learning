# Buy fruits from market, count bill (fruit price * number)
fruit_name = ['apple', 'banana', 'lemon', 'mango']
fruit_num = [ 3, 5, 10, 1 ]  # 各項水果的數量
fruit_price = [ 50, 10, 20, 300 ]  # 各項水果價格 

for i in range(4):
    count = fruit_price[i] * fruit_num[i]
    print('小計: '+str(count))
