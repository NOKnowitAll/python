# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


while True:
    ip = input('IP-адрес в формате 10.0.1.1: ')
    octets=ip.split(".")
    ipadress = True
    print(octets)

    if len(octets) == 4:
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                ipadress = False
                break
    else:
        ipadress = False

    if ipadress:
        break
    print("Неправильный IP-адрес")

    

ip1 = int(ip.split('.')[0])


if ip == "255.255.255.255":
    print('local broadcast')
elif ip == "0.0.0.0":
    print('unassigned')
elif 1 <= ip1 <= 223:
    print('unicast')
elif ip1 >= 224 and ip1 <= 239:
    print('multicast')
else:
    print('unused')

