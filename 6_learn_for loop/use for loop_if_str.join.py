# Write a program which will find all such numbers which are divisible by 7 
# but are not a multiple(倍數) of 5,between 2000 and 3200 (both included).
# The numbers obtained should be printed 
# in a comma(逗號)-separated sequence on a single line.

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0: 
    #Python 用單一等號 = 表示指派，連續兩個等 == 號表示相等性
        print(i,end=', ')
        # print預設是印一行，結尾加换行。end=','意思是末尾不换行，加逗號。  
print("\b")

numbers = [str(x) for x in range(2000, 3201) if x % 7 == 0 and x % 5!= 0] #list
print(', '.join(numbers))
# str.join(要連接的元素序列)

