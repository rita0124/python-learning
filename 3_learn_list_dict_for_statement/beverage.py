# 10 kinds of drinks / prices
drinkPrice = {
    '美式黑咖啡': 15, '招牌咖啡': 55, '拿鐵咖啡': 65, '英式奶茶': 30, '珍珠奶茶': 45,
    '布丁奶茶': 35, '錫蘭紅茶': 20, '多多綠茶': 30, '海鹽清茶': 45, '芒果冰沙': 65 }

# 在腦海中想像一般在訂飲料的情形，會傳一張紙，
# Rita: 美式黑咖啡一杯 多多綠茶兩杯
# Alex: 錫蘭紅茶三杯 甘蔗清茶一杯
# 思考一下這是什麼結構呢?
# Hint 1:   這張紙上只會出現一個 Rita
# Hint 2:   這個 Rita 可以訂很多種飲料, 重複訂了多多綠茶, 你會寫成「多多綠茶x2」
#           不偏好寫成：「多多綠茶、多多綠茶」

bookingNote = {}
bookingNote['Rita'] = {'美式黑咖啡': 18, '多多綠茶': 2}
bookingNote['Alex'] = {'錫蘭紅茶': 3, '甘蔗清茶':1}
bookingNote['momo'] = {'多多綠茶':5}
bookingNote['lulu'] = {'招牌咖啡':1, '布丁奶茶':1}
bookingNote['mango'] = {'珍珠奶茶':1}
print('訂購單資料如下')
print(bookingNote)

# 紀錄每個人要付多少錢的字典
eachPayment = {}

# 收錢股長先算出每個人要付多少錢
for person, booked in bookingNote.items():
    # 當你看到常常一串名單不知道有多少人的時候
    # 你會一行一行讀，一次算一個人的錢
    # 所以這一個迴圈要先把問題從 收很多人訂飲料的錢
    # 切割成每一個人應該要收多少錢，所以一個人頭一個人頭算
    # 把長長的 A4 紙名單 bookingNote 切開變成某人和某人所訂購的飲料細項 person, booked
    print('===== 開始點餐 =====')
    currentPayment = 0
    for drinkName, num in booked.items():
        if drinkName in drinkPrice:
            currentPayment += drinkPrice[drinkName] * num
            print('{} 點了 {} 杯 {} ({}/杯)'.format(person, num, drinkName, drinkPrice[drinkName]))
        else:
            print('{} 點了菜單裡面沒有的 {}'.format(person, drinkName))
    # 算完這個人的錢之後<把他的名字和價錢 顯示出來 並且 記錄起來
    print('{} 需付 {} 元'.format(person, currentPayment))
    eachPayment[person] = currentPayment

# 寫到這邊先印出 eachPayment 檢查看看資料是否正確 然後再接續寫下去    
print('----- Debug -----')
print(eachPayment)

# 計算有沒有達到打折的部分 ...
# sum 來計算大家總共花了多少錢
sum = 0
for p in eachPayment.values():
    sum += p

if sum >= 300:  # 最後總價打八折的緣故 因此可以拿到兩成的回扣
    print('收回扣 {} 元'.format( 0.2 * sum))
else:   # 未滿三百塊
    print('還差 {} 元才可以享有八折優惠'.format( 300 - sum ))
    
''' 
basket = {}
nameque = []

nameque.append('momo')
nameque.append('mango')
nameque.append('rita')
nameque.append('alex')
nameque.append('lulu')

basket['招牌咖啡'] = 1
basket['英式奶茶'] = 1
basket['珍珠奶茶'] = 1
basket['芒果冰沙'] = 1
basket['木瓜牛奶'] = 1

sum = 0
for k,v in basket.items():
    if k in drinkPrice.keys():
         for i in range(len(nameque)):
            print ( '飲料名稱: {}, 飲料數量: {} 杯, {} 須付金額: {} 元'.format(k, v, 
                nameque[i], drinkPrice[k] * v ))
            sum = sum + drinkPrice[k] * v 
print('總金額: {} 元'.format(sum))

if sum >= 300:
    sum = sum*0.8
    print('滿300元打8折後是 {} 元'.format(sum))
else:
    sum < 300
    sum = 300 - sum    
    print( '還差{}元滿300元'.format(sum) ) 
'''