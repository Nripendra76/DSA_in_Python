
## brute force
# result = []
# num = 20

# for i in range(1, num+1):
#     if num % i == 0:
#         result.append(i)
# print(result)

## better solution
# result = []
# num=20
# for i in range(1,num//2):
#     if num%i==0:
#         result.append(i)
# result.append(num)
# print(result)

## optimal solution
from math import sqrt
result =[]
num = 36

for i in range(1,int(sqrt(num))+1):
    if num % i ==0:
        result.append(i)
        if num // i !=i:
            result.append(num//i)
result.sort()
print(result)   