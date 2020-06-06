import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
## 建立一個預測披薩價格的數學模型
## 先訓練資料 也就是從已知價格的披薩尺寸調整 model
'''
Training Instance   |   Size    |   Price
---------------------------------------------
    1               |   6       |   80
---------------------------------------------
    2               |   8       |   99
---------------------------------------------
    3               |   10      |   150
---------------------------------------------
    4               |   14      |   180
---------------------------------------------
    5               |   18      |   220
    
'''
######  建模階段  ######
## 使用 大寫X 來表示 訓練資料中的解釋變數
## numpy 的 array reshape 掛兩個參數 表示切成二為矩陣
## row 代 -1, col 代 1 表示切成 1 col 的 matrix
X = np.array([[6], [8], [10], [14], [18]]).reshape(-1, 1)
y = [80, 99, 150, 180, 220]

plt.figure()
plt.title("披薩尺寸價格關係圖")
plt.xlabel("直徑 Size (inches)")
plt.ylabel("價格 Price (元)")
plt.plot(X, y, 'k.')
plt.axis([0, 25, 0, 300])
plt.grid()
# plt.show()

# 設定機器學習所使用的數學模型 model 為 線性迴歸模式
model = LinearRegression()
# 訓練資料帶進 model
model.fit(X, y)


######  預測階段  ######
# 假設未來將會推出兩種新尺寸，分別為 13 和 17 吋
# 因此令 X_new_pizza 為未來將會推出的披薩尺寸
# 並採用 透過先前訓練資料 所訓練出來的披薩尺寸對應價格預測模型 model 中
# 將所猜測出來的價格 放到 y_guess_price
X_new_pizza = np.array([[13], [17]])
y_guess_price = model.predict(X_new_pizza)
# 將猜測出來的兩個價格，標在原本的分布圖中
plt.plot(X_new_pizza, y_guess_price, '*', color='g')

# 列出所猜測的價格
for r in range(len(X_new_pizza)):
    print('未上市的披薩尺寸: ', X_new_pizza[r][0], ' ---> 預測價格: ', y_guess_price[r])


######  評價模型  ######
# 俗話說海水退了就知道誰沒穿褲子
# 所以要知道這個預測模型準不準確
# 到底是嘴砲成分多呢? 還是真的很神準呢?
# 於是我們會在最後知悉新產品上市後的價格時 來評價模型得分

# 在統計學中，我們會以 差平方總和 (R Square) 進行扣分... 零誤差就零扣分, 誤差越多扣越多
# 幾何意義就是 把每一筆預測價格和實際價格的誤差取平方之後加總起來
# 有那麼點計算距離的感覺

# 根據先前鐵口直斷 預測
# 未上市的披薩尺寸:  13  ---> 預測價格:  166.88793103448276
# 未上市的披薩尺寸:  17  ---> 預測價格:  213.75
# 那麼如果 13 吋最後上市的價格落在 170 元; 17 吋的 219 元
y_real_price = [170, 219]
r_square = model.score(X_new_pizza, y_real_price)
print('預測模型得分: ', r_square)
# 預測模型得分:  0.9689733667254181

# 這個線性迴歸的預測方式優缺點
# 建模的時候 因為要不斷地去找出一條最靠近所有點的線性方程式 所以會花很多時間建模型 (缺點)
# 但是 在預測時 只需要將特徵帶入先前建好的模型中 即可很快速地得到預測結果 (優點)
# 致命缺陷是 "數多必有枯枝 人多必有白癡" (缺點，以下實例說明)

# 如果有個違背市場機制的傻人老闆 用很便宜價格 去販售 巨無霸披薩
# 抑或是有個黑心商人 小披薩賣超貴
# 要是出現在 訓練資料中 那會導致數學模型失準
# 要是出現在 預測資料中 因為違背常理所以測不準，還會使數學模型得分下降
# 我們假設那個老闆賣 4 吋 290 元; 22 吋 88 元
X_kerker_pizza = np.array([[4], [22]])
y_tricky_price = [290, 88]
plt.plot(X_kerker_pizza, y_tricky_price, 'x', color='r')
socre_kerker = model.score(X_kerker_pizza, y_tricky_price)
print('預測偏離群體的披薩價格得分: ', socre_kerker)


# 將分布圖儲存起來
plt.savefig("pizza_price_fig.png")
# 在銀幕上看看結果    
plt.show()