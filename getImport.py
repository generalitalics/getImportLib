__autor__ = 'm.shoshin'

# -*- coding: utf-8 -*-

import os
import re
import sys
import shutil

from datetime import datetime

comp = re.compile(r'import (\S+?)\s')
comp1 = re.compile(r'from (\S) import \S+?\s')
p = []
dictLog = {}
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
data = None
# with open(source) as f:
#     lines = f.readlines()



if not os.path.exists(res_dir):
    os.makedirs(res_dir)

print('\nOK')
# сколько выполнялась это чудесная програмуля
time_end = datetime.now()
time_delta = time_start - time_end
print("Total time: %d s" % -time_delta.total_seconds())
