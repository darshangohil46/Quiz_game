import mysql.connector


class ScoreList:
    def __init__(self, username) -> None:
        self.username = username

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

    def viewScore(self):
        sql = f"select * from quiz where userName = '{self.username}'"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        if data == []:
            print("User Name not found.")
        else:
            d = data[0]
            print()
            print("*********************************")
            s1 = "%-10s%-20s%-10s%-10s%-10s" % (
                "Mythology",
                "| General Knowledge",
                "| Sports",
                "| History",
                "| Movie",
            )
            print(s1)
            s2 = "%-10s%-20s%-10s%-10s%-10s" % (
                (str(d[5])),
                ("| " + str(d[6])),
                ("| " + str(d[7])),
                ("| " + str(d[8])),
                ("| " + str(d[9])),
            )
            print(s2)
            print("*********************************")
            print()


class AllPlayersScore:
    def __init__(self, type):
        self.type = type
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

    def show_score(self):
        if self.type == "all":
            self.total_score()
        else:
            # query for data recieve in descending order
            sql = (
                f"select userName, {self.type}, id from quiz order by {self.type} DESC"
            )
            self.cur.execute(sql)
            data = self.cur.fetchone()

            player = 1
            s1 = "%-7s%-20s%-17s%-10s" % (
                "Rank",
                "| User Name",
                "| Highest Score",
                "| Player ID",
            )
            print(s1)
            print("-------------------------------------------------------")

            while data:
                string = "%-7s%-20s%-17s%-10s" % (
                    (str(player)),
                    ("| " + str(data[0])),
                    ("| " + str(data[1])),
                    ("| " + str(data[2])),
                )
                print(string)
                player += 1
                data = self.cur.fetchone()

    def total_score(self):
        sql = "SELECT id, userName, SUM(mythology + gk + sports + history + movie) AS total_score FROM quiz GROUP BY id ORDER BY total_score DESC;"
        self.cur.execute(sql)
        data = self.cur.fetchall()

        if not data:
            print("No data found.")
            return

        print(
            "%-7s%-20s%-17s%-10s"
            % ("Rank", "| User Name", "| Total Score", "| Player ID")
        )
        print("-------------------------------------------------------")

        for player, row in enumerate(data, start=1):
            print(
                "%-7s%-20s%-17s%-10s"
                % (player, "| " + str(row[1]), "| " + str(row[2]), "| " + str(row[0]))
            )

        print("-------------------------------------------------------")
