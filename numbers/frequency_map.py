frequency_map = dict()
nums = [1,4,6,4,5,8,1,8,2]
for i in range(0,len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]]+=1
    else:
        frequency_map[nums[i]]=1
print(frequency_map)
    