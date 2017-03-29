# -*- coding: utf-8 -*-
import sys
import os
import os.path
import shutil
import re

configPath = os.path.join((sys.path)[0], "file")
processPath = os.path.join((sys.path)[0], "XMLFile")
#删除
if os.path.exists(processPath):
        shutil.rmtree(processPath)
#新建
os.mkdir(processPath)
#处理全部文件
for parent, dirnames, filenames in os.walk(os.path.join((sys.path)[0], "file")):
	#print "dirnames:" + dirnames
	#print (filenames)
	for filename in filenames:
		fileType = filename[len(filename)-4:len(filename)]
		if fileType == '.txt':  #只处理txt文件
			targetFileName = filename[:len(filename)-3] + "xml"
			os.system('python ./transXML.py ' + os.path.join(parent, filename) + " " + os.path.join(processPath, targetFileName))
						