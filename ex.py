__autor__ = 'm.shoshin'

# f = open('C:/2_strings.py ', 'r', encoding='utf-8')
# print(f.read())
# f.close()

import re
a = []
comp = re.compile(r'import (.+)\n')
p = re.findall(comp, 'import asv\n       sdfdff dsfsdf s df sdf sdfsd\n  f sdfsdf import ewr\n dfgdg')
print(p)
