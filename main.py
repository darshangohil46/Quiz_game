import random
import mysql.connector
from score import *
from play_quiz import *


try:
    connection = mysql.connector.connect(
        host="localhost",  # MySQL server host
        user="root",  # MySQL username
        password="",  # MySQL password
        database="python",  # the name of database
    )
except:
    print("Error connecting to MySQL")

if connection.is_connected():
    cur = connection.cursor()
else:
    print("Database not connected")


class Register:
    def __init__(self, username, password, phone, email):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email

    # store into database
    def storeInDataBase(self):
        sql = f"insert into quiz(userName, password, phone, email) values ('{self.username}', '{self.password}', '{self.phone}', '{self.email}')"
        cur.execute(sql)
        connection.commit()


def phoneNum():
    phone = input("Enter Your Phone Number: ")
    if len(phone) == 10 and phone.isdigit():
        return phone
    print("Phone Number is Invalid...")
    phoneNum()


def create_password():
    password = input("Enter Your Password (min-length = 7): ")
    if len(password) < 7:
        print("Password is not valid...")
        create_password()
    return password


def email_check():
    email = input("Enter Your Email: ")
    if email != None:
        if "@" not in email or "." not in email:
            email_check()
        if email.count("@") != 1:
            email_check()
        before_a, after_a = email.split("@")
        if not before_a or not after_a:
            email_check()
        if "." not in after_a or len(after_a.split(".")[-1]) < 2:
            email_check()
    # print(before_a, after_a)
    return email


def register():
    phone_Num = phoneNum()
    password = create_password()
    email = email_check()
    name = input("Enter Your Name: ")

    # for duplicate username1
    username = ""
    while True:
        username = name + "_" + str(random.randint(10, 1000))
        cur.execute(f"select * from quiz where userName='{username}'")
        d = cur.fetchall()
        if d == []:
            break

    # call constructor of register class
    reg = Register(username, password, phone_Num, email)
    reg.storeInDataBase()

    print("Your Username is:", username)
    print("Registration Done! Now, You can Login into your account\n")


# login
def login():
    username = input("Enter Your Username: ")
    pwd = input("Enter Your Password: ")
    sql = f"SELECT * FROM quiz WHERE userName='{username}' AND password='{pwd}'"
    cur.execute(sql)
    data = cur.fetchall()
    return data


# for score list
def scores():
    while True:
        print("***********************")
        print("1. Show My Score")
        print("2. Mythology Quiz Score")
        print("3. Sports Quiz Score")
        print("4. History Quiz Score")
        print("5. Movie Quiz Score")
        print("6. Generak Knowledge Quiz Score")
        print("7. Total Score")
        print("8. Exit")
        print("***********************")

        c = input("Enter Your Choice: ")
        choice = c.strip(" ")

        if choice == "1":
            usr = input("Enter Your UserName: ")
            sl = ScoreList(usr)
            sl.viewScore()

        elif choice == "2":
            all_player_data = AllPlayersScore("mythology")
            all_player_data.show_score()

        elif choice == "3":
            all_player_data = AllPlayersScore("sports")
            all_player_data.show_score()

        elif choice == "4":
            all_player_data = AllPlayersScore("history")
            all_player_data.show_score()

        elif choice == "5":
            all_player_data = AllPlayersScore("movie")
            all_player_data.show_score()

        elif choice == "6":
            all_player_data = AllPlayersScore("gk")
            all_player_data.show_score()

        elif choice == "7":
            all_player_data = AllPlayersScore("all")
            all_player_data.show_score()

        elif choice == "8":
            break
        else:
            print("Invalid Choice...")


while True:
    print("**************************")
    print("1. Login")
    print("2. Register (New User)")
    print("3. View Score List")
    print("4. Exit")
    print("**************************")

    c = input("Enter Your Choice: ")
    choice = c.strip(" ")
    if choice == "1":
        d = login()
        # print(d) # [()]

        # if account exist
        if d:
            data = d[0]
            # data --> (id, userName, password, phoneNum, email)
            # print(data)
            id = data[0]
            userName = data[1]
            password = data[2]
            phone = data[3]
            email = data[4]
            # print(id, userName, password, phoneNum, email)

            play_quiz = Play_quiz(id, userName, phone, email)
            play_quiz.choose_quetion_type()
        else:
            print("Please, Register First.")

    elif choice == "2":
        register()

    elif choice == "3":
        scores()

    elif choice == "4":
        break

    else:
        print("Enter Valid Choice...")
