import mysql.connector
import random
class Play_quiz:
    # my_score=0

    def __init__(self, id, userName, phoneNum, email):
        self.id = id
        self.userName = userName
        self.phonNum = phoneNum
        self.email = email

        try:
            self.connection = mysql.connector.connect(
                host="localhost",  # MySQL server host
                user="root",  # MySQL username
                password="",  # MySQL password
                database="python",  # the name of database
            )
        except:
            print("DataBase not coonected")
        self.cur = self.connection.cursor()

    def choose_quetion_type(self):
        while True:
            print("Enter Your Subject")
            print("1. Mythology")
            print("2. General Knowledge")
            print("3. Sports")
            print("4. History Of India")
            print("5. Indian Movies")
            print("6. Exit")

            c = input("Enter Your Choice: ")
            choice = c.strip(" ")
            if choice == "1":
                self.mythology()
                break
            elif choice=='2':
                self.general_knowledge()
                break
            elif choice=='3':
                self.sports()
                break
            elif choice == '4':
                self.history()
                break
            elif choice == '5':
                self.movie()
                break
            elif choice=="6":
                break
            else:
                print('Invalid Choice...')
            print()

    # quetions for mythology
    def mythology(self):
        quetions = [
            """
Who is considered the king of the gods in Hindu mythology?
a) Vishnu
b) Shiva
c) Brahma
d) Indra
""",
            """
The epic poem "Mahabharata" is traditionally attributed to which sage?
a) Valmiki
b) Vyasa
c) Tulsidas
d) Kalidasa
""",
            """
Who is the wife of Lord Rama in the Hindu epic "Ramayana"?
a) Draupadi
b) Sita
c) Parvati
d) Saraswati
""",
            """
Which weapon is associated with the god Shiva?
a) Sudarshana Chakra
b) Trishul (trident)
c) Bow and arrow
d) Gada (mace)
""",
            """
Who is the goddess of wealth and prosperity in Hindu mythology?
a) Saraswati
b) Lakshmi
c) Parvati
d) Durga
""",
            """
In the story of the "Churning of the Ocean" (Samudra Manthan), what emerged first from the ocean?
a) The moon
b) Poison
c) Nectar (Amrit)
d) Goddess Lakshmi
""",
            """
Who is the monkey god known for his strength and loyalty in Hindu mythology?
a) Hanuman
b) Garuda
c) Jambavan
d) Sugriva
""",
            """
Who is the demon king killed by Lord Rama in the epic "Ramayana"?
a) Ravana
b) Hiranyakashipu
c) Mahishasura
d) Kumbhakarna
""",
            """
Who is the sage who wrote the "Bhagavad Gita"?
a) Vyasa
b) Valmiki
c) Narada
d) Vashishta
""",
            """
Who is the elephant-headed god worshipped as the remover of obstacles?
a) Ganesha
b) Kartikeya
c) Varuna
d) Agni
""",
        ]

        right_ = ["d", "b", "b", "b", "b", "b", "a", "a", "a", "a"]
        answer_list = []
        quit = 0
        index=1

        right_answers = []
        
        num=[]
        l = []
        # length=0
        while True:
            que_i = random.randint(0, 9)
            if que_i not in num:
                num.append(que_i)
                if que_i not in l:
                    l.append(quetions[que_i])
                    right_answers.append(right_[que_i])
            else:
                continue
            if len(l) == 10:
                break
            # l.append(quetions[que_i])

        for i in l:
            print(f"****************************{"Quetion " + str(index)}****************************")
            print(i)
            while True:
                answer = input(
                    "Enter Your Answer: (Enter Only A, B, C, D, or Exit) --> "
                ).lower()
                if answer == "exit":
                    quit = 1
                    break
                if answer in ["a", "b", "c", "d"]:
                    answer_list.append(answer)
                    break
                print("Invalid Answer...")
            if quit == 1:
                break
            index+=1

        self.check_answers(right_answers, answer_list, 'mythology')
        
    # quetions of gk
    def general_knowledge(self):
        questions = [
            """
What is the capital of France?
a) London
b) Paris
c) Rome
d) Berlin
""",
            """
Who painted the Mona Lisa?
a) Vincent van Gogh
b) Pablo Picasso
c) Leonardo da Vinci
d) Michelangelo
""",
            """
What is the largest planet in our solar system?
a) Earth
b) Jupiter
c) Mars
d) Saturn
""",
            """
Who wrote "To Kill a Mockingbird"?
a) Ernest Hemingway
b) Harper Lee
c) F. Scott Fitzgerald
d) Mark Twain
""",
            """
What is the chemical symbol for water?
a) Wo
b) W
c) H2O
d) H2
""",
            """
Who discovered penicillin?
a) Alexander Fleming
b) Marie Curie
c) Isaac Newton
d) Albert Einstein
""",
            """
Which country is famous for the pyramids?
a) Italy
b) Egypt
c) Greece
d) Turkey
""",
            """
What is the currency of Japan?
a) Yen
b) Euro
c) Dollar
d) Pound
""",
            """
Who was the first man to walk on the moon?
a) Buzz Aldrin
b) Neil Armstrong
c) Yuri Gagarin
d) Alan Shepard
""",
            """
Which gas do plants use to carry out photosynthesis?
a) Oxygen
b) Carbon dioxide
c) Nitrogen
d) Hydrogen
""",
        ]

        right_answers = ["b", "c", "b", "b", "c", "a", "b", "a", "b", "b"]
        answer_list = []
        quit_flag = False
        index =1


        for question in questions:
            print(f"****************************{"Quetion " + str(index)}****************************")
            print(question)
            while True:
                answer = input("Enter Your Answer: (Enter Only A, B, C, D, or Exit) --> ").lower()
                if answer == "exit":
                    quit_flag = True
                    break
                if answer in ["a", "b", "c", "d"]:
                    answer_list.append(answer)
                    break
                print("Invalid Answer...")
            if quit_flag:
                break
            index+=1

        self.check_answers(right_answers, answer_list, 'gk')

    # quetions for sports
    def sports(self):
        questions = [
            """
Which sport is known as the "king of sports"?
a) Soccer
b) Basketball
c) Tennis
d) Cricket
""",
            """
In which sport can a player score a "hat-trick"?
a) Football (Soccer)
b) Basketball
c) Tennis
d) Golf
""",
            """
How many players are there on a baseball team?
a) 9
b) 11
c) 7
d) 6
""",
            """
Who is known as the "Flying Sikh"?
a) Sachin Tendulkar
b) Milkha Singh
c) Kapil Dev
d) Dhyan Chand
""",
            """
What is the maximum number of clubs that a golfer is allowed to carry in a golf bag during a round?
a) 10
b) 14
c) 18
d) 20
""",
            """
Which country has won the most FIFA World Cup titles?
a) Brazil
b) Argentina
c) Germany
d) Italy
""",
            """
Which sport is associated with Wimbledon?
a) Tennis
b) Golf
c) Cricket
d) Rugby
""",
            """
In which sport would you perform an "alley-oop"?
a) Basketball
b) Soccer
c) Volleyball
d) American Football
""",
            """
Which of the following is not an event in the Olympic Games?
a) Marathon
b) Badminton
c) Taekwondo
d) Rugby Sevens
""",
            """
Who holds the record for the most Grand Slam singles titles in tennis history?
a) Serena Williams
b) Roger Federer
c) Rafael Nadal
d) Margaret Court
""",
        ]

        right_answers = ["d", "a", "a", "b", "b", "a", "a", "a", "d", "a"]
        answer_list = []  
        quit = 0
        index=1

        for question in questions:
            print(f"****************************{"Quetion " + str(index)}****************************")
            print(question)
            while True:
                answer = input("Enter Your Answer: (Enter Only A, B, C, D, or Exit) --> ").lower()
                if answer == "exit":
                    quit = 1
                    break
                if answer in ["a", "b", "c", "d"]:
                    answer_list.append(answer)
                    break
                print("Invalid Answer...")
            if quit == 1:
                break
            index+=1

        self.check_answers(right_answers=right_answers, answer_list=answer_list, type="sports")

    # quetions of history
    def history(self):
        questions = [
            """
Who was the first Governor-General of independent India?
a) Lord Mountbatten
b) Jawaharlal Nehru
c) C. Rajagopalachari
d) Dr. Rajendra Prasad
""",
            """
The Harappan Civilization is also known as:
a) Mesopotamian Civilization
b) Indus Valley Civilization
c) Vedic Civilization
d) Aryan Civilization
""",
            """
The Mauryan Empire was founded by:
a) Ashoka
b) Chandragupta Maurya
c) Bindusara
d) Pushyamitra Sunga
""",
            """
Who was the Mughal emperor at the time of the Battle of Plassey in 1757?
a) Akbar
b) Shah Jahan
c) Aurangzeb
d) Bahadur Shah II
""",
            """
The Indian National Congress (INC) was founded in:
a) 1885
b) 1905
c) 1919
d) 1942
""",
            """
Who was the first Indian woman to become the President of the Indian National Congress?
a) Sarojini Naidu
b) Annie Besant
c) Indira Gandhi
d) Vijaya Lakshmi Pandit
""",
            """
The Quit India Movement was launched in the year:
a) 1919
b) 1929
c) 1942
d) 1947
""",
            """
The Indian state of Jammu and Kashmir acceded to India in:
a) 1947
b) 1948
c) 1950
d) 1951
""",
            """
Who was the first Prime Minister of India?
a) Jawaharlal Nehru
b) Sardar Vallabhbhai Patel
c) Lal Bahadur Shastri
d) Indira Gandhi
""",
            """
The Indian Rebellion of 1857 started from:
a) Delhi
b) Meerut
c) Lucknow
d) Kanpur
""",
        ]

        right_answers = ["a", "b", "b", "d", "a", "a", "c", "b", "a", "b"]
        index=1
        answer_list = [] 
        quit_flag = False

        # Loop through each question
        for question in questions:
            print(f"****************************{"Quetion " + str(index)}****************************")
            print(question)
            while True:
                answer = input("Enter Your Answer: (Enter Only A, B, C, D, or Exit) --> ").lower()
                if answer == "exit":
                    quit_flag = True
                    break
                if answer in ["a", "b", "c", "d"]:
                    answer_list.append(answer)
                    break
                print("Invalid Answer...")
            if quit_flag:
                break
            index+=1

        self.check_answers(right_answers, answer_list, 'history')

    # quetions of movies
    def movie(self):
        questions = [
            """
Who directed the movie "Sholay," one of the most iconic films in Indian cinema?
a) Raj Kapoor
b) Yash Chopra
c) Ramesh Sippy
d) Manmohan Desai
""",
            """
Which Indian actor starred in the film "3 Idiots," which became one of the highest-grossing Bollywood films of all time?
a) Shah Rukh Khan
b) Salman Khan
c) Aamir Khan
d) Akshay Kumar
""",
            """
In which language was the movie "Baahubali: The Beginning" primarily released?
a) Hindi
b) Telugu
c) Tamil
d) Kannada
""",
            """
Who was the lead actress in the film "Mughal-e-Azam," often considered one of the greatest Indian films ever made?
a) Madhubala
b) Nutan
c) Meena Kumari
d) Nargis
""",
            """
Which film won the Academy Award for Best Foreign Language Film, making it the first and only Indian film to win in that category?
a) "Mother India"
b) "Lagaan"
c) "Pather Panchali"
d) "Gandhi"
""",
            """
Who directed the critically acclaimed film "Piku," starring Amitabh Bachchan and Deepika Padukone?
a) Karan Johar
b) Anurag Kashyap
c) Shoojit Sircar
d) Zoya Akhtar
""",
            """
In which year was the first Indian feature film, "Raja Harishchandra," released?
a) 1905
b) 1913
c) 1920
d) 1931
""",
            """
Which Indian movie holds the record for the highest-grossing film of all time in India?
a) "Dangal"
b) "Baahubali 2: The Conclusion"
c) "PK"
d) "Bajrangi Bhaijaan"
""",
            """
Who composed the music for the film "Slumdog Millionaire," which won the Academy Award for Best Original Score?
a) A.R. Rahman
b) Anu Malik
c) Shankar-Ehsaan-Loy
d) Vishal-Shekhar
""",
            """
Which Indian actress starred in the Hollywood film "Quantico" and also appeared in Bollywood movies like "Bajirao Mastani" and "Padmaavat"?
a) Deepika Padukone
b) Priyanka Chopra
c) Aishwarya Rai Bachchan
d) Kareena Kapoor Khan
""",
        ]

        right_answers = ["c", "c", "b", "a", "c", "c", "b", "b", "a", "b"]
        answer_list = []
        index=1
        quit_flag = False 

        # Loop through each question
        for question in questions:
            print(f"****************************{"Quetion " + str(index)}****************************")
            print(question)
            while True:
                answer = input("Enter Your Answer: (Enter Only A, B, C, D, or Exit) --> ").lower()
                if answer == "exit":
                    quit_flag = True
                    break
                if answer in ["a", "b", "c", "d"]:
                    answer_list.append(answer)
                    break
                print("Invalid Answer...")
            if quit_flag:
                break
            index+=1

        self.check_answers(right_answers, answer_list, 'movie')

    # method for check answers
    def check_answers(self, right_answers, answer_list, type):
        my_score=0
        self.right_answers = right_answers
        self.type = type
        self.answer_list = answer_list

        if right_answers == answer_list:
            print("Your All quetions Are Right")
        else:
            # index = 0
            min_length = min(len(right_answers), len(answer_list))
            for index, (right_answer, my_answer) in enumerate(zip(right_answers, answer_list)):
                if min_length == index:
                    break
                if right_answer == my_answer:
                    print(f"Your {index+1} is right.")
                    my_score += 10
                else:
                    print(f"Your {index+1} quetion is wrong {"("+my_answer+")"}. Right answer is {right_answer}")
            print(f"Your Score is {my_score}")

            self.insertDatabase(type, my_score)

    def insertDatabase(self, type, my_score):
        self.type = type
        self.my_score=my_score

        sql = f'UPDATE quiz SET {type} = {my_score} WHERE userName = "{self.userName}"'
        self.cur.execute(sql)
        self.connection.commit()
        self.connection.close()
