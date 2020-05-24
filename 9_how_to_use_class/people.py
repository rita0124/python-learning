class People:
    name = ''
    money = 0

    #  在以 People類別 實作出各個物件時(下方幾個人的誕生)，預設會被呼叫的函式
    #  以物件導向程式設計的觀念來說，這是一個「建構子函式」(constructor function)
    #  憲法第一條規定，如果出生時不取名字的話 就會被稱為無名氏
    #  憲法第二條規定，任何人出生的時候，如果沒有錢，就會得到一百元
    def __init__(self, n = '無名氏', m = 100):
        self.name = n
        self.money = m
        
    #  來實作第一個 function: 嘛嘛砸摳~
    #  每一個小孩子都會跟媽媽要錢, 成功的話 錢就會多十塊
    def ask_mama_ten_dollar(self):
        self.money = self.money + 10
