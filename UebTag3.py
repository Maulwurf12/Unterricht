'''
#1.1
#A1.1.1
Was macht das folgende Programm?
myGrades = []
with open("grade.txt", "r") as grades:
    for grade in grades:
        myGrades.append(grade)
print(myGrades)
# Liest Zeile für Zeile die Datei aus und speichert sie in der Liste und gibt sie anschließend aus
'''
'''
#A1.1.2
with open("zutaten.txt", "r+"): # a ist besser
    zutaten.write("Butter\n") 
    zutaten.write("Zucker\n")
zutaten.close() #nicht nötig
'''
#1.1.3
'''
Schreiben Sie den Code so, dass der Kontextmanager verwendet wird
myMovies = []
movies = open("movies.txt", "r")
for movie in movies:
    myMovies.append(movie)
movies.close()

###

myMovies = []
with open("myMovies.txt", "r") as m:
    for movie in m:
        myMovies.append(movie.strip())
print(myMovies)
'''
#1.2
#1.2.1
'''
# Ein Paket besteht aus ganz vielen Modulen und Unterverzeichnissen
# Ein Modul besteht einfach nur aus einer Datei mit verschiedenen Methoden, die dann vom Modul bereitgestellt werden
'''
#1.2.2
'''

import math
zahl1=112
zahl2=220
print(math.gcd(zahl1, zahl2))
#A: 4
'''
#1.2.3
'''
import os
user = os.getlogin()
os.system("echo Hallo " + user)
'''
#1.2.4
'''
import sys
version = sys.version
print("Ihre Version " + version)
'''
#1.2.5
'''import datetime
def timepoint():
    print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
timepoint()
'''
#1.2.6
# import random
#1.2.7
'''
#Modul:
import os
import datetime
import sys
class myOwnBib:
    def __init__(self, bib):
        self.bib = bib
    def getLogin(self):
        return os.getlogin()
    def getDate(self):
        return datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    def getPythonVersion(self):
        return sys.version.split()[0]
'''

#1.3
#1.3.1
'''import sys

def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        numbers = list(map(float, sys.argv[1:]))
        print(average(*numbers))
    else:
        print("Keine Werte übergeben!")'''
#1.3.2
'''def print_types(pos_param, *args, **kwargs):
    # Positional Parameter
    print(f"Positional Parameter: {pos_param} - Typ: {type(pos_param)}")

    # *args Parameter
    for arg in args:
        print(f"*args Parameter: {arg} - Typ: {type(arg)}")

    # **kwargs Parameter
    for key, value in kwargs.items():
        print(f"**kwargs Parameter: {key} = {value} - Typ: {type(value)}")

print_types(10, 20, 30, "Hallo", [1, 2, 3], key1="Wert1", key2=5.5)'''

#1.3.3
#erste Variante
'''numbers = [4, -2, 102, -5, -12, 3]
newList = []
for i in range (len(numbers)):
    if(numbers[i] > 0):
        print(numbers[i])
        newList.append(numbers[i])
#zweite Variante
newList = [new for new in numbers if new > 0]
print(newList)'''
