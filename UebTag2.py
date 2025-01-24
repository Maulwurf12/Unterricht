# Aufgabe 1.1
#1.1.1
#data = ["abc123",12,True,0.25,-3,'J','N']
#Welche Elemente werden ausgegeben
'''
data[0] # abc123
data[3] #0.25
data[-2] #J
data[-5] #True
data[2] #True
data[2+2] #-3
data[3*0-1] #N
data[3//3] #12
data[-1*3] #-3
data[7-2] #J
'''
#1.1.2
#alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L']
#Welche Elemente werden in folgendem Program ausgegeben?
#alphabet[2:5] cde
#alphabet[-5:-1] hijk
#alphabet[:] abcdefghijkl
#alphabet[5:] fghijkl
#alphabet[:3] abc
#alphabet[:-5] abcdefg
#alphabet[2:2] nichts
#alphabet[::2] acegik
#alphabet[2::2] cegik
#alphabet[-50:50] abcdefghijkl
#alphabet[:len(alphabet)] abcdefghijkl
#1.1.3
'''
[0,1,2] * 2 = [0,1,2,0,1,2]
3 * [True,False] = [True,False, True, False, True, False]
[1,1] + [2,2] + [3,3] = [1,1,2,2,3,3]
["Hallo"] + ["Python",'!'] = ["Hallo","Python",'!']
2 * ([True] + [True, False]) = [True, True, False, True, True, False]
'''
#1.1.4
#values = [0,1,2,3,4,5]
#Geben Sie für jede Zeile an, wie sich die Liste verändert?
'''
values[2] = 5, es wird draus [0,1,5,3,4,5]
values.remove(1), es wird draus [0,2,3,4,5]
values.append(7), es wird draus [0,1,2,3,4,5,7]
values.remove(4), es wird draus [0,1,2,3,5]
values += [1,2,3], es wird draus [0,1,2,3,4,5,1,2,3]
values.insert(3,0), es wird draus [0,1,2,0,3,4,5]
values.sort(reverse=True), es wird draus [5,4,3,2,1,0]
values.insert(2,3), es wird draus [0,1,3,2,3,4,5]
values.append(values.count(0)), es wird draus [0,1,2,3,4,5,0]
values.remove(values.index(3)), es wird draus [0,1,2,4,5]
values.clear(), es wird draus []
'''
#1.1.5
'''
print(','.join(['3',"14"])) = 3,14
print('.'.join(["Max","Mustermann"])) = Max.Mustermann
print('*'.join(['1', '2', '3', '4','5'])) = 1*2*3*4*5 
print(''.join(['F','l','o'])) = Flo
print('--'.join(['-','-','-'])) = --/--
'''
#1.1.6
'''matrix = [
[1,0,1],
[0,1,0],
[3,2,1],
[1,2,3],
[3,0,3]
]'''
#Wie lauten die Ausgaben des Programms?
'''
matrix[0][2] = 1
matrix[2][2] = 1
matrix[4][2] = 3
matrix[1][1] = 1
matrix[3][1] = 2
matrix[2][0] = 3
matrix[0] = [1,0,1]
matrix[2] = [3,2,1]
'''
#Aufgabe 1.2
#1.2.1
'''
Was unterschiedet Tupel und Listen voneinander?
Tupel sind unveränderbar, während Listen sich quasi unendlich erweitern lassen.
Die Syntax ist ein wenig anders und sie werden in c auch anders angelegt.
Welche Vorteile bieten Tupel gegenüber Listen?
Sie sind schneller, sie benötigen weniger Speicher und sind schneller. Außerdem lassen sich Dictionaries draus machen
'''
#1.2.2
#Was wird durch folgendes Program ausgegeben?
'''
tupel = (0,1,2,3,3,0)
copy = tupel
print(tupel[2])
print(copy[5])
print(tupel.index(0))
index = tupel.index(3)
print(copy[index])
index = copy.count(3)
print(tupel[index])
print(5 in copy)

Ausgabe: 20032False
'''
#1.2.3
'''
a = (1, 2, 3)
b = (4, 5, 6)

# Umwandlung der Tupel in eine Liste
list = list(a) + list(b)

# Ausgabe
print(list)
'''
#1.2.4
#chreiben Sie eine Funktion mit dem Namen checkSet(), die als Parameter eine Variable und ein
#set erhält. Die Funktion soll true zurückgeben, sollte die Zahl in dem Set vorhanden sein
'''def checkset(var, my_set):
    if var in my_set: return True
    else: return False'''
