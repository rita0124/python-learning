# 平均速率(average speed)
# 一段時間delta_t內，質點所走的路徑長delta_L和delta_t的比值

def s_avg(delta_L, delta_t):
    s_avg = delta_L / delta_t
    return (s_avg)

s_avg = s_avg(100, 10)
print('平均速率: ' + str(s_avg) + ' (m/s)')


# v1：初速度（m/s或cm/s）、v2：末速度（m/s或cm/s）、a：加速度（m/s2或cm/s2）