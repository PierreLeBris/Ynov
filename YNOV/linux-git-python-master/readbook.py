import os 
import requests
import re
from bs4 import BeautifulSoup

file = open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/1.txt')
file2 = open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/2.txt')
file3 = open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/3.txt')
file4 = open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/4.txt')
file5 = open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/5.txt')
print("non")

#with file as fo:
#    for rec in fo:
#        print(rec.split('Author:'))

print("Premier TXT")
data = file.read()
words = data.split()
print(file.read(), len(words))

print("Deuxième TXT")
data2 = file2.read()
words2 = data2.split()
print(file2.read(), len(words2))

print("Troisième TXT")
data3 = file3.read()
words3 = data3.split()
print(file3.read(), len(words3))

print("Quatrième TXT")
data4 = file4.read()
words4 = data4.split()
print(file4.read(), len(words4))

print("Cinquième TXT")
data5 = file5.read()
words5 = data5.split()
print(file5.read(), len(words5))


#text = open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/1.txt')
#result = re.match(r"Author:", text)

#results = requests.get(file)

print("oui")