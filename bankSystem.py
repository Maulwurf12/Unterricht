import sqlite3
import hashlib

def connect_db():
    conn = sqlite3.connect('banksystem.db')
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personen (
            id INTEGER PRIMARY KEY,
            vorname TEXT,
            nachname TEXT,
            guthaben INTEGER,
            passwort TEXT
        )
    ''')

def hash_value(value):
    return hashlib.sha256(value.encode()).hexdigest()

def get_person_data(cursor, vorname, nachname):
    hashed_vorname = hash_value(vorname)
    hashed_nachname = hash_value(nachname)
    cursor.execute('''
    SELECT id, guthaben, passwort FROM personen
    WHERE vorname = ? AND nachname = ? 
    ''', (hashed_vorname, hashed_nachname))
    return cursor.fetchone()

def insert_new_person(cursor, vorname, nachname, guthaben, password):
    hashed_vorname = hash_value(vorname)
    hashed_nachname = hash_value(nachname)
    cursor.execute(
        "INSERT INTO personen (vorname, nachname, guthaben, passwort) VALUES (?, ?, ?, ?)",
        (hashed_vorname, hashed_nachname, guthaben, password)
    )

def update_balance(cursor, id, guthaben):
    cursor.execute("UPDATE personen SET guthaben = ? WHERE id = ?", (guthaben, id))

def get_user_input(prompt, valid_condition):
    while True:
        try:
            user_input = valid_condition(input(prompt))
            if user_input > 0:
                return user_input
        except ValueError:
            print("Bitte eine gültige Zahl eingeben!")

def main():
    conn, cursor = connect_db()
    create_table(cursor)

    print("Welcome to Bank System")
    givenPrename = input("Wie ist ihr Vorname? ").upper()
    givenLastname = input("Wie ist ihr Nachname? ").upper()

    person = get_person_data(cursor, givenPrename, givenLastname)

    if person is None:
        passwd = input("Legen sie ihr Passwort fest: ")
        hashedPasswd = hash_value(passwd)
        guthaben = 0
        insert_new_person(cursor, givenPrename, givenLastname, guthaben, hashedPasswd)
        person = get_person_data(cursor, givenPrename, givenLastname)
        conn.commit()

    id = person[0]
    kontostand = person[1]
    password = person[2]

    print("Was möchten sie tun?")
    print("1. Einzahlung \n2. Auszahlung \n3. Abfrage \n4. Exit")
    option = input("Wählen Sie ihre Option (1/2/3/4): ")
    inputPasswd = input("Bitte bestätigen sie ihre Identität mit einem Passwort: ")
    hashedInputPasswd = hash_value(inputPasswd)
    if hashedInputPasswd != password:
        print("Entschuldigen sie bitte, aber dies war nicht das korrekte Passwort. Dieser Vorgang wird nun beendet!")
        exit(1)
    if option == '1':
        einzahlung = get_user_input("Wie viel wollen Sie einzahlen? ", float)
        kontostand += einzahlung
        update_balance(cursor, id, kontostand)
        print("Ihre Einzahlung wurde ausgeführt!")
    elif option == '2':
        auszahlung = get_user_input("Wie viel wollen Sie sich auszahlen lassen? ", float)
        if auszahlung <= kontostand:
            kontostand -= auszahlung
            update_balance(cursor, id, kontostand)
            print("Ihre Auszahlung wurde ausgeführt!")
        else:
            print("Unzureichendes Guthaben!")
    elif option == '3':
        print(f"Ihr Kontostand beträgt: {kontostand}€")
    elif option == '4':
        print("Sie verlassen das Banksystem")
        conn.commit()
        conn.close()
        exit(0)
    else:
        print("Ungültige Option!")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
