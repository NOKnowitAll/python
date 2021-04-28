# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vv=input('ввод номера VLAN: ')
mac_table =[]
file = open('CAM_table.txt', "r")
for line in file:
    line = line.split()
    if line and line[0].isdigit() and line[0] == vv:
        vlan, mac, _, interface = line
        print(f"{vlan:<9}{mac:20}{interface}")   


