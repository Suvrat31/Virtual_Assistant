import json
def analysis(command,command_sentence):
    if("youtube" == command):
        temp_var=input("Do you want to open YOUTUBE, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            youtube(command_sentence)
        else:
            google(command)
    elif("wikipedia" == command):
        temp_var=input("Do you want to open WIKIPEDIA, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            wikipedia(command_sentence)
        else:
            google(command)
    elif("reboot" == command):
        temp_var=input("Do you want to REBOOT, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            reboot()
        else:
            google(command)
    elif("update" == command):
        temp_var=input("Do you want to UPDATE your computer, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            update()
        else:
            google(command)
    elif("weather" == command):
        temp_var=input("Do you want to the WEATHER, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            google(command)
        else:
            google(command)
    elif("spotify" == command):
        temp_var=input("Do you want to open SPOTIFY, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            spotify()
        else:
            google(command)
    elif("time" == command):
        temp_var=input("Do you want to get the TIME, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            time()
        else:
            google(command)
    elif("ip" == command):
        temp_var=input("Do you want to know the IP ADDRESS, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            ip()
        else:
            google(command)
    elif("compile_prog" == command):
        temp_var=input("Do you want to COMPILE the program, enter yes: ")
        if(temp_var.lower()=="yes"):
            with open('data.json', 'r') as fp:
                training_data = json.load(fp)
            training_data.append({"class" : command, "sentence" : command_sentence})
            with open('data.json', 'w') as fp:
                json.dump(training_data, fp)
            compile_prog(command_sentence)
        else:
            google(command)

    else:
        google(command)
        
        
        
        
def wikipedia(command):
    import webbrowser
    url="https://en.wikipedia.org/wiki/" + command
    webbrowser.open(url)

def youtube(command):
    import re
    import webbrowser
    import urllib
    reg_ex = re.search("youtube (.+)", command)
    if reg_ex:
       domain = command.split("youtube", 1)[1]
       query_string = urllib.parse.urlencode({"search_query": domain})
       html_content = urllib.request.urlopen(
           "http://www.youtube.com/results?" + query_string
       )
       search_results = re.findall(
           r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
       )
       # print("http://www.youtube.com/watch?v=" + search_results[0])
       webbrowser.open(
           "http://www.youtube.com/watch?v={}".format(search_results[0])
       )
       pass

           #  weather forecast in your city (e.g. weather in London)
           # please create and use your own API it is free
def google(command):
    import webbrowser
    url="https://www.google.com/search?q="+command
    webbrowser.open(url)
def reboot():
    import os
    os.system("reboot")
def spotify():
    import os
    os.system("spotify")
def time():
    import os
    os.system("date")
def ip():
    import os
    os.system("ifconfig")
def weather():
    import webbrowser
    string1="weather today"
    url="https://www.google.com/search?q="+string1
    webbrowser.open(url)
def compile_prog():
    #do something
    print(1)
def update():
    import os
    os.system("sudo apt-get update")
    
