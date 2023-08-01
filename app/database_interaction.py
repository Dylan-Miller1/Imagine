import sqlite3
import datetime

#Write prompt and keywords to database
def db_write(prompt, chatgpt_response):
    #Connect to database
    connection = sqlite3.connect("prompts.db")

    #Create cursor to database connection to execute commands
    cursor = connection.cursor()

    #Create Tuple to insert into table
    db_input = (str(datetime.datetime.now()), prompt, chatgpt_response)

    #Insert user date, prompt and response into database (no duplicates)
    cursor.execute("SELECT COUNT(*) FROM prompts WHERE user_keywords = ?", (db_input[1],))
    count = cursor.fetchone()
    if count[0] == 0:
        cursor.execute("INSERT INTO prompts VALUES (?,?,?)", db_input)

    #If db has more than 20 entries delete the oldest
    cursor.execute("SELECT COUNT(*) FROM prompts")
    number_entries = cursor.fetchone()[0]
    if number_entries > 20:
        cursor.execute("SELECT * FROM prompts ORDER BY entry_date ASC LIMIT 1")
        oldest_prompt = cursor.fetchone()
        oldest_id = oldest_prompt[0]
        cursor.execute("DELETE FROM prompts WHERE entry_date = ?", (oldest_id,))
        
    #Commit changes to database
    connection.commit()

    #Close database connection
    connection.close()

#Pull 20 most recent items in database
def db_get_recent():
    #Connect to database
    connection = sqlite3.connect("prompts.db")

    #Create cursor to database connection to execute commands
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM prompts ORDER BY entry_date DESC LIMIT 20")
    last_ten = cursor.fetchall()

    #Close database connection
    connection.close()
    return last_ten