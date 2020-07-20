import re
import pymysql

infile = open('nodisc.txt', 'r', encoding="utf8")   # input file

regex = r"(\d{1,2}\/\d{1,2}\/\d{2,4}), (\d{1,2}\:\d{2}\s\w\.?\w\.?) - ([a-z0-9 \S]+?): ((?:[^\/]+(?:\n|$))+)"

test_str = infile.read()    # the entire text file in string


# Open database connection
db = pymysql.connect("localhost", "root", "", "testdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS DATA")

# Create table as per requirement
sql = """CREATE TABLE DATA (
   DATE  CHAR(20) NOT NULL,
   TIME CHAR(20) NOT NULL,
   SENDER  CHAR(20),
   MESSAGE MEDIUMTEXT )"""

cursor.execute(sql)

try:
    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches):
        # matchNum = matchNum + 1
        cursor.execute("""INSERT INTO DATA(DATE, TIME, SENDER, MESSAGE) VALUES(%s,%s,%s,%s)""", (match.group(1),
                                                                                                 match.group(2),
                                                                                                 match.group(3),
                                                                                                 match.group(4),
                                                                                                 ))
    db.commit()

except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
infile.close()
