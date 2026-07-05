from cryptography.fernet import Fernet

master_pwd = input("What is your master password: ")


# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)


def load_key():
    with open('key.key', 'rb') as key_file:
        return key_file.read()

   

  
key = load_key()
fer = Fernet(key)

if master_pwd == "bharathi2003":
    print("Login success!")
else:
    print("Invaid password")
    quit()

def add():
    name = input("Account name ")
    pwd = input("password ")
    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n" )
       

def view():
    with open('password.txt' , 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,password = data.split('|')
            print("user:" , user, "| password:", fer.decrypt(password.encode()).decode())


while True:
    mode = input("Would you like to 'add' a new password or 'view' an existing password or 'q' to quit ").lower()

    if mode == "q":
        break

    if mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("Invalid mode")
        quit()


