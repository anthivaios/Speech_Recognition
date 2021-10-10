import subprocess
import pafy,youtube_dl
import vlc
import speech_recognition as sr
import webbrowser,time
from time import ctime
import pyttsx3

names = ["hey Coco", "Coco"]
def activate():
    command_level = False
    while 1 :
        l = audio_record(command_level)
        print("notin")
        print(l[0])
       

        if any(x in l[0] for x in names):
            command_level = True
            Speak("How can i help you")
            while 1:
                l = audio_record(command_level)
                command_level = l[1]
                
                print(l[0])
                respond(l[0])
                
                Speak("Do you need anything else")
                ans = audio_record(command_level)
                print(ans)
                yeap = ["yes", "yep"]
                nope = ["no", "nope"]
                if  any(x in ans for x in yeap):
                    Speak("how can i help you")
                    continue
                if  any (x in ans for x in nope):
                    Speak("let me know when you need me")
                    command_level = False
                    break
                Speak("Bye")
                command_level = False
                break
                    


def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def audio_record(command_level):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        r.pause_threshold= 0.6
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            print("Sorry didn't get that!")
            if command_level:
                Speak("Maybe next time")
                command_level = True
                
        except sr.RequestError:
            print("Speech servise is Down")
    return [voice_data, command_level]



def respond(voice_data):
    if "what is your name" in voice_data:
        Speak("my name is koko")
    if "what time is it" in voice_data:
        print(ctime())

    if "search" in voice_data:
        Speak("what do you want to search for?")
        search = audio_record(True)
        msg ="Here is what i found for " + search[0]
        url = "http://google.com/search?q="
        url+= search[0].replace(" ", "+")
        print(url)
        webbrowser.open(url)
        #chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        #chrome_browser.open_new_tab(url)
        Speak(msg)
    
    if "exit" in voice_data:
        exit()

    if "what do I have" in voice_data:
        print("mphka")
        url = "https://www.youtube.com/watch?v=0W8aX1uaNuU"
        video  = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.add_option('start-time=15.0')
        Media.add_option('run-time=60.0')
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        time.sleep(10)
        player.stop()

    if "cancer" in voice_data:
        subprocess.call("C:\Riot Games\Riot Client\RiotClientServices.exe")
        
       

activate()


