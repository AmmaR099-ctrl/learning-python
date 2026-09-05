from bs4 import BeautifulSoup

with open("indie.html","r") as f:
    html=f.read()
soup=BeautifulSoup(html,"html.parser")
print(soup.title.parent.name,"\n",soup.p.text,"\n",soup.a)