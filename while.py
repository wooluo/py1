# coding=gbk
#__author__ = 'wooluo'
#filename:while.py

number = 23
running = True

while running:
    guess = int(input('Enter an integer :'))
    if guess == number:
        print('��ϲ���¶���')
        running = False
    elif guess < number:
        print('�����С��')
    else:
        print('���������')

print('�������')