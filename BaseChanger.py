from sys import exit
def Convert(x,b):
    t=str(x)
    y=0
    for i in range(len(t)):
        p=b**i
        if b!=16:
            y+=((float(t[::-1][i]))*p)
        else:
            y=int(t,16) 
    return y

q=0
print("Welcome to the Number base Converter!")
while q!=2:
    print('''\n
    -------> Main Menu <-------
    1) Convert
    2) Exit
    ''')
    q=int(input("Enter the Number Corresponding to your Choice: "))
    if q==1:
        print('''-----> Input type <-----
    1) Binary
    2) Octal
    3) Hexadecimal
    ''')
        c1=int(input("Enter the Number Corresponding to your choice: "))
        if c1==1:
            z=int(input("Enter the Binary Number: "))
            print(z,"in Binary =",Convert(z,2),"in decimal")
        elif c1==2:
            z=int(input("Enter the Octal Number: "))
            print(z,"in Octal =",Convert(z,8),"in decimal")
        elif c1==3:
            z=input("Enter the Hexadecimal Number: ")
            print(z,"in Hexadecimal =",Convert(z,16),"in decimal")
        else:
            print("Invalid Choice...")
    elif q==2:
        print("Bye!")
        exit()
    else:
        print("Invalid Choice...")

