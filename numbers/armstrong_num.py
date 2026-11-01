num = int(input('enter your num:'))
nod = len(str(num))
total = 0
original_num = num

while num>0:
    last_digit = num%10
    total = total+(last_digit**nod)
    num=num//10
if total == original_num:
    print("armstrong")
else:
    print('not armstrong')
    