# 字符串格式化：完成版
# 3.3.1 简单转换
price = 'Price of eggs: $%d' % 42
print(price)
# 改成不带符号的十六进制（小写）
price = 'Hexadecimal price of eggs: %x' %42
print(price)
# 转换成十进制浮点数
from math import pi
p = 'Pi: %f' %pi
print(p)

# ---------------------

# 3.3.2 字段宽度和精度
# 字段宽是10
p = 'Pi: %10f' % pi
print(p)
# 字段宽是8，精度是2
p = 'Pi: %8.2f' % pi
print(p)
# 精度是20
p = 'Pi: %.20f' % pi
print(p)
# 可以使用*（星号）作为字段宽度或者精度 宽度是10，精度是2
p = 'Pi: %*.*f' % (10,2,pi)
print(p)

# ----------------------

# 3.3.3 符号、对齐和用0填充
# 用0填充
p = 'Pi: %010.2f' % pi
print(p)
# 减号（-）左对齐
p = 'Pi: %-10.2f' % pi
print(p)
# 空白（“ ”）就是在前面留白
p = 'Pi: % 2.2f' % pi
print(p)
# 加号（+）不论是整数还是负数都显示符号
p = '%+5d' % +10 + '\n' + '%+5d' % -10
print(p)

# -----------------------

# 字符串格式化演示

width = int(input("Please enter width:"))

price_format = 10
item_width = width-price_format

header_format = '%-*s%*s'
format1 = '%-*s%*.2f'

print('=' * width)

print(header_format % (item_width,'Item',price_format,'Price'))

print('-' * width)

print(format1 % (item_width,'Apples',price_format,0.7))
print(format1 % (item_width,'Beer',price_format,1.7))
print(format1 % (item_width,'Juice',price_format,7.7))
print(format1 % (item_width,'Orange',price_format,0.3))
print(format1 % (item_width,'Watermelon',price_format,0.6))

print('=' * width)