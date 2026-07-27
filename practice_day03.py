gmail=" "
password=" "
def register():
    while True:
        name=input("Enter your name: ")
        name=name.title().strip()
        name=name.replace("!","").replace("@","").replace("#","").replace("$","").replace("_","").replace("-","").replace("%","").replace("&","").replace("^","").replace("(","").replace(")","").replace(",","").replace(":","").replace("~","")
        iscorrect=True
        for n in name:
            if n in "0123456789":
                iscorrect=False
        if iscorrect:
            break
        else:
            print ("Invalid name! enter again.")
                

    while True:
        gmail=input("Enter your gmail: ")
        gmail=gmail.lower().strip()
        if "." in gmail and "@" in gmail:
            break
        else:
            print ("Invalid email! enter again. ")

    while True:
        gender=input("Enter Gender: ")
        gender=gender.lower().strip()
        if gender=="male" or gender=="female":
            break
        else:
            print("Invlid! enter again.")
    while True:
        password=input("Enter password of atleast 8 characters: ")
        iscorrect=True
        if (len(password)<8):
            print("password must contain atleast 8 characters. ")
            continue
        has_alphabet=any(char.isalpha() for char in password)
        has_digit=any(ch.isdigit() for ch in password)
        has_special= any (ch in "!@#$%^&*<>:?~_-:;" for ch in password)
        if has_alphabet and has_digit and has_special and iscorrect:
            break
        else:
            print("your password always have alphabet, digit and special character")
            print("Try agian!")
    while True:
        c_password=input("confirm your password: ")        
        if c_password==password:
            break
        else:
            print("must match the password. try agian!")
    print("CONGRATULATION! you got registered")
    c=int(input("press 1 to sign in!"))
    if c==1:
        sign_in()

def sign_in():
    user=input("Enter your gmail: ")
    pas=input("Enter password: ")
    if user==gmail and pas==password:
        print("WELCOME! You logged in ")

    
print("register your self here! ")
register()


