def define_usr_fun():
    import json
    trigger_word=input("Enter the trigger for your command")
    usr_command=input("Enter the correct Bash command")
    with open('usr_triggers.json', 'r') as fp:
                usr_triggers= json.load(fp)
    usr_triggers.append(trigger_word)
    with open('usr_triggers.json', 'w') as fp:
                json.dump(usr_triggers, fp)
    with open('usr_fn.json', 'r') as fp:
                usr_fn= json.load(fp)
    usr_fn[trigger_word]=usr_command
    with open('usr_fn.json', 'w') as fp:
                json.dump(usr_fn, fp)
def run_usr_fun(trigger_word):
    import json
    import os
    with open('usr_fn.json', 'r') as fp:
                usr_fn= json.load(fp)
    command_to_run=usr_fn[trigger_word]
    os.system(command_to_run)
    
