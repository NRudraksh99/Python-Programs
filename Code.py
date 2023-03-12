import cv2
from io import BytesIO
from pyzbar.pyzbar import decode
from barcode import EAN
from barcode.writer import ImageWriter as iw
from os import path,listdir

def BarCodeCreator(x):
    with open(path.join("Codes",(x+".jpg")),"wb") as f:
        EAN(x,writer=iw()).write(f)
    print("Code Successfully Generated!")

def Reader(image):
    img=cv2.imread(image)
    r=decode(img)
    if not r:
        print("Invalid Barcode...")
    else:
        for i in r:
            (a,b,c,d)=i.rect
            cv2.rectangle(img,(a-10,b-10),(a+c+10,b+d+10),(255,0,0),2)
            if i.data!="":
                print("Data in the barcode is:")
                print(int(i.data,10))

d=listdir("Codes")
ch=0
while ch!=3:
    print('''\n\n----> Welcome to the Barcode Reader <----
1) Generate new Barcode
2) Decode Existing Barcode
3) Exit
''')
    ch=int(input("Enter the Number Corressponding to your choice: "))
    if ch==1:
        n=int(input("Enter 12-digit Barcode Number: "))
        BarCodeCreator(str(n))
    elif ch==2:
        for i in range(len(d)):
            print(f"{i+1}) {d[i]}")
        n=int(input("Enter the Number Corresponding to your choice: "))
        Reader(path.join("Codes",d[n-1]))
    elif ch==3:
        print("Thanks for using this program! Bye!!")
        break
    else:
        print("Invalid Choice...")

