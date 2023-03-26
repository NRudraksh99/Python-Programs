from googlesearch import search
q=input("Enter your Query: ")
for i in search(q,tld='co.in',num=10,stop=10,pause=2):
    print(i)

