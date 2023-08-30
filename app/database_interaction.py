import pymysql
import os
import datetime

#RDS Database Details
instance = os.environ["mysql_instance"]
username = os.environ["mysql_username"]
password = os.environ["mysql_password"]
endpoint = os.environ["mysql_endpoint"]
port = os.environ["mysql_port"]

#connect to database
db = pymysql.connect(host=endpoint, user=username, password=password, db=instance)

#create cursor
cursor = db.cursor()

#Write prompt and keywords to database
def db_write(prompt, chatgpt_response):
    db_input = (str(datetime.datetime.now()), prompt, chatgpt_response)
    cursor.execute("INSERT INTO imagine_prompts VALUES (%s,%s,%s)", db_input)
    db.commit()

#Pull 100 most recent items in database
def db_get_recent():
    cursor.execute("SELECT * FROM imagine_prompts ORDER BY datesubmitted DESC LIMIT 100")
    saved_prompts = cursor.fetchall()
    print(saved_prompts)
    return saved_prompts

cursor.close()
db.close()
