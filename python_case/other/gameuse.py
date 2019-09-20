


# ans = 0
#
# while ans == 0:
#     num = input("ans: ")
#     if num == ("1"):
#         print ("ture", num)
#
#     else :
#         print("try again")
#

# print("good bye")




# print("我现在要写一个文件数字猜游戏数字游戏：")
# temp=input("请你输入一个数字，猜对了有奖，猜错了，没有关系：")
# guess=int(temp)
#
#
# while guess != 8:
#         temp=input("还没有猜对，继续猜猜看，不要放弃：")
#         guess=int (temp)
#
#         if guess == 8:
#          print("你猜对了！")
#
#         else:
#             if guess > 8:
#                 print("数字猜大了！")
#             else:
#                 print("数字猜小了")
import re

float_number = str(input('Please input the number:'))

value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

result = value.match(float_number)

if result:
    print ("Number is a float.")

else:
    print ("Number is not a float.")