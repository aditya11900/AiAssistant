import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import pyttsx3
import random
import numpy as np

# Initialize chatStr outside the chat function
chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "Api-Key"
    chatStr += f"Aditya: {query}\n Jarvis: "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
   messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": chatStr}
    ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Update the global chatStr variable with the response
    chatStr += f"{response['choices'][0]['message']['content']}\n"
    # todo: Wrap this inside of a  try catch block
    say(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']


def ai(prompt):
    openai.api_key = "Api-key"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    print("Saying:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "C:\\Users\\hp\\Downloads\\song.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "C:\\Users\\hp\\Downloads\\song.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open zoom".lower() in query.lower():
            os.system(f"open /C:/Users/hp/AppData/Roaming/Zoom/bin/Zoom.exe")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
