import qrcode
from random import randint
from os.path import dirname

p=dirname(__file__)

def QR_Create(d,x):
    qr=qrcode.QRCode(version=1,box_size=15,border=5)
    qr.add_data(d)
    qr.make(fit='True')
    i=qr.make_image(fill_color='black',back_color='white')
    i.save(f"{p}\\QRs Created\\{x}.png")

a=input("Enter the Link for which the QR Code has to be Genrated: ")
b=input("Enter the Name to be used to name the image file created: ")
QR_Create(a,b)
print("QR has been successfully created!!")