#1.2.5
'''values = {"eins" : 1, "zwei" : 2, "drei" : 3}
#Geben Sie an, wie das dictionary nach jeder Zeile aussieht.
values.update({"eins" : 2})
#values = {"eins" : 2, "zwei" : 2, "drei" : 3}
del values["drei"]
#values = {"eins" : 1, "zwei" : 2}
values.clear()
# values = {}
values.update({"null" : 0})
# values = {"null": 0}
values.update({"eins" : 0})
#values = {"null" : 0, "eins" : 0}
values["eins"] = 1
#values = {"null" : 0, "eins" : 1}
del values["null"]
#values = {"eins": 1}'''

#1.2.6
'''
names = {
"Florian" : 25,
"Bertel" : 28,
"Eva" : 51,
"Günter" : 60
}
'''
#Erstellen Sie eine Liste mit allen Namen und eine zweite Liste mit jedem Alter
'''def copy_keys_and_values(my_dict):
    keys_list = list(my_dict.keys())
    values_list = list(my_dict.values())
    return keys_list, values_list'''
#1.2.7
'''
#Definieren Sie ein Dictionary mit allen Schulnoten als Schlüssel (1-6). Als Werte soll die jeweilige
#Note verbalisiert sein (z.B. 1: Sehr gut).
notenDic = {1: "Sehr gut", 2: "gut", 3:"befriedigend", 4:"ausreichend", 5:"mangelhaft", 6:"ungenügend"}
#Schreiben Sie eine Funktion, die als Input eine Zahl nimmt und als Output die Note als Text
#ausgibt. Die Funktion muss das Dictionary verwenden.
def translationOfGrades(grade):
    if grade in notenDic:
        return notenDic[grade]
'''
#Aufgabe 1.3
#1.3.1
#Geben Sie alle geraden Zahlen der Liste aus. myList = [10,11,12,13,14,15,16,17,18,19,20]
'''
for i in myList:
    if i % 2 == 0:
        print(i)
'''
#1.3.2
#Geben Sie folgende Liste mit Index aus. names = ["Anna", "Bella", "Charlotte", "Diana", "Erika", "Fiona"]
'''
for i in names:
    print("Das ist der Index " + str(names.index(i)) + ", Name: " + i)
'''
#1.3.3
#Schreiben Sie eine Funktion, welche eine zweidimensionale Liste aus Integern erhält. Diese soll mit
#der folgenden Formatierung ausgegeben werden. Die einzelnen Listen müssen alle gleich lang sein.
'''def print_matrix(matrix):
    # Erste Zeile: Indizes
    print("  ", end="")
    for j in range(len(matrix[0])):
        print(j, end=" ")
    print()  # Neue Zeile für die Trennlinie

    # Trennlinie
    print(" — " * len(matrix[0]))

    # Die restlichen Zeilen
    for i in range(len(matrix)):
        print(f"{i} |", end=" ")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

matrix = [
    [5, 5, 5],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix(matrix)'''
#1.3.4
'''
x = 0
for i in range(5):
    x += 1
    for j in range(x):
        print("!")
'''
#Antwort: 5 + 4 + 3 + 2 + 1
#1.3.5
'''
Welche der Schleifen sind Endlosschleifen?
Schleife 1: #keine Endlosschleife
while True and False:
print("Text")
Schleife 2: #keine Endlosschleife
running = False
while running:
running = True
if running:
print("Das Programm wird ausgeführt.")
else:
print("Das Programm wird nicht ausgeführt.")
Schleife 3: #kommt drauf an. Wenn was eingegeben wird dann ja, wenn nichts, dann nicht
running = True
while running:
    running = input("Weitermachen? ")
    if running != False:
        running = True
'''
#1.3.6
#Ersetzen Sie diese while Schleife durch eine for Schleife

value = [12.50, 13.99, 21.75, 3.14, 13, 37]
'''
i = 0
while True:
    if i == len(value):
        break
    print(value[i])
    i += 1
'''
'''
for i in value:
    print(i)
'''