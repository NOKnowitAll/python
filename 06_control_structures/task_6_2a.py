# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ipadress = True
ip = input('IP-адрес в формате 10.0.1.1: ')
octets=ip.split(".")
print(octets)
if len(octets) != 4:
    ipadress = False
else:
    for octet in octets:
        if not (octet.isdigit() and int(octet) in range(256)):
            ipadress = False
            break


if not ipadress:
    print("Неправильный IP-адрес")
else:
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

