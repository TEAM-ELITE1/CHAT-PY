
import os, random,sys

try:
    import openai
except:
    os.system("pip install openai")
    import openai
try:
    import rich
except:
    os.system("pip install rich")
    import rich

from rich import print
from rich import print_json
from rich import pretty
from rich.panel import Panel
from rich.markdown import Markdown 
pretty.install()


try:
    import gtts
except:
    os.system("pip install gtts")
    import gtts
from gtts import gTTS

def create_(text,file):
    my_a = gTTS(text)
    my_a.save(file)


def play_audio(audio_file):
    os.system("play-audio "+audio_file)

def dual(text,file):
    create_(text,file)
    play_audio(file)
logo="""
[bold violet]  ___  _  _   __  ____     ____  _  _ 
 / __)/ )( \ / _\(_  _)___(  _ \( \/ )
( (__ ) __ (/    \ )( (___)) __/ )  / 
 \___)\_)(_/\_/\_/(__)    (__)  (__/  
 """
develop={
"FACEBOOK":"HERON AFRIDI",
"MAIN WORK":"Data Analyst",
"TEAM":"ELITE",
}
welcome=["Give cradite for Team Elite","Hello world, my name is Kaitlyn.","System Started successfuly","hey, learner welcome to CHat-PY","Welcome ,I am A.I"]






#------------------------------------------------#
# todo Authorization 👇
#openai.api_key_path ="/sdcard/key.txt"
#openai.api_key =""
"""
এই খানে দুই টা Authorization system আছে
[1] openai.api_key_path
[2] openai.api_key

প্রথম টি দিয়ে Authorization করার জন্য openai website থেকে
একটি api_key তৈরি করে একটা txt file এর ভিতর রাখুন এবং
ফাইল লোকেশন দিয়ে দিন |উদাহরণ /sdcard/api_key.txt

দ্বিতীয় টি দিয়ে Authorization করার জন্য আপনার api key টা কপি করুন
এবং openai.api_key ="your key" 👈 এই ভাবে কি বসবেন

আপনি আপনার প্রোগ্রাম এ ২ টি Authorization এর যে কোনো
একটি ইউজ করতে পারবেন ইউজ করার জন্য ৬১ বা ৬২ নাম্বার লাইনের # হেস কেটে দিন

এইবার বলি আপনি api_key কোথায় পাবে ,তার জন্য আপনার
https://platform.openai.com/account/api-keys
এই ওয়েব সাইট এ একটা একাউন্ট করতে হবে এবং লিংক টা দ্বিতীয় বার
ওপেন করলেই আপনারা api_key মেক এর পেজে চলে যাবেন
---------------------
আমি Heron Afridi
এই প্রজেক্ট টি ওপেন সোর্স
হিসাবে আপলোড দিচ্ছি , দয়া করে
এটা কেউ সেল দিবেন না ,
ভালো থাকবেন 

"""

#------------------------------------------------#


def heron_afridi():
    os.system("clear")
    print(Panel.fit(logo))
    print_json(data=develop)
    print(Markdown("\n- This Tool Is Only For __Learning__ Anything\n- Use It For **Fatch** Information & Data "))
    jk=random.choice(welcome)
    dual(jk,"n.mp3")
    while True:
        prompt = input ("\n\n\n[ Give Question ? ] >")
        response = openai.Completion.create(engine="text-davinci-002",prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.5,)
        generated_text = response["choices"][0]["text"]
        reply=Markdown("# "+prompt.upper())
        print("\n\n")
        print(reply)
        print(f"\n\n[bold green] {generated_text}")
        dual(generated_text,"n.mp3")

heron_afridi()
