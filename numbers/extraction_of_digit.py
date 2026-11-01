num = int(input("enter your number:"))

while num>0:
    last_digit = num%10
    print(f'your last digit of {num} is {last_digit}')
    num = num//10