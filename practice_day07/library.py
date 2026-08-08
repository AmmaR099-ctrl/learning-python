import json

class member:
    def __init__(self, Id, name):
        self.__ID = str(Id)
        self.__name = name
        self.__borrow_books = []

    def add_members(self):
        try:    
            with open("member.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            data={self.__ID:[self.__name,self.__borrow_books]}
            
        else:
            data[self.__ID] = [self.__name, self.__borrow_books]
        finally:
            with open('member.json', 'w') as f:
                json.dump(data, f, indent=4)

    @staticmethod
    def borrow_book():
        Id = input("what is your ID: ")
        try:
            with open("member.json", "r") as f:
                members = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            print("file missing!")
            return None
        else:
            if Id not in members:
                print("Invalid Member ID!")
                return

            print("name: ", members[Id][0], "\nborrowed books: ", members[Id][1])
            
            if len(members[Id][1]) < 5:
                i = input("Enter 'y' if you want to borrow book: ")
                if i == 'y':
                    result = member.check_book()
                    
                    if result is not None:
                        code, name = result
                        members[Id][1].append([code, name])
                            
                        with open("member.json", "w") as f:
                            json.dump(members, f, indent=4)
                        print("Book borrowed successfully!")
                else:
                    return
                        
    @staticmethod    
    def check_book():
        code = input("code of book: ")
        try:
            with open("books.json", "r") as f:
                books = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            print("file missing!")
            return None
        else:        
            if code not in books:
                print("Book code not found!")
                return None

            print("available books: ", books[code][3])
        
            
            if books[code][3] >= 1:
                books[code][3] -= 1
                with open('books.json', 'w') as f:
                    json.dump(books, f, indent=4)
                return code, books[code][0]
            else:
                print("Not available!")
            
                return None
    @staticmethod
    def return_book():
        Id=input("what is your Id? ")
        try:
            with open('member.json','r') as f:
                data=json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            print ("File missing!")
            return None
        else:
            if Id not in data:
                print("Invalid ID!")
                return None
        code=input("Enter code of book: ")
        try:
            with open ("books.json","r") as f:
                books=json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            print ("file misssing!")
            return None
        else:
            if code not in books:
                print("Incorrect code")
                return None
        i=0
        for book in data[Id][1]:
            if book[0]==code:
                data[Id][1].remove(book)
                books[code][3]+=1
                i+=1
                break
        if i==0:
            print("No book is borrowed! ")
        with open("member.json","w") as f:
            json.dump(data,f,indent=4)
        with open("books.json","w") as f:
            json.dump(books,f,indent=4)
            
# member.borrow_book()
while True:
    c=int(input("---Main menu---\n1.borrow book\n2.return book\n3.main menu\n4.Exit\npress choice number: "))
    if c==1:
        member.borrow_book()
    elif c==2:
        member.return_book()
    elif c==3:
        continue
    elif c==4:
        break
    else:
        print("Incorrect choice! try again.")

