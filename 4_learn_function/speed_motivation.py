# 平均速率(average speed)
# 一段時間delta_t內，質點所走的路徑長delta_L和delta_t的比值

def s_avg(delta_L, delta_t):
    s_avg = delta_L / delta_t
    return (s_avg)

s_avg = s_avg(100, 10)
print('平均速率: ' + str(s_avg) + ' (m/s)')


# v1：初速度（m/s或cm/s）、v2：末速度（m/s或cm/s）、a：加速度（m/s2或cm/s2）、t:所經過的時間（s）

def v2(v1, a, t):
    v2 = v1 + a * t
    return v2

v2 = v2(0, 10, 2)
print('末速度: ' + str(v2) + ' (m/s)')

# x：t秒內所行的距離（m或cm）、 v1：初速度（m/s或cm/s）、a：加速度（m/s2或cm/s2）、t:所經過的時間（s）

def x_distance(v1, a, t):
    x = v1 * t + 0.5 * a * t**2
    return x

x = x_distance(0, 10, 2)
print('所行的距離: ' + str(x) + ' (m)')

# x：t秒內所行的距離（m或cm）、 v1：初速度（m/s或cm/s）、v2：末速度（m/s或cm/s）、a：加速度（m/s2或cm/s2）

def v2_sqrt(v1, a, x):
    import math 
    v2_sqrt = math.sqrt(v1**2 + 2 * a * x)
    return v2_sqrt

v2_sqrt = v2_sqrt(0, 10, 5)
print('末速度: ' + str(v2_sqrt) + '(m/s)')