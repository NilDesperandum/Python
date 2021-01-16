import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    statement = """ CREATE TABLE IF NOT EXISTS contacts(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        address text,
                                        phone_number text,
                                        email_address text
                                    ); """
    try:
        cursor = conn.cursor()
        cursor.execute(statement)
    except Error as e:
        print(e)

def add_contact(conn):

    print("Tworzenie nowego kontaktu: ")
    name = input("Podaj nazwę kontaktu: ")
    address = input("Podaj adres kontaktu: ")
    phone = input("Podaj numer telefonu kontaktu: ")
    email = input("Podaj email kontaktu: ")
    data = [name,address,phone,email]

    sql = " INSERT INTO contacts(name,address,phone_number,email_address) VALUES(?,?,?,?) "

    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit()
    print("Dodano kontakt")


def edit_contact(conn):
    
    print("Edytowanie kontaktu: ")
    id = int(input("Podaj id kontaktu: "))

    sql = "UPDATE contacts SET name = ?,address = ?,phone_number = ?,email_address = ? WHERE id = ?"

    name = input("Podaj nową nazwę kontaktu: ")
    address = input("Podaj nowy adres kontaktu: ")
    phone = input("Podaj nowy numer telefonu kontaktu: ")
    email = input("Podaj nowy email kontaktu: ")
    data = [name,address,phone,email,id]

    cur = conn.cursor()
    cur.execute(sql,data) 
    conn.commit()
    print('Edytowano kontakt')


def delete_contact(conn):
    print("Usuwanie kontaktu: ")

    sql = "DELETE FROM contacts WHERE id = ?"
    
    id = int(input("Podaj id kontaktu: "))
    data = (id,)
    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit()
    print("Usunieto kontakt")


def list_contacts(conn):

    print("Lista kontaktów: ")

    sql = "SELECT * FROM contacts"

    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def stop_app(conn):
    return True


def main():

    database = r"pythonsqlite.db"

    

    conn = create_connection(database)

    if conn is not None:
        create_table(conn)
        cases = {
                1: add_contact,
                2: edit_contact,
                3: delete_contact,
                4: list_contacts,
                0: stop_app
            }
        while True:
            print("MENU GŁÓWNE: ")
            print("1. Dodaj kontakt ")
            print("2. Edytuj kontakt")
            print("3. Usuń kontakt")
            print("4. Wypisz kontakty")
            print("0. Wyjdź z aplikacji")
            choice = int(input("Co chcesz zrobić ?\n"))
            result = cases.get(choice,lambda x: print("Nie ma podanej opcji!"))(conn)
            if result == True:
                print("Zamykanie aplikacji")
                break

        
    else:
        print("Error! Cannot create database connection.")

    



if __name__ == "__main__":
    main()
