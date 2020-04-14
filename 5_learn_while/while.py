# 計算 1 加到 10 的總和，使用 while 和 for 迴圈

n = 0
sum = 0
# while 條件:
while n < 10:     
    n = n + 1
    sum = sum + n
       
print(sum)

n = 1
sum = 0
while n <= 10:      
    sum = sum + n
    n = n + 1
       
print(sum)

sum = 0
# for 變數名稱 in 串列或字串:
for n in range(1,11):   
    sum = sum + n
    
print(sum)


# 輸入數字不是 0，輸入數字不是 0，顯示該數字的平方，使用 while 迴圈

 
while int(n) != 0:
    n = input('請輸入數字: ')
    print( '數字的平方: ' + str (int(n)**2))
else:
    print('False')
        
    

   