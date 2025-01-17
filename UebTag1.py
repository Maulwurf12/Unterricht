'''
#A1.1
firstName = "Mustermann"
lastName = "Max"

temp = lastName
print(temp)
lastName = firstName
print(lastName)
firstName = temp
print(firstName)

print(firstName)
print(lastName)'''
import math

'''#A1.2:
a = 42
b = a
c = a
a = 10
b = c
print(a, b, c)
#Antwort: 10 42 42'''
'''#A1.3
int(5.5) #möglich
float(-1) #möglich
str(0.3) #möglich
bool(0.0001) #möglich
str("False") #möglich
int(False) #möglich
bool('0') #nicht möglich
int("False") #nicht möglich
float("True") #nicht möglich
'''
'''
#A1.4:
firstName = "Lisa"
lastName = "Mueller"
height = 180
day = 23
month = "January"
year = "1999"
print(f"""Hi, my name is {firstName} {lastName}.
I am {height}cm tall and I was born on {day} {month} {year}.""")
#Antwort: Hi my name is Lisa Mueller. I am 180cm tall and I was born on 23 January 1999.
'''

'''#A2.1
#Entwickeln Sie ein Program, welches den BMI berechnet. Formel: BMI = Körpergewicht (kg) /
#Größe (m) ^ 2
weight = input("Enter your weight (in kg): ")
weight = float(weight)
size = input("Enter your size (in cm): ")
size = float(size) / 100
BMI = weight / (size ** 2)
print("Das ist ihr BMI: " + str(BMI))'''
'''#A2.2
#Entwickeln Sie ein Programm welches den Satz des Pythagoras berechnet. Es soll die Länge der
#Ankathete und Gegenkathete eingegeben werden. Als Ergebnis soll die Hypotenuse ausgegeben
#werden.
a = input("Enter number for a: ")
b = input("Enter number for b: ")
c = math.sqrt(int(a) ** 2 + int(b) ** 2)
print(c)'''
'''#A2.3
#Programmieren Sie einen Taschenrechner, welcher Plus, Minus, Mal und Geteilt rechnen kann. Der
#Rechner soll mit zwei Zahlen arbeiten können.
expression = input("Enter your calculation (e.g. 5 + 3): ")

try:
    # Teilen der Eingabe in Zahlen und Operator
    numberOne, operationType, numberTwo = expression.split()

    # Umwandlung der Zahlen in float
    numberOne = float(numberOne)
    numberTwo = float(numberTwo)

    # Berechnung basierend auf der Operation
    if operationType == "+":
        print(f"Result: {numberOne + numberTwo}")
    elif operationType == "-":
        print(f"Result: {numberOne - numberTwo}")
    elif operationType == "*":
        print(f"Result: {numberOne * numberTwo}")
    elif operationType == "/":
        if numberTwo == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {numberOne / numberTwo}")
    else:
        print("Error: Invalid operation.")
except ValueError:
    print("Error: Invalid input. Make sure to enter the expression in the format 'number operator number'.")
'''
'''#A3.1
#Bearbeiten Sie den Taschenrechner aus Übung 2.3. Das Programm soll mit verschiedenen Funktionen
#programmiert werden. Für jede Rechenart soll eine Funktion vorhanden sein
def add(numberOne, numberTwo):
    return numberOne + numberTwo


def subtract(numberOne, numberTwo):
    return numberOne - numberTwo


def multiply(numberOne, numberTwo):
    return numberOne * numberTwo


def divide(numberOne, numberTwo):
    if numberTwo == 0:
        return "Error: Division by zero is not allowed."
    return numberOne / numberTwo


def calculator():
    expression = input("Enter your calculation (e.g. 5 + 3): ")
    try:
        numberOne, operationType, numberTwo = expression.split()

        numberOne = float(numberOne)
        numberTwo = float(numberTwo)

        if operationType == "+":
            print(f"Result: {add(numberOne, numberTwo)}")
        elif operationType == "-":
            print(f"Result: {subtract(numberOne, numberTwo)}")
        elif operationType == "*":
            print(f"Result: {multiply(numberOne, numberTwo)}")
        elif operationType == "/":
            print(f"Result: {divide(numberOne, numberTwo)}")
        else:
            print("Error: Invalid operation.")
    except ValueError:
        print("Error: Invalid input. Make sure to enter the expression in the format 'number operator number'.")

calculator()'''



