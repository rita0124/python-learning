tixque = []  # tix que means, ticket queue

# 使用 List 的內建方法 append 增加內容
tixque.append('Rita')

# 在隊伍中增加一個人 'Terry'
tixque.append('Terry')
tixque.append('momo')

# 秀出 List 的內容
print('隊伍中共有 {} 人'.format( len(tixque) ))
print(tixque)

tixque.reverse()
print(tixque)

tixque.insert(0, 'mango')
print(tixque)