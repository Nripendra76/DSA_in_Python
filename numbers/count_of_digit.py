count = 0
num = int(input("enter you number:"))

# while num>0:
#     last_digit = num%10
#     num=num//10
#     count=count+1
    
# print(f"your number contain {count} digit ")

from math import *
def count_digit(num):
    return int(log10(num)+1)
print(count_digit(num))