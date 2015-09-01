# coding=gbk
#__author__ = 'wooluo'
a = ['cat', 'window', 'defenestrate']
for x in a:
    print(x, len(x))
for x in a[:]: #make a slie copy of the entire list
    if len(x) > 6:  a.insert(0, x)
