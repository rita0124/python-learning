# 製作一個簡單的函式
# 他唯一的功能就是在螢幕上印出打招呼文字
def say_hello():
    print('是在Hello')
    print('義大利中文哥很雞掰')
    print('上廁所不洗手')
    print('垃圾亂丟')
    print('馬惹發科')
    # Python 的函式允許結束時 可以不回傳任何東西

# 製作第二個函式
# 在參數輸入一個字串
# 在螢幕印出三倍字串
# 如果成功印出字串 則回傳 布林值 True
# 如果輸入的參數不是字串 顯示警告訊息之後 回傳 布林值 False
def tripple_string(message):
    if type(message) != type(''):
        print('警告: 輸入參數不是字串')
        print(message)
        print(type(message))
        return False    # 一旦 17 行條件成立，並且執行到 21 行的 return 後，就會在行結束函式
    # 因為所有不是字串輸入的例外狀況 都會在前面被阻擋掉 並且 return
    # 所以可以執行到下面這行程式碼 而沒有提在前面被 return 結束函式運作
    # 表示所輸入的參數是字串 也就不必再多做一次檢查 (不用檢查 message == type('') )
    print( message * 3 )
    return True

# Python 的函式 可以在函式結束時 回傳任何內容
# 我們在製作這個函式時 取名叫做 add_two_num 意思是 希望傳入兩個數 做相加之後 得到答案
# 例如 add_two_num(8, 9) 可以得到 17
# 例如 add_two_num(123, 12) 可以得到 135
def add_two_num(x, y):  # x 是函式的第一個參數 y 是函式的第二個參數
    print('Add {} and {}'. format(x, y))
    # 於是 我們在下面這一行來作加法運算
    ans = x + y
    
    # return 這是一個關鍵字 可以出現在函式區塊中的任何地方
    # 一旦函式進行 return 之後 函式便會結束在該行
    # 並且在函式被結束的前一刻 將指定的東西回傳給呼叫者/呼叫函式的地方
    return ans
    
# 以上我們定義 define 函式
# 並且實作 implement 函式
# 所以我們可以在定義實作函式之後 進行 「呼叫函式」 ( Call Function ) 

# 範例一: 直接呼叫 say_hello() 來達到在螢幕上輸出先前所定義好的字串
# 因為打招呼的文字很多行 不可能每次都在重寫那五行程式 太麻煩
# 直接呼叫函式 省時省力
# print('\n第一次看到中文哥，來跟她打招呼\n\n')
# say_hello()
#print('\n第二次看到雞巴人，來跟她打招呼\n\n')
#say_hello()


# 範例二: 輸出三倍字串
# 因為我們在設計函式的時候，定義了  return 布林值 True 或 False 來代表成功或失敗
# 在函式結束實，有回傳值的情況下
# 我們要定義一個變數來承接 function 的 return value
result = tripple_string('義大利人都去吃大便!!') # 使用字串作為函式的參數
print('三倍字串成功與否? {}'.format(result))

result = tripple_string(9487)   # 使用整數 9487 作為此函式的參數
print('三倍字串成功與否? {}'.format(result))


# 範例三: 使用我們自訂的 add_two_num() 函式來做期望的事情
luckyNumber = add_two_num(9478, 5566)
print('神秘數字: {}'.format(luckyNumber))

