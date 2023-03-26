from time import sleep
r=input("Enter the String: ")
x=float(input("Enter the time delay: "))
print("Auto-typing animation:\n")
for i in r:
    print(i,end='')
    sleep(x)
