# Tribonacci sequence

# Function Return Tribonacci Sequence
def NRfunc(num):
    # sumlist for storing sequence
    sumlist = []
    for i in range(num):
        if i == 0 or i == 1 or i == 2:
            # sum for summing the sequence
            sum = 1
            sumlist.append(sum)
        else:
            sum = sumlist[i-1] + sumlist[i-2] + sumlist[i-3]
            sumlist.append(sum)
    return sumlist

num = 5
NonRecursive = []
if num >= 0:
    NonRecursive = NRfunc(num)
    for i in NonRecursive:
        print(i)
    if num > 2:
        print('Non-Recursive Tribonacci ', NonRecursive[-1] + NonRecursive[-2] + NonRecursive[-3])
    else:
        print('Non-Recursive Tribonacci ', 1)
else:
    print('You entered negative number')



