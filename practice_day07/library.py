import json
class Library:
    Lib_name="AIR UNIVERSITY LIBRARY"
class Book():
    def __init__(self,code,name,author,total_copies,available_copies):
        self.__code=code
        self.__name=name
        self.__author=author
        self.__total_copies=total_copies
        self.__available_copies=available_copies
    def add_books(self):
        try:
            with open("books.json","r") as f:
                data=json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            data={self.__code:{"name":self.__name,"author":self.__author,"total_copies":self.__total_copies,"available_copies":self.__available_copies}}
        else:
            data[self.__code]={"name":self.__name,"author":self.__author,"total_copies":self.__total_copies,"available_copies":self.__available_copies}
        finally:
            with open("books.json","w") as f:
                json.dump(data,f,indent=4)           
            print("Added successfully! ")
        while True:
            i=input("Enter 'next' for main menu: ")     
            if i=='next':
                break

class member:
    def __init__(self, Id, name):
        self.__ID = Id
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

            print("available books: ", books[code]["available_copies"])
        
            
            if books[code]["available_copies"] >= 1:
                books[code]["available_copies"] -= 1
                with open('books.json', 'w') as f:
                    json.dump(books, f, indent=4)
                return code, books[code]["name"]
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
                books[code]["available_copies"]+=1
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
    c=int(input("---Main menu---\n1.borrow book\n2.return book\n3.Add book\n4.main menu\n5.Exit\npress choice number: "))
    if c==1:
        member.borrow_book()
    elif c==2:
        member.return_book()
    elif c==3:
        code=input("Enter code:")
        name=input("Enter book name: ")
        author=input("Enter author name: ")
        total=int(input("Enter no. of total copies: "))
        available=int(input("Enter no. of available copies: "))
        book=Book(code,name,author,total,available)
        book.add_books()
        del book

    elif c==4:
        continue
    elif c==5: 
        break
    else:
        print("Incorrect choice! try again.")

