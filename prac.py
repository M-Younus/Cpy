

from bs4 import BeautifulSoup

a=open(r"C:\Users\MY\Desktop\count_list.html","r")

allText=[]

soup=BeautifulSoup(a)
b=soup.select("option")
for i in range(239):
    b[i]['value']=b[i].text
    allText.append(b[i])


print(len(allText))
for i in range(239):
    print(allText[i])

