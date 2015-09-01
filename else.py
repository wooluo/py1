# coding=gbk
#__author__ = 'wooluo'
#Mult-way decision
x=int(input('Please enter aninteger:'))
if (x<0):
    x=0
    print('Negative changed to zero')
elif x==0:
    print ('Zero')
else:
    print('More')

#   Loops List
a=['cat','windows','defenestrate']
for x in a:
    print (x,len(x))
