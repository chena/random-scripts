# -*- coding: utf-8 -*-

members = [] ## names
amounts = [] ## amount balance

values = sorted(map(list, zip(members, amounts)), key=lambda t: t[1])
start, end = 0, len(members) - 1

while start < end:
    ower, owed = values[start]
    payer, paid = values[end]
    if paid >= abs(owed):
        print(u'{} pays {} ${}'.format(ower, payer, abs(owed)))
        values[start][1] = 0
        values[end][1] = paid + owed
        start += 1
    else:
        print(u'{} pays {} ${}'.format(ower, payer, paid))
        values[start][1] = paid + owed
        values[end][1] = 0
        end -= 1colleges