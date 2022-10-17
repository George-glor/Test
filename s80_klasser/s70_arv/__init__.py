import sys

nums = sys.argv[1:]
sum = 0

for num in nums:
    sum += float(num)

average = sum/(len(sys.argv)-1)

print("The average of the set is: {}".format(average))