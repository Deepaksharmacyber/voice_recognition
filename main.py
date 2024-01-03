import random
import webbrowser
import pyjokes
import speech_recognition as sr
import win32com.client
import datetime
import os
import subprocess
import openai
import requests
import winshell
import wolframalpha

from config import apikey


def get_latest_news(api_key):
    # Function to get the latest news headlines
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

    try:
        response = requests.get(url)
        news_data = response.json()

        if news_data['status'] == 'ok':
            articles = news_data['articles']

            # Read the latest news headlines
            for index, article in enumerate(articles):
                title = article['title']
                speaker.Speak(f"News {index + 1}: {title}")
        else:
            speaker.Speak("Unable to fetch news. Please try again later.")

    except Exception as e:
        speaker.Speak(f"An error occurred: {str(e)}")



def open_camera():
    try:
        # Open the default camera application on Windows
        subprocess.run(["start", "microsoft.windows.camera:"], shell=True)
        speaker.Speak("Opening the camera...")
    except Exception as e:
        print(f"Error opening the camera: {e}")

# def ai(prompt):
#     openai.api_key = apikey
#     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
#
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     # todo: Wrap this inside of a  try catch block
#     # print(response["choices"][0]["text"])
#     text += response["choices"][0]["text"]
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")
#
#     # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
#     with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
#         f.write(text)



def open_file_explorer_folder(path):
    # Check if the path existsSs
    if os.path.exists(path):
        # Use subprocess to run the system-specific command
        subprocess.Popen(['explorer', path], shell=True)
        print(f"File Explorer opened at: {path}")
    else:
        print("Invalid path. Please provide a valid folder path.")

speaker = win32com.client.Dispatch("SAPI.SpVoice")





def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said :{query}")
            return query
        except Exception as e:
            return "Some Error Occurred.Sorry form Jarvis"





while 1:
    print("enter the word you want to speak it out by computer")
    # s=in put()
    speaker.Speak("Hello I am Jody AI assistant")
    while True:
        print("Listening.....")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://google.com"], ["instagram", "https://www.instagram.com"],
                 ["Stack overflow", "https://stackoverflow.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} sir....")
                webbrowser.open(site[1])





        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"Sir the time is {strfTime}")




        elif 'play music' in query or "play song" in query:
            speaker.Speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\pictures\\instagrampics\\Musi"
            songs = os.listdir(music_dir)
            print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))
            # random = os.startfile(os.path.join(music_dir, songs[0]))


        elif 'how are you' in query:
            speaker.Speak("I am fine, Thank you")
            speaker.Speak("How are you, Sir")


        elif 'fine' in query or "good" in query:
            speaker.Speak("It's good to know that your fine")




        elif 'open Chrome' in query:
            browser_paths = {'chrome':'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'}
            browser_name = "chrome"
            speaker.Speak("open chrome")
            webbrowser.register(browser_name,None, webbrowser.BackgroundBrowser(browser_paths[browser_name]))
            webbrowser.get(browser_name).open("")




        elif 'open Brave' in query:
            browser_paths = {'brave':'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'}
            browser_name = "brave"
            speaker.Speak("open Brave ")
            webbrowser.register(browser_name,None, webbrowser.BackgroundBrowser(browser_paths[browser_name]))
            webbrowser.get(browser_name).open("")




        elif 'open Microsoft edge' in query:
            browser_paths = {'Microsoft edge':'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'}
            browser_name = "Microsoft edge"
            speaker.Speak("open microsoft edge")
            webbrowser.register(browser_name,None, webbrowser.BackgroundBrowser(browser_paths[browser_name]))
            webbrowser.get(browser_name).open("")





        elif 'open Visual Studio code' in query:
            browser_paths = {'Visual Studio code':'C:\\Users\\dell\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'}
            browser_name = "Visual Studio code"
            speaker.Speak("open Visual Studio Code")
            webbrowser.register(browser_name,None, webbrowser.BackgroundBrowser(browser_paths[browser_name]))
            webbrowser.get(browser_name).open("")





        elif 'open Android studio' in query:
            browser_paths = {'Android studio':'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe'}
            browser_name = "Android studio"
            speaker.Speak("open Android studio")
            webbrowser.register(browser_name,None, webbrowser.BackgroundBrowser(browser_paths[browser_name]))
            webbrowser.get(browser_name).open("")





        elif 'open playit' in query:
            browser_paths = {'PLAYit':'C:\Program Files (x86)\PLAYit\PLAYit.exe'}
            browser_name = "PLAYit"
            speaker.Speak("PLAYit")
            webbrowser.register(browser_name,None, webbrowser.BackgroundBrowser(browser_paths[browser_name]))
            webbrowser.get(browser_name).open("")






        elif 'joke' in query:
            speaker.Speak(pyjokes.get_joke())



        elif 'open camera' in query:
            open_camera()

        #to open only file explorer not any specfic folder
        # elif 'open file explorer' in query:
        #     subprocess.Popen(['explorer'], shell=True)
        #     speaker.Speak(f"File Explorer opened ")


        elif 'open file explorer' in query:
            folder_path = r'C:\pictures\instagrampics'  # Replace with your desired folder path
            open_file_explorer_folder(folder_path)

        # elif "Using artificial intelligence".lower() in query.lower():
        #     ai(prompt=query)


        elif 'get latest news' in query:
            news_api_key = 'acb1e63e54474d239f3f1c07749c23ad'
            get_latest_news(news_api_key)




        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speaker.Speak("User asked to Locate")
            speaker.Speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")



        elif "who are you" in query:
            speaker.Speak("I am your virtual assistant created by Deepak")

        # elif 'empty recycle bin' in query:
        #     winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        #     speaker.Speak("Recycle Bin Recycled")

        elif "write a note" in query:
            speaker.Speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speaker.Speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speaker.Speak("Showing Notes")
            file = open("jarvis.txt", "r")
            notes = file.read()
            # print(notes)
            speaker.Speak(notes[:])
            file.close()



        elif 'shutdown system' in query:
            speaker.Speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('C:\\Windows\\System32\\shutdown.exe /p /f')


        elif 'exit' in query:
            speaker.Speak("Thanks for giving me your time")
            exit()






