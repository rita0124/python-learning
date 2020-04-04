bookNumber = [2,4,6,8,10]
bookPrice = [200,400,600,800,1000]
# price = []
sum = 0

for x in range(5):
    # Rita: Make every item price into a list
    # price.append(bookNumber[x] * bookPrice[x])
    # print('每項總價: '+str (price) + ' 元')
    # sum = sum + price[x]
    # Better one: use one variable to store total price
    # 因為這樣就不用特別花一個 LIST 去儲存很多項變數
    # sum = sum + bookNumber[x] * bookPrice[x]
    sum += bookNumber[x] * bookPrice[x]

print('總金額: '+ str (sum) +' 元')