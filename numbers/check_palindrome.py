num = int(input('enter your number:'))
result =0
original_num = num

while num>0:
    ld = num%10
    result = (result*10)+ld
    num = num//10
    
if original_num==result:
    print("your number is a palindrome")
else:
    print("your number is not a palindrome")