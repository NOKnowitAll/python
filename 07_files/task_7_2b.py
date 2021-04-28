# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]


from sys import argv

fname1 = argv[1]
fname2 = argv[2]
lines2 = []

file2 = open(fname2, 'w')

with open(fname1, 'r') as file:
    for line in file:
        if not line.startswith('!'):
            if line.find(ignore[0]) is -1 and line.find(ignore[1]) is -1 and line.find(ignore[2]) is -1:
                lines2.append(line.rstrip() + '\n')
file2.writelines(lines2)
file2.close()

            
