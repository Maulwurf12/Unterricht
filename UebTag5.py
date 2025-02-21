#1.1
#1.1.1 Aufgabe 1
#Gegeben sind die folgenden Variablen und Datenstrukturen
name = "Nico"
i = 42
myList = [i, name, True]
j = 42
book = {"angreifen" : "attack", "schreiben" : "write"}
#Geben Sie für jede Zeile an, welche Art von Exception geworfen wird:
#int(i)
#float(name)
#myList[3]
#i/(i-j)
#myList[i-40]
#print(f'Hallo {name}!")
#book["angreifen"]
#bool(name)
#i/(j%6)
#file = open("test.txt",'r') # "test.txt" existiert nicht.
#Antwort:
'''
int(i) gibt keinen Fehler, da es sich bereits um einen Integer handelt
float(name) Value Error. Der String name kann nicht in einen float gewandelt werden
myList[3] IndexError: list index out of range
i/(i-j) ZeroDivisionError: division by zero
myList[i-40] gibt keinen Fehler.
print(f'Hallo {name}!") SyntaxError: invalid syntax
book["angreifen"] gibt keinen Fehler.
bool(name) gibt keinen Fehler.
i/(j%6) ZeroDivisionError: division by zero
file = open("test.txt",'r') FileNotFoundError
'''
#1.1.2 Aufgabe 2
#Welche Exception könnte in folgendem Programm geworfen werden? Ergänzen Sie eine except
#Anweisung um den Fehler abzufangen und geben Sie darin aus, warum der Fehler aufgetreten ist.
'''names = {
"Jürgen" : "Müller",
"Martin": "Freund",
"Lisa": "Sonntag"
}
try:
    firstName = input("Enter first name")
    lastName = names[firstName]
    print(f"{firstName} {lastName}")'''
#Antwort:
'''
SyntaxError: expected 'except'

Ergänzung:
except KeyError:
    print(f"Fehler: Der Name '{firstName}' ist nicht in der Liste vorhanden.")
'''
#1.1.3 Aufgabe 3
#Welche Exceptions können in folgendem Programm geworfen werden? Ergänzen Sie mehrere except
#Anweisungen um die Fehler abzufangen und geben Sie darin aus, warum der Fehler aufgetreten ist.
'''try:
    weight = int(input("Gewicht (in kg): "))
    height = float(input("Körpergröße (in cm): "))
    bmi = weight/height**2
    print(f"Dein BMI ist {bmi}")'''
#Antwort:
'''
try:
    weight = int(input("Gewicht (in kg): "))
    height = float(input("Körpergröße (in cm): "))
    bmi = weight/height**2
    print(f"Dein BMI ist {bmi}")
except ValueError:
    print(f"Fehler: Bitte gültige Zahl eingeben")
except ZeroDivisionError:
    print(f"Fehler: Die Körpergröße darf nicht 0 sein")
'''
#1.1.4 Aufgabe 4
#Gegeben ist das folgende Programm:
'''class Zahl:
    def __init__(self, wert):
        self.wert = wert
try:
    wert = int(input("Geben Sie einen Wert an: "))
    zahl = Zahl(wert)
    ergebnis = 42 / zahl.wert'''
#Sorgen Sie mit einem finally Block dafür, dass das Objekt zahl immer gelöscht wird. Gebe dem
#Nutzer eine Nachricht aus, dass das Objekt gelöscht wurde. Sollte das Objekt nicht gelöscht werden
#können (z.B. wenn das Objekt nicht erzeugt werden konnte (siehe Zeile 6)), entsteht ein NameError.
#Dieser muss auch im finally Block abgefangen werden.

#Lösung:
'''
class Zahl:
    def __init__(self, wert):
        self.wert = wert

try:
    wert = int(input("Geben Sie einen Wert an: "))
    zahl = Zahl(wert)
    ergebnis = 42 / zahl.wert
    print(f"Ergebnis: {ergebnis}")
except ValueError:
    print("Fehler: Bitte eine gültige Zahl eingeben.")
except ZeroDivisionError:
    print("Fehler: Teilen durch Null ist nicht erlaubt.")
finally:
    try:
        del zahl
        print("Das Objekt 'zahl' wurde gelöscht.")
    except NameError:
        print("Fehler: Das Objekt 'zahl' konnte nicht gelöscht werden, da es nicht existiert.")

'''
#1.1.5 Aufgabe 5
#Gegeben ist folgendes Programm:
'''def isPrime(n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True
zahl = int(input("Gib eine Primzahl ein: "))
if not isPrime(zahl):
    raise IsNotPrimeError(zahl)'''
