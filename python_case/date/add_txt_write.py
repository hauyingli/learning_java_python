# * coding:utf 8 *


f = open("Label.txt",'a')
# 读取label.txt文件，没有则创建，‘a’表示再次写入时不覆盖之前的内容

f.write("你好")
f.write('\n')
f.write("www")
f.write('\n')
f.close()