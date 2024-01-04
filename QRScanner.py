from cv2 import VideoCapture as vc
from cv2 import QRCodeDetector as qr
from cv2 import imshow as im
from cv2 import waitKey as wk
from cv2 import destroyAllWindows as daw
from webbrowser import open as op

def qrscan():
    while True:
        _,img=cam.read()
        im('Webcam', img)
        if wk(1) & 0xFF == ord('q'):
            break
        data,box,_=scan.detectAndDecode(img)
        if data:
            break
    cam.release()
    daw()
    return data

cam=vc(0)
scan=qr()

print("Press 'q' anytime to quit scanning!")
l=qrscan()

if str(l)!="":
    print("Link/Resource found in the scanned QR:",str(l))
    a=input("Enter '1' to open the link, or any other key to exit: ")
    if a=="1":
        op(str(l))
    else:
        print("Thanks for using this program! Bye!!")
else:
    print("No QR code was found....")
