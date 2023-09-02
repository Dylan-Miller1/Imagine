from flask import Flask, render_template, request, redirect, url_for
import os
from chatgpt_api import get_chatgpt
from database_interaction import db_write, db_get_recent

app = Flask(__name__)

#Home page for user to input keywords
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        #Pull user keywords from the form
        user_keywords = request.form["keywords"]

        #Feed the keywords to ChatGPT for a response
        chatgpt_response = get_chatgpt(user_keywords)

        #Send the keywords/repsonse to the results page for the user to view
        return redirect(url_for('results',user_keywords=user_keywords, chatgpt_response=chatgpt_response))
    else:
        return render_template('home.html')
    
#Results page: View response, gives option to share to DB
@app.route("/results", methods=["GET", "POST"])
def results():
    #Assign query parameters from home page
    user_keywords = request.args.get('user_keywords')
    chatgpt_response = request.args.get('chatgpt_response')
    
    if request.method == 'POST':
        #Write to DB
        db_write(user_keywords, chatgpt_response)
        #Redirect to shared page
        return redirect(url_for('shared'))
    else:
        #Render results page with chatgpt repsonse
        return render_template('result.html', chatgpt_response=chatgpt_response)

#Shows prompts/responses from DB (submitted by users)
@app.route("/shared", methods=["GET", "POST"])
def shared():
    posts = db_get_recent()
    return render_template('shared.html', posts=posts)

#Shows all the tools used in this project
@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)