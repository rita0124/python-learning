# 參數吃進一個數字 代表攝氏溫度 他是數字 可能會有小數點
# 函式裡面進行運算
# 把期望的華氏溫標數值 作為是函式的回傳值 他也會是個數字 可能會有小數點
# 加分項目: 為了避免使用者智障 丟入不符合預期的內容
# 試圖造成程式崩潰 因此可以針對輸入的參數進行檢查 (請參考老師的教學範例二 tripple_string)

def transCtoF(c): 
    return c * 9 / 5 + 32
  
def transFtoC(f):
    return ( f - 32 ) * 5 / 9

print('We\'re going to transfer C deg to F deg')
cDeg = float(input('Cexxx Degree: '))
fDeg = transCtoF(cDeg)
print('Afetr transformation, the F degree is {}'.format(fDeg))