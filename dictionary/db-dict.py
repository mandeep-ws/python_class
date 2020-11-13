
import mysql.connector
import json
import difflib
from difflib import get_close_matches








def db_dict(word):
    con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
    cursor = con.cursor()
    word = word.lower()
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[0])
    elif not results:
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression  LIKE '{}%'".format(word))
        results = cursor.fetchall
        print(results)
        if results:
            for result in results:
                print(result[0])
        else:
            print("not found")








word=input("Enter the word: ")
db_dict(word)


