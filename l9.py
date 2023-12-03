import json


def read():
    try:
        with open("data_file_with_users.json", "r") as f_json:
            read = json.load(f_json)
        return read
    except FileNotFoundError:
        print('At first you need to join')


def write(new_data):
    users = read()
    if users == None:
        users = []
    users.append(new_data)
    with open("data_file_with_users.json", "w") as f_json:
        json.dump(users, f_json)


def your_choice():
    choice = input("choose what would you like to do (log in or join)")
    return choice


def app(your_choice):
    spisok = your_choice()
    if "join" in spisok:
        email = input('your email')
        user = read()
        for account in user:
            if account['email'] == email:
                print("already exists")
                quit()
            else:
                ...
        while True:
            password1 = input('password')
            password2 = input('password')
            if password1 == password2:
                new_data = {"email": email, "password": password1}
                write(new_data)
                print("Registartion is over ")
                quit()
    if "log in" in spisok:
        while True:
            email1 = input('your email')
            password1 = input('password')
            new_data = {"email": email1, "password": password1}
            write(new_data)
            users = read()
            for i in users:
                if email1 == i["email"] and password1 == i["password"]:
                    print("Welcome!")
                    quit()
                else:
                    ...


app(your_choice)
