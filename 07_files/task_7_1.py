# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
file = open('ospf.txt', 'r')
mask = """
Prefix                {0:}
AD/Metric             {1:}
Next-Hop              {2:}
Last update           {3:}
Outbound Interface    {4:}
"""

for line in file:
    line1 = line.replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    print(mask.format(line1[1], line1[2], line1[4], line1[5], line1[6]))
    


    



    


    

