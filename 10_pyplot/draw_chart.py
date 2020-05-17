import numpy as np  # 引入套件庫 numpy 並且予以別名 np
import matplotlib.pyplot as plt  # 引入 matplotlib 的 pyplot 並予以別名 plt

# 令 x 是一個 array (陣列), 其中的數值從 0 ~ 5, 每筆數值間隔 0.1
# 並且令 y 是對陣列中每個數值 取 sin 值 後的陣列
# https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/561623/
x = np.arange(0, 5, 0.1)
y = np.sin(x)

# 以下操作 pyplot 
plt.figure()    # make a figure
plt.title('畫畫圖')  # set the title of this figure
plt.plot(x, y)  # Draw the plot line by using data x and y
plt.xlabel('橫向資料')
plt.ylabel('取賽值')
plt.grid()  # print the grid 格網
plt.savefig('畫畫圖.png')  # 必須在 show 之前存檔 (先存再秀會正常, 先秀再存會存到空白檔案)
plt.show()  # 讓圖顯示出來 (不寫這行無所謂) 
