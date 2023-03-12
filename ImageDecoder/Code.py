from stegano import lsb
from os import listdir,path
from sys import exit
from random import randint

def fetch_dir(p):
    l=listdir(path.join(p))
    return l
    

def Encode(i,m):
    s=lsb.hide(i,m)
    s.save(path.join('CodedImages','Encoded_'+str(randint(0,10000))+".png"))

def Decode(i):
    return lsb.reveal(i)

c=0
x=fetch_dir("Images")
y=fetch_dir("CodedImages")
g=1

print('''
------> Welcome to the Image Encoder/Decoder <------
1) Encode an Image
2) Decode an Image
3) Exit
'''
)
c=int(input("Enter the Number Corresponding to your Choice: "))
if c==1:
    print("To encode an image ,place the file in the 'Images' Folder.")
    if len(x)!=0:
        print("\nThe files in the directory are:")
        for i in x:
            print(g,i)
            g+=1
        a=int(input("\nEnter the Number Corresponding to your choice: "))
        if a<len(x) and a>0:
            b=input("Enter the message to be Encoded into the Image: ")
            Encode(path.join("Images",x[a-1]),b)
            print("Image has been Successfully Encoded and Stored in the Folder 'CodedImages'")
        else:
            print("Invalid Choice...")
    else:
        print("Directory is Empty...")
elif c==2:
    if len(y)!=0:
        for i in y:
            print(g,i)
            g+=1
        a=int(input("Enter the Number Corresponding to your Choice: "))
        if a<len(y) and a>0:
            print("The Message Encoded into the Selected Image is: \n",Decode(path.join("CodedImages",y[a-1])))
        else:
            print("Invalid Choice...")
    else:
        print("Directory is Empty...")
elif c==3:
    exit()
else:
    print("Invalid Choice...")



