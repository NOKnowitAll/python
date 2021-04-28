# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf = ospf_route.replace(',', ' ').replace('via', ' ').replace('[', '').replace(']', '').split()

prefix = ospf[0]
metric = ospf[1]
nexthop = ospf[2]
update = ospf[3]
outintf = ospf[4]

maska = '''
Prefix               {:15}   
AD/Metric            {:15} 
Next-Hop             {:15}
Last update          {:15}
Outbound Interface   {:15}
'''  

print(maska.format(prefix, metric, nexthop, update, outintf))






