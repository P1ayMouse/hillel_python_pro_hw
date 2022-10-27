import sqlite3
from faker import Faker


def create_table():
    con = sqlite3.connect("hw_3.db")
    cur = con.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS person(
    personid INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    address VARCHAR(1024),
    job VARCHAR(128),
    age INTEGER NOT NULL
    )
    '''
    cur.execute(sql)
    con.close()


def insert_person():
    fake = Faker()
    con = sqlite3.connect("hw_3.db")
    cur = con.cursor()
    sql = f'''
            INSERT INTO person (first_name, last_name, Address, job, Age)
            VALUES
                ('{fake.first_name()}', '{fake.last_name()}', 
                '{fake.address()}', '{fake.job()}', {fake.random_int(18, 80)})
        '''
    cur.execute(sql)
    con.commit()
    con.close()


def print_people():
    con = sqlite3.connect("hw_3.db")
    cur = con.cursor()
    sql = '''
        SELECT * FROM person
        '''
    people = cur.execute(sql)
    for p in people:
        print(p)
    con.close()


def delete_person_by_id(personid):
    con = sqlite3.connect("hw_3.db")
    cur = con.cursor()
    sql = f'''
        DELETE FROM person WHERE personid = {personid}
        '''
    cur.execute(sql)
    con.commit()
    con.close()


def update_person_age(personid, age):
    con = sqlite3.connect("hw_3.db")
    cur = con.cursor()
    sql = f'''
        UPDATE person
        SET AGE = {age}
        WHERE personid = {personid}
        '''
    cur.execute(sql)
    con.commit()
    con.close()


if __name__ == "__main__":
    create_table()
    while True:
        user_select = input("\nЩо вам необхідно?\n"
                            "\n\t1. Створити нову персону"
                            "\n\t2. Вивід усіх людей"
                            "\n\t3. Оновити вік якоїсь персони"
                            "\n\t4. Видалення персони за id"
                            "\n\nВідповідь: ")
        if user_select == '1':
            insert_person()
        elif user_select == '2':
            print("\nТаблиця person:")
            print_people()
        elif user_select == '3':
            update_person_age(int(input("\nВведіть id персони: ")),
                              int(input("Введіть оновлений вік персони: ")))
        elif user_select == '4':
            delete_person_by_id(int(input("\nВведіть id персони: ")))
        else:
            print("\nНе правильно вказана відповідь")
