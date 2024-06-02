from time import time,sleep
import calendar
for i in range(1,13):
    print(i)
    sleep(1)
# 遍历 2024 年的每个月
for month in range(1, 13):
    # 调用 calendar.month() 函数并打印返回的字符串
    print(calendar.month(2024, month))
    # 如果你希望在每个月的日历之间有一些空行分隔，可以添加 print('\n')
    print('\n' * 2)  # 打印两个空行作为分隔



