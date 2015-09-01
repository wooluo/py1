# coding=gbk
#__author__ = 'wooluo'
#filename:while.py

number = 23
running = True

while running:
    guess = int(input('Enter an integer :'))
    if guess == number:
        print('恭喜，猜对了')
        running = False
    elif guess < number:
        print('这个数小了')
    else:
        print('这个数大了')

print('程序完成')