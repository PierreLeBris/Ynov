import os 
import requests
import re
from bs4 import BeautifulSoup
from collections import Counter

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

mots = re.findall(r'\w+', open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/1.txt').read().lower())
print(Counter(mots).most_common(10))

print("Deuxième TXT")
data2 = file2.read()
words2 = data2.split()
print(file2.read(), len(words2))

mots2 = re.findall(r'\w+', open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/2.txt').read().lower())
print(Counter(mots2).most_common(10))

print("Troisième TXT")
data3 = file3.read()
words3 = data3.split()
print(file3.read(), len(words3))

mots3 = re.findall(r'\w+', open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/3.txt').read().lower())
print(Counter(mots3).most_common(10))

print("Quatrième TXT")
data4 = file4.read()
words4 = data4.split()
print(file4.read(), len(words4))

mots4 = re.findall(r'\w+', open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/4.txt').read().lower())
print(Counter(mots4).most_common(10))

print("Cinquième TXT")
data5 = file5.read()
words5 = data5.split()
print(file5.read(), len(words5))

mots5 = re.findall(r'\w+', open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/5.txt').read().lower())
print(Counter(mots5).most_common(10))

#text = open('/home/pierre/Bureau/YNOV/linux-git-python-master/books/1.txt')
#result = re.match(r"Author:", text)

#results = requests.get(file)

print("oui")