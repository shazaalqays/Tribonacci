# tribonacci sequence

# Function Return Tribonacci Sequence
def Rfunc(num):
    if num == 0 or num == 1 or num == 2:
        return 1
    else:
        return Rfunc(num-1) + Rfunc(num-2) + Rfunc(num-3)

num = 5;
if num >= 0:
    for i in range(num):
        print(Rfunc(i));
    print('Recursive Tribonacci ', Rfunc(num));
else:
    print('You entered negative number');