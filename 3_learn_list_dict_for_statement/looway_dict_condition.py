滷味菜單 = {
    '王子麵': 15, '雞心': 20, '豆干': 10, '甜不辣': 15, '火鍋料': 15, '空心菜': 30, 
    '百頁豆腐': 30 }

飲料菜單 = {
    '美式黑咖啡': 15, '招牌咖啡': 55, '拿鐵咖啡': 65, '英式奶茶': 30, '珍珠奶茶': 45,
    '布丁奶茶': 35, '錫蘭紅茶': 20, '多多綠茶': 30, '海鹽清茶': 45, '芒果冰沙': 65  }

order = {}
order['momo'] = { '王子麵': 1, '雞心': 2, '火鍋料': 5, '珍珠奶茶': 1 }
order['mango'] = { '豆干': 3, '甜不辣': 1, '火鍋料': 2, '空心菜': 1, '酸梅湯': 1 }
order['lulu'] = { '王子麵': 1, '雞心': 1, '豆干': 1, '百頁豆腐': 1, '錫蘭紅茶': 1, '海鹽清茶': 1 }

for name, eachOrder in order.items():
    sum=0
    print('開始計算購買者: {}'.format(name))
    for food, num in eachOrder.items():
        if food in 滷味菜單.keys():
            sum += 滷味菜單[food] * num
            print('加入滷味: {} x {} 個 = {} 元'.format( food, num,  滷味菜單[food] * num))
        if food in 飲料菜單.keys():
            sum += 飲料菜單[food] * num
            print('加入飲料: {} x {} 杯 = {} 元'.format( food, num,  飲料菜單[food] * num))
    print('這個人要付 {} 元'.format(sum))