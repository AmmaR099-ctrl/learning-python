import json

class member:
    def __init__(self, Id, name):
        self.__ID = str(Id)
        self.__name = name
        self.__borrow_books = []

    def add_members(self):
        with open("member.json", "r") as f:
            data = json.load(f)
        data[self.__ID] = [self.__name, self.__borrow_books]
        with open('member.json', 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def borrow_book():
        Id = input("what is your ID: ")
        with open("member.json", "r") as f:
            members = json.load(f)

        if Id not in members:
            print("Invalid Member ID!")
            return

        print("name: ", members[Id][0], "\nborrowed books: ", members[Id][1])
        
        if len(members[Id][1]) < 5:
            i = input("Enter 'y' if you want to borrow book: ")
            if i == 'y':
                result = member.check_book()
                
                # Check if check_book() actually returned a book (not None)
                if result is not None:
                    code, name = result
                    members[Id][1].append([code, name])
                    
                    # FIX 1: Save updated borrowed list back to member.json!
                    with open("member.json", "w") as f:
                        json.dump(members, f, indent=4)
                    print("Book borrowed successfully!")
            else:
                return
                        
    @staticmethod    
    def check_book():
        code = input("code of book: ")
        
        with open("books.json", "r") as f:
            books = json.load(f)
            
        if code not in books:
            print("Book code not found!")
            return None

        print("available books: ", books[code][3])
        
        # FIX 3: Changed > 1 to >= 1 (or > 0)
        if books[code][3] >= 1:
            books[code][3] -= 1
            with open('books.json', 'w') as f:
                json.dump(books, f, indent=4)
            return code, books[code][0]
        else:
            print("Not available!")
            # FIX 2: Returns None safely so unpack doesn't crash
            return None

member.borrow_book()