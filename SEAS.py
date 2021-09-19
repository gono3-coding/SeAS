import requests
import pyperclip
from bs4 import BeautifulSoup
import webbrowser as wb


                                  
a = "░██████╗███████ ░█████╗░░██████╗"
b = "██╔════╝█       ██╔══██╗██╔════╝"
c = "╚█████╗░███████╗███████║╚█████╗░"
d = "░╚═══██╗██╔══╝░░██╔══██║░╚═══██╗"
e = "██████╔╝███████╗██║░░██║██████╔╝"
f = "╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(" ")
print(" Credit : Gono3")
print("\n")
movie_name = input("Enter Movie Name :-- ")
url = requests.get(f"https://www.levidia.ch/search.php?q={movie_name}")
src = url.content
soup = BeautifulSoup(src, "lxml")



link = soup.find("div",class_="mainlink")
for url in link.find_all('a'):
    a = url.get('href')
    
    
b = "https://www.levidia.ch/"+a


url = requests.get(b)
src = url.content
soup = BeautifulSoup(src, "lxml")

link = soup.find("span",class_="mainlink kiri")
try:
    for url in link.find_all('a'):
        a = url.get('href')
        print(a)
except:
    print("We currently do not support that movie (✖╭╮✖) ")
    quit()

    
wb.open(a)








