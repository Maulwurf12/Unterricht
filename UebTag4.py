#1.1
#1.1.1
#Was sind die Vorteile von objektorientierter Programmierung?
#Wann sollte man sie nutzen?
'''
1. Modularität und Wiederverwendbarkeit
2. Verbesserte Wartbarkeit
3. Erweiterbarkeit (Polymorphismus)
4. Bessere Modellierung komplexer Probleme
5. Kapselung
Man sollte sie nutzen sobald das Programm komplexer wird oder Entitäten modelliert werden sollen
'''
#A1.1.2
'''
Geben Sie für jede Zeile an, ob eine Methode oder eine Funktion aufgerufen wird.
len([1,2,3,4,5]) # Funktion
"Hallo Python!".index('y') # Methode
["Amina","Aurelia","Anna"].count('A') # Methode
random.shuffle([4,8,15,16,23,42]) # Funktion
print("Hallo Python!") # Funktion
math.sqrt(9) # Funktion
{}.clear() # Methode
set().add(0) # Methode
'''
#A1.1.3
'''
class Account:
    def __init__(self, owner, accountNumber, amount):
        self._owner = owner
        self._accountNumber = accountNumber
        self._amount = amount
Schreiben Sie eine Methode getInfo, mit der der Kontoinhaber und die Kontonummer ausgelesen
werden kann. Auf den Geldbetrag darf nicht zugegriffen werden. Die Schnittstelle soll einen Param-
eter key bekommen. Ist dieser key “owner” soll der Eigentümer, ist dieser key “accountNumber”,
soll die Nummer zurückgegeben werden.
    def getInfo(self, key):
        if key == "owner":
            return self._owner
        elif key == "accountNumber":
            return self._accountNumber
        else:
            return "Ungültiger Schlüssel"
'''
#A1.1.4
'''Gegeben sei die folgende Pokemon Klasse:
1
class Pokemon:
    def __init__(self, name, number, height, weight, trainer, pokeType):
        self._name = name
        self._number = number
        self._height = height
        self._weight = weight
        self._trainer = trainer
        self._pokeType = pokeType
        self._health = 20
    def getHealth(self):
        return self._health
Schreiben Sie eine Methode transferHealth, die als Parameter ein Pokemon und die Anzahl an
Lebenspunkten erhält. Diese wird z.B. so aufgerufen:
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")
schiggy.transferHealth(pikatchu, 5)
Nach dem Aufruf soll Pikachu nun 25 und Schiggy 15 Leben haben.
Ein Pokemon kann die gewünschte Anzahl an Leben aber nur übertragen, wenn noch mindestens
ein Lebenspunkt übrig ist. Ansonsten soll die Funktion einen Fehler melden
    def transferHealth(self, targetPokemon, healthPoints):
        if healthPoints <= 0:
            print("Fehler: Die Anzahl der übertragenen Lebenspunkte muss positiv sein.")
            return

        if self._health > healthPoints:
            self._health -= healthPoints
            targetPokemon._health += healthPoints
            print(f"{self._name} überträgt {healthPoints} Lebenspunkte an {targetPokemon._name}.")
        else:
            print(f"Fehler: {self._name} hat nicht genug Lebenspunkte für die Übertragung.")
'''
#1.2
#A1.2.1
'''
class Pokemon:
    def __init__(self,name,number,height,weight,trainer,pokeType):
        self._name = name
        self._number = number
        self._height = height
        self._weight = weight
        self._trainer = trainer
        self._pokeType = pokeType
    def __eq__(self,other):
        return self._name == other._name
Welche Ausgabe erzeugt das folgende Programm?
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu1 = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")
pikachu2 = pikachu1
pikachu3 = Pokemon("Pikachu", 25, 0.35, 5, "Max", "Elektro")
glumanda = Pokemon("Schiggy", 4, 0.61, 8.5, "Ash", "Feuer")
print(schiggy == pikachu1) # False
print(schiggy == schiggy) # True
print(schiggy is schiggy) # True
print(pikachu1 == pikachu2) # True
print(pikachu2 is pikachu1) # True
print(glumanda is glumanda) # True
print(glumanda == schiggy) # True
print(glumanda is schiggy) # False
print(pikachu1 == pikachu3) # True
print(pikachu1 is pikachu3) # False
'''
#1.2.2
'''
class Pokemon:
    def __init__(self,name,number,height,weight,trainer,pokeType):
        self._name = name
        self._number = number
        self._height = height
        self._weight = weight
        self._trainer = trainer
        self._pokeType = pokeType
        self.printName()
    def __eq__(self,other):
        return self._name == other._name

    def printName(self):
        name = self._name
        if(name.lower() == "pikachu"):
            print("Pika, Pika!")
        else:
            print(name + ", " + name + "!")

pikachu = Pokemon("Pikachu", 7, 0.5, 9, "Ash", "Wasser")'''
#1.2.3
'''class Bruch:
    def __init__(self, zähler, nenner):
        if nenner == 0:
            raise ValueError("Nenner darf nicht 0 sein")
        self.zähler = zähler
        self.nenner = nenner

    def __add__(self, other):
        zähler = self.zähler * other.nenner + self.nenner * other.zähler
        nenner = self.nenner * other.nenner
        return Bruch(zähler, nenner)

    def __sub__(self, other):
        zähler = self.zähler * other.nenner - self.nenner * other.zähler
        nenner = self.nenner * other.nenner
        return Bruch(zähler, nenner)

    def __mul__(self, other):
        zähler = self.zähler * other.zähler
        nenner = self.nenner * other.nenner
        return Bruch(zähler, nenner)

    def __truediv__(self, other):
        zähler = self.zähler * other.nenner
        nenner = self.nenner * other.zähler
        return Bruch(zähler, nenner)

    def __eq__(self, other):
        return self.zähler * other.nenner == self.nenner * other.zähler

    def __lt__(self, other):
        return self.zähler * other.nenner < self.nenner * other.zähler

    def __gt__(self, other):
        return self.zähler * other.nenner > self.nenner * other.zähler

    def __str__(self):
        if self.zähler == 0:
            return "0"
        elif self.nenner == 1:
            return str(self.zähler)
        elif (self.zähler < 0) ^ (self.nenner < 0):
            return f"-{abs(self.zähler)}/{abs(self.nenner)}"
        else:
            return f"{abs(self.zähler)}/{abs(self.nenner)}"
'''
#1.3
#1.3.1
'''
class Tier:
    def __init__(self, name):
        self.name = name
        self.tierart = "Tier"

    def __str__(self):
        return f"{self.name} ist ein {self.tierart}."

    def reden(self):
        print("...")

class Hund(Tier):
    def __init__(self, name):
        super().__init__(name)
        self.tierart = "Hund"

    def reden(self):
        print("Wuff, wuff!")

class Ente(Tier):
    pass

class Robbe(Tier):
    def __init__(self, name):
        super().__init__(name)
        self.tierart = "Robbe"

    def reden(self):
        print("Ow, ow!")

benni = Tier("Benni")
maya = Hund("Maya")
robin = Robbe("Robin")
darkwing = Ente("Darkwing")
print(benni)
print(maya)
print(robin)
print(darkwing)
benni.reden()
robin.reden()
darkwing.reden()
maya.reden()
Erwartete Ausgabe:
Benni ist ein Tier.
Maya ist ein Hund.
Robin ist ein Robbe.
Darkwing ist ein Tier.
...
Ow, ow!
...
Wuff, wuff!

'''
#A1.3.2
'''class Person:
    def __init__(self, name, alter):
        self._name = name
        self._alter = alter

    def geburtstagFeiern(self):
        self._alter += 1

class Student(Person):
    def __init__(self, name, alter, matrikelnummer, altersgrenze):
        super().__init__(name, alter)
        self._matrikelnummer = matrikelnummer
        self.altersgrenze = altersgrenze

    def studieren(self):  # Funktionsaufruf hinzugefügt
        if self._alter < self.altersgrenze:
            print("Der Student " + self._name + " mit Matrikelnummer " + str(self._matrikelnummer) + " studiert fleißig")
        else:
            print("Der Student " + self._name + " ist zu alt zum Studieren")
student1 = Student("Max", 22, 12345, 33)
student1.studieren()'''
