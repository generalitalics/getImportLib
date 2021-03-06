__autor__ = 'm.shoshin'

# -*- coding: utf-8 -*-

import os
import re
import sys
fileName = 'Log.txt'
dirName = r'C:\getImportLib'
libName = 'android'
tempName = r'C:\getImportLib\tempLog.txt'

from datetime import datetime

def tempParse(liblib):
    if os.path.exists(tempName):
        os.remove(tempName)
    with open("C:\getImportLib\search.bat", 'w', encoding='utf-8') as f:
        f.write('@echo off\ncd %s\npip3 search %s>%s\n' % (dirName, liblib, tempName))

    os.system("C:\getImportLib\search.bat")


comp = re.compile(r'import (\S+?)\s')
comp1 = re.compile(r'from (\S) import \S+?\s')

a=[]
p = []
dictLog = {}
temp = []
print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

time_start = datetime.now()

res_dir = os.path.join(".", "for_Lera")
print('Running      : [' + sys.argv[0] + ']')
print('Diectory   : [' + sys.argv[1] + ']')
print('Wait...',)
print()


source = os.path.join(".", sys.argv[1])
#source = sys.argv[1] - путь к файлу


directory = sys.argv[1]
files = os.listdir(directory)
print("Список файлов *.py")
path_f = []
for d, dirs, files in os.walk(directory):
    for f in files:
        path = os.path.join(d, f) # формирование адреса
        path_f.append(path) # добавление адреса в список
# print(path_f)
pyFiles = filter(lambda x: x.endswith('.py'), path_f)
for i in pyFiles:
    print("|   ", '{:<200}'.format(i), "|")
    with open(i, encoding='utf-8') as f:
        try:
            lines = f.readlines()
            dictLog[i] = []
            for line in lines:
                for j in re.findall(comp, line):
                    dictLog[i].append(j)
                for k in re.findall(comp1, line):
                    dictLog[i].append(k)
        except:
            print("Ошибка! Не прочитался файл: ", i)


p = set(p)
print(p)
print(dictLog)

# Записываем лог
os.remove(fileName)
with open(fileName, 'w', encoding='utf8') as f:
    for i in dictLog:
        f.write('Файл [%s]:\n' % i)
        if len(dictLog[i]) == 0:
            f.write('нет библиотек\n')
        else:
            for j in range(len(dictLog[i])):
                f.write('|{:<17}|'.format(dictLog[i][j]))
                if dictLog[i][j] not in temp:
                    tempParse(dictLog[i][j])
                    with open(tempName, 'r', encoding='utf8') as f2:
                        try:
                            lines = f2.read()
                            comp2 = re.compile('(?m)^%s \S+\W+ ([^\n]+)' % dictLog[i][j])
                            a = re.findall(comp2, lines)
                            if a == []:
                                f.write(' нет данных')
                        except:
                            print("Ошибка чтения temp файла")
                    for z in a:
                        f.write('%s @@@ ' % z)
                    f.write('\n')
                    temp.append(dictLog[i][j])
                else:
                    f.write(' <описание библиотеи выше>\n')


if not os.path.exists(res_dir):
    os.makedirs(res_dir)

print('\nOK')
# сколько выполнялась это чудесная програмуля
time_end = datetime.now()
time_delta = time_start - time_end
print("Total time: %d s" % -time_delta.total_seconds())
