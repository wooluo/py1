__author__ = 'wooluo'
from _ctypes import *
msvcrt = cdll.msvcrt
message_string = "hello world!\n"
msvcrt.print("Testing:%s",message_string)