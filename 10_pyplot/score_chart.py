# 寫一支程式計算小明 八次小考成績
# 身為小老師的你 為了方便計算平均 所以必須採用 numpy 所提供的方法
# 因為全班考試分數都很悲劇 所以老師大發慈悲 讓同學可以採最高分的五次取平均
# 畫成折線圖 觀察他的成績波動

import numpy as np
import matplotlib.pyplot as plt

score = [32, 54, 61, 58, 87, 66, 93, 82]
avgScore = np.mean(score)
print('小明八次小考的得分: ', score)
print('小明八次小考的的平均分數: ', avgScore)

tmpScore = score.copy()
highScoreList = []
for i in range(5):
    highestScore = np.max(tmpScore)
    highScoreList.append(highestScore)
    tmpScore.remove(highestScore)
    
print('小明最高的五次: ', highScoreList)
highAvgScore = np.mean(highScoreList)
print('小明最好五次小考的的平均分數: ', highAvgScore)

plt.figure()
plt.title('小明小考得分曲線圖')
plt.xlabel('小考次別')
plt.ylabel('得分')
plt.plot( range(1,9), score)  # 若在呼叫 plot 畫圖函式時候 只給一組數值 則資料會當成各組數值的 y, x 會從 0 開始算
plt.axis([1, 8, 0, 100])
plt.grid()
plt.savefig('小明得分曲線圖')
plt.show()