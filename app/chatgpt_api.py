import os
import openai

#Pull the environment variable for the chatGPT api key
openai.api_key = os.environ["chatgpt_api"]


#Get chatgpt response to user prompt
def get_chatgpt(prompt):
    #Create full prompt with instructions and user input
    prompt = "write me a dream day in the life that includes all of the following things: " + prompt

    #Request to chatgpt
    completion = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 500,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    
    #Pull first response from chatgpt
    response = completion.choices[0].text
    return response