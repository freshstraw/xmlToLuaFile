# -*- coding: utf-8 -*-
import sys
import codecs
import os

path = (sys.argv)[1]
target = (sys.argv)[2]
#print path
#print target

#加载文件
with codecs.open(path, "r", "gbk") as f:
		txt = f.readlines()
#拆分类型
types = txt[0].replace('\r\n','').split("\t")
#拆分参数
fields = txt[1].replace('\r\n','').split("\t")

fileContent = "<?xml version=\"1.0\" encoding=\"utf-8\"?> \n"
fileContent += "<root> \n"
#分发参数数据
x = 2
txtFile = ""
content = ""
while x < len(txt):
	if txt[x][0] != "#":
		elements = txt[x].replace('\r\n','').split("\t")
		squ = 0
		content = "\t<data_node\n"
		while squ < len(fields):
			content += "\t\t" + fields[squ] + " = \"" + elements[squ] + "\"\n" 
			squ += 1
		content += "\t/>\n"
		txtFile += content
	x += 1
#写入方法
fileContent += txtFile + "</root> \n"
fileContent.encode('utf-8')	#转换成utf-8格式
with codecs.open(target, 'w', 'utf-8') as f:
    f.write(fileContent)
print "Complete !"
