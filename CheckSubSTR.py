def isSub(x,y):
    t=0
    for i in y:
        if i in x:
            t+=1
        else:
            t-=1
    if t==len(y):
        return True
    else:
        return False

s=input("Enter a String: ")
c=input("Enter another string which is to be checked for in the above String: ")
if isSub(s,c):
    print("The String",c,"is a sub-string of the String:")
    print(s)
else:
    print("The String",c,"is not a sub-string of the String:")
    print(s)

