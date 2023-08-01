import sqlite3

def db_create():
    #Create Database
    connection = sqlite3.connect("prompts.db")

    #create cursor to database connection to execute commands
    cursor = connection.cursor()

    #create table with columns "entry_date", "user_keywords" and "chatgpt_response".
    cursor.execute("create table prompts (entry_date text, user_keywords text, chatgpt_response text)")

    #commit changes
    connection.commit()

    #close the connection
    connection.close()