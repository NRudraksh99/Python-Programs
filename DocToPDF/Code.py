from os import path,listdir
from docx2pdf import convert
from sys import exit

c=0
x=listdir("Documents")
print('''Welcome to Document to PDF Converter!
To Convert your Documents, make sure they are present in the 'Documents' Folder!''')
while c!=2:
    print('''
1) Convert .docx file into .pdf
2) Exit
''')
    c=int(input("Enter the Number Corresponding to your choice: "))
    if c==1:
        print('The Files Currently in the Folder are:')
        for i in x:
            print(x.index(i)+1,i)
        y=int(input("\nEnter the Number Corresponding to your choice: "))
        n=i.split(".")[0]+".pdf"
        try:
            convert(path.join("Documents",x[y-1]),path.join("PDFs Created",n))
            print("Conversion Successfully Completed, file has been save in the 'PDFs Created' Folder")
        except:
            print("Oops! Some Error Occured...")
    elif c==2:
        print("Thank you for using this Program! Bye!!")
        exit()
    else:
        print("Invalid Choice... Please try again.")
    
