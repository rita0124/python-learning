# s = (a+b+c)/2
# A = sqrt[s * (s-a) * (s-b) * (s-c)

# a = 6
# b = 8
# c = 10

# s = (a + b + c)/2
# area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
# print (area)

x1 = int (input('輸入x1: '))
y1 = int (input('輸入y1: '))
x2 = int (input('輸入x2: '))
y2 = int (input('輸入y2: '))
x3 = int (input('輸入x3: '))
y3 = int (input('輸入y3: '))

a = (( x1 - x2 )**2 + ( y1 - y2 )**2)**0.5
print (a)
b = (( x2 - x3 )**2 + ( y2 - y3 )**2)**0.5
print(b)
c = (( x1 - x3 )**2 + ( y1 - y3 )**2)**0.5
print(c)
if ( y1 - y2 )/( x1 - x2 ) != ( y2 - y3 )/( x2 - x3 ) != ( y1 - y3 )/( x1 - x3 ):
    s = (a + b + c)/2
    print(s)
    area = (s * ( s-a ) * ( s-b ) * ( s-c ))**0.5
    print(area)
else:
    print(False)