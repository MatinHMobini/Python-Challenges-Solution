#Q6
import math
import statistics 
n = int(input('Enter a postive integer for how many numbers you want'))
nums = []
medianlist = nums
numsmode = nums
numscount = []
modeanswer = []
ihold = []
for i in range(0 , n):

    num = float(input('Enter any real number'))
    nums.append(num)


avg = (sum(nums)) / n

rangeofnums = (max(nums)) - (min(nums))

medianlist.sort()
p = len(nums)
if p % 2 == 0:
    median = (medianlist[int((p/2)-1)] + (medianlist[int(p/2)])) / 2

if p % 2 != 0:
    median = (medianlist[int(p/2)])


u = 0
for k in nums:
    if numsmode.count(k) > 1:
        numscount.append(numsmode.count(k))
        ihold.append(numsmode.index(k))
        numsmode.remove(k)
        u = u + 1
if u == 1:
    mode = True
    m1 = numsmode[ihold[0]]
    modeanswer.append(m1)
    print('The mode is:', modeanswer)
if u > 1:
    if numscount[0] == numscount[1]:
        modes = True
        ms1 = numsmode[ihold[0]]
        ms2 = numsmode[ihold[1]]
        modeanswer.append(ms1)
        modeanswer.append(ms2)
        print('The modes are',modeanswer)

    if numscount[0] > numscount[1]:
        mode = True
        m1 = numsmode[ihold[0]]
        modeanswer.append(m1)
        print('The mode is:', modeanswer)

    if numscount[0] < numscount[1]:
        mode = True
        m2 = numsmode[ihold[1]]
        modeanswer.append(m2)
        print('The mode is:', modeanswer)

    
print('The average is:', avg)
print('The Range is:', rangeofnums)
print('The median is:', median)

