def Fact(x):
    if x>1:
        x*=Fact(x-1)
    return x

n=int(input("Enter the Number: "))
print("Factorial of",n,"=",Fact(n))
