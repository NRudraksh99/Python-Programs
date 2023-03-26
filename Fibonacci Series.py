def FibTerm(x):
    if x<=1:
        return 0
    elif x==2:
        return 1
    else:
        return FibTerm(x-1)+FibTerm(x-2)

r=int(input("Enter the Range required: "))
print("The Required Fibonacci Series is:")
for i in range(1,r+1):
    print(FibTerm(i),end=' ')