#Die Funktion isPrime() gibt für eine Zahl zurück, ob es sich um eine Primzahl handelt. Das
#Hauptprogramm fragt einen Nutzer nach einer Zahl. Handelt es sich nicht um eine Primzahl,
#wird die Exception IsNotPrimeError geworfen. Für die Eingabe 12 soll folgende Fehlermeldung
#erscheinen: main.IsNotPrimeError: 12 ist keine Primzahl!

#Lösung:
'''
class IsNotPrimeError(Exception):
    def __init__(self, zahl):
        super().__init__(f"{zahl} ist keine Primzahl!")

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Optimierung: Nur bis sqrt(n) prüfen
        if n % i == 0:
            return False
    return True

try:
    zahl = int(input("Gib eine Primzahl ein: "))
    if not isPrime(zahl):
        raise IsNotPrimeError(zahl)
    print(f"{zahl} ist eine Primzahl.")
except ValueError:
    print("Fehler: Bitte eine gültige ganze Zahl eingeben.")
except IsNotPrimeError as e:
    print(f"main.IsNotPrimeError: {e}")'''
#1.2
#1.2.1 Aufgabe 1
#1.2.2
#1.2.3
'''Schreiben Sie ein Programm, welches Daten von einer Crypto API abrufen kann. Nutzen Sie hierfür
die Kucoin API. Der Nutzer soll über die Konsole einen Coin und eine Währung eingeben können.
Das Programm soll den aktuellen Preis in der passenden Währung ausgeben. Es soll zusätzlich das
Datum und die Uhrzeit ausgegeben werden, von der der aktuelle Preis stammt.
Info: Die Funktionalität der Kucoin API ist sehr umfangreich. Sie benötigen keinen API key
um diese zu verwenden. Die Aufgaben beziehen sich nur auf das Kapitel “Market Data” der
Dokumentation: Dokumentation Marked Data
Tipp: Nutzen Sie die Funktion “Get Ticker” um die Aufgabe zu lösen: Get Ticker
Beispiel: Request für BTC in EURO: https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-
USDT'''

#Programm:
'''
import requests
from datetime import datetime

def get_currency_name(currency_code):
    url = f"https://api.kucoin.com/api/v1/currencies/{currency_code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['code'] == '200000':
            return data['data']['fullName']
        else:
            print(f"Fehler beim Abrufen des Namens für {currency_code}: {data['msg']}")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP-Fehler aufgetreten: {http_err}")
        return None
    except Exception as err:
        print(f"Ein Fehler ist aufgetreten: {err}")
        return None

def get_crypto_price():
    coin = input("Geben Sie die Kryptowährung ein (z.B. BTC): ").upper()
    currency = input("Geben Sie die Zielwährung ein (z.B. USDT): ").upper()
    symbol = f"{coin}-{currency}"

    coin_name = get_currency_name(coin)
    currency_name = get_currency_name(currency)

    if not coin_name or not currency_name:
        print("Konnte die vollständigen Namen nicht abrufen. Überprüfen Sie die eingegebenen Währungscodes.")
        return

    url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data['code'] == '200000':
            price = data['data']['price']
            timestamp = data['data']['time'] / 1000
            dt_object = datetime.fromtimestamp(timestamp)

            print(f"Der aktuelle Preis von {coin_name} beträgt: {price} {currency_name}")
            print(f"Datum und Uhrzeit des Preises: {dt_object}")
        else:
            print("Fehler beim Abrufen der Preisdaten:", data['msg'])

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP-Fehler aufgetreten: {http_err}")
    except Exception as err:
        print(f"Ein Fehler ist aufgetreten: {err}")

get_crypto_price()
'''