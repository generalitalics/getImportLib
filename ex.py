__autor__ = 'm.shoshin'
import os
import subprocess
import time
dirName = r'C:\getImportLib'
libName = 'android'
tempName = r'C:\getImportLib\tempLog.txt'
# f = open('C:/2_strings.py ', 'r', encoding='utf-8')
# print(f.read())
# f.close()

# import re
# p = []
# comp = re.compile(r'import (.+)\n')
# p = p + re.findall(comp, 'import asv\n       sdfdff dsfsdf s df sdf sdfsd\n  f sdfsdf import ewr\n dfgdg')
# print(p)
# # p = p.append(re.findall(comp, 'import edfg\n       sdfdff dsfsdf s df sdf sdfsd\n  f sdfsdf import wedf\n dfgdg'))
# dictg = {}
# dictg[1] = 3
# dictg[1] = 4
# print(dictg)
# os.remove(tempName)
if os.path.exists(tempName):
    os.remove(tempName)
with open("C:\getImportLib\search.bat", 'w', encoding='utf-8') as f:
    f.write('@echo off\ncd %s\npip3 search %s>%s\n' % (dirName, libName, tempName))

os.system("C:\getImportLib\search.bat")
# print('!!!', a)
