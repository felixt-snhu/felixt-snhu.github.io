from management import Trader
from management import Manager
import json
import chr2hex
import getpass
import re

# function to parse user choice when logging in as manager or trader
def request_prompt():
    execute_prompt = input("Execute as (m)anager or (t)rader: ")
    while not re.match('m|t', execute_prompt):
        print("Invalid option, type either 'm' or 't'")
        execute_prompt = input("Execute as (m)anager or (t)rader: ")
    return execute_prompt

if __name__ == "__main__":
    with open('users.json') as users_file:
        data = json.load(users_file)

    user = input("Username: ")
    password = getpass.getpass(prompt="Enter Password, then press ENTER: ")
    try:
        if data[user] == chr2hex.encode(password):
            print("Welcome, %s!" % user)
            prompt_response = request_prompt()
            if prompt_response == "m":
                print("Executing as manager")
                t = Manager()
            if prompt_response == "t":
                print("Executing as trader")
                t = Trader()
        else:
            print("Incorrect passwword")
    except KeyError:
        print("Username does not exist")
