# coding=gbk
#__author__ = 'wooluo'
spath="E:/PY/baa.txt"
n="10"
# Opens file for writing.
#Creates this file doesn't exist.
f=open(spath,"w")
f.write("First line 1.\n")
f.writelines("First line 2.\n")
f.writelines("First line 3.\n")
f.writelines("First line 4.\n")
f.writelines("First line 5.\n")
f.writelines("First line 7.\n")
f.writelines("First line 8.\n")
f.writelines("First line 9.\n")
f.close()
f=open(spath,"r") # Opens file for reading
for line in f:
    print(line)
f.close()