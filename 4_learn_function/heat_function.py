''# 寫出第一個函式，接受三個參數，回傳熱容量
# 寫出第二個函式，卡轉焦耳的函式

def heat_capacity(m, s, deltaT):
    heat = m * s * deltaT
    return heat
            
def cal_trans_J(cal):
    joule = cal * 4.184 
    return joule

heat = heat_capacity(100, 1, 10)
# print(H)
joule = cal_trans_J(heat)
print( '熱容量 ' + str(joule) + ' 焦耳' )