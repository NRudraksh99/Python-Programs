from bs4 import BeautifulSoup as bs
from requests import get
from os.path import dirname
from json import dump

d={}
p=dirname(__file__)
x=input("Enter the link: ")
name=input("Enter the name to be used for the resultant JSON file (without '.json' extension): ")
result=get(x)
if result.status_code==200:
    soup_result=bs(result.content,'html.parser')
    d["text"]=soup_result.get_text()
    d["links"]=[i.get("href") for i in soup_result.find_all("a",href=True)]
    d["images"]=[i.get("src") for i in soup_result.find_all("img",src=True)]
    with open(f"{p}\\JSON\\{name}.json","w") as file:
        dump(d,file,indent=4)
    print(f"File has been successfully saved to JSON/{name}.json!")
else:
    print("Failed to get any results for the entered URL........")