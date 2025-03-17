class Member:
    allMembers = 0
    members = []
    def __init__(self, Fname, Lname, Age, ID, email, password):
        self.Fname = Fname
        self.Lname = Lname
        self.Age = Age
        self.ID = ID
        self.email = email
        self.__password = password
        self.fullName = Fname + " " + Lname 
        Member.members.append(ID)
        Member.allMembers += 1

    def __str__(self): 
        return "Name: " + self.fullName + "\nAge: " + str(self.Age) + "\nID: " + str(self.ID) + "\nEmail: " + self.email + "\nPassword: " + self.__password
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password

    def register(self, Fname, Lname, Age, ID, email, password):
        Member.__init__(self, Fname, Lname, Age, ID, email, password)
        if self.ID in Member.members:                                # This Condition not working
            print("Sorry, This ID Is Already Registered")
        else: 
            print(f"Welcome {self.Fname} You Are Now Registered")
            Member.members.append(self.ID)

    def login(self, fullName, email):
        self.fullName = fullName
        self.email = email
        print(f"Welcome {self.fullName} You Are Now Logged In")


    def update_info(self, Fname, Lname, Age, ID, email, password):
        self.Fname = Fname
        self.Lname = Lname
        self.Age = Age
        self.ID = ID
        self.email = email
        self.__password = password
        print("Your Information Updated")

    def logout(self, password):
        self.password = password
        print(f"Goodbye {self.Fname} You Are Now Logged Out")

    def get_info(self, ID):
        self.ID = ID
        return self.__str__()

    
class book:
    catalog = []
    available = True
    def __init__(self, bookName, author, category, ISBN, book_price):
        self.bookName = bookName
        self.author = author
        self.category = category
        self.ISBN = ISBN
        self.book_price = book_price

    @classmethod
    def show_books_count(cls):      # Point to class itself not instance of class
        return len(cls.catalog)

    def search_book_by_name(self, bookname):
        self.bookname = bookname
        for book in book.catalog:
            if book.bookName == bookname:
                print("Book Is Found")
                return book
        print("Book Not Found")
    
    def search_book_by_author(self, author):
        self.author = author
        for author in book.catalog:
            if book.author == author:
                print("Book Is Found")
                return book
        print("Book Not Found")

    def search_book_by_category(self, category):
        self.category = category
        for category in book.catalog:
            if book.category == category:
                print("Book Is Found")
                return book
        print("Book Not Found")

    def check_book_status(self, bookname, available):
        self.bookname = bookname
        self.available = available
        if self.available == True:
            print("Book is Available")
        else:
            print("Book is Reserved")

    def get_book_info(self, bookName):
        for book in book.catalog:
            if book.bookName == bookName:
                print(f"Book Name: {book.bookName}\nAuthor: {book.author}\nCategory: {book.category}\nISBN: {book.ISBN}\nPrice: {book.book_price}")
                return
        print("Book not found!")

    
class Librarian(Member):
    def Add_book(self, bookName, author, category, ISBN, book_price):
        book.__init__(self, bookName, author, category, ISBN, book_price)
        book.catalog.append(bookName)
        print("Book Is Added")

    def remove_book(self, bookname):
        self.bookname = bookname
        if bookname in book.catalog:
            book.catalog.remove(bookname)
            print("Book Is Deleted")
        else:
            print("Sorry, Book Not Found")

    def edit_book_info(self, new_bookName, new_author, new_category, new_ISBN, new_book_price):
        for book in book.catalog:
            if book.bookName == new_bookName:  
                book.author = new_author
                book.category = new_category
                book.ISBN = new_ISBN
                book.book_price = new_book_price
                print("Book Information Updated")
                return
        print("Book not found!")
        book.catalog.update(new_bookName, new_author, new_category, new_ISBN, new_book_price)

    def check_payment(self, bookName, book_price, payment):
        self.bookName = bookName
        self.book_price = book_price
        self.payment = payment
        if  book_price == payment:
            print("Payment Is Done")
        elif payment < book_price:
            print("You Need To Pay The Full Amount")
        else:
            print("Payment Is Done And The Remaining Amount Is: ", payment - book_price)

    def search_Member(self, ID):
        self.ID = ID
        for member in Member.members:
            if member.ID == ID:
                print("Member Is Found", member.get_info())
                return
        print("Member Is Found")

    def check_max_limit_of_books(self,customerID, num_of_books):
        self.customerID = customerID
        self.num_of_books = num_of_books
        if  Customer.number_of_books < 5:
            print("Customer Can Borrow More Books")
        elif Customer.number_of_books == 5:
            print("Customer Has Reached The Maximum Limit Of Books")
        else:
            print("Customer can not borrow more books")


class Customer(Member):
    number_of_books = 0
    def borrow_book(self, bookname, customerID):
        self.bookname = bookname
        self.customerID = customerID
        if self.available == True:
            print("Book Borrowed, You Have 10 Days To Return It")
            number_of_books += 1
        else:
            print("Sorry, Book is Not Available Now You Can Reserve It For Later")

    def return_book(self, bookname, customerID):
        self.bookname = bookname
        self.customerID = customerID
        print("Book Returned")
        number_of_books -= 1

    @staticmethod
    def reserve_book(self, bookname, customerID):
        self.bookname = bookname
        self.customerID = customerID
        if self.available == False:
            print("Book Reserved")
        else:
            print("Book is Available Now You Can Borrow It")


# Create member instances
Librarian1 = Librarian("Norhan", "Gamal", 22, 12345, "norhangamal123@gmail.com", "2468")
print(Librarian1)
customer1 = Customer("Ahmed", "Ali", 25, 67890, "ahmedali123@gmail.com", "13579")
print(customer1)
print(Member.allMembers)

# Register
Librarian1.register("Haidy", "Gamal", 22, 12345, "norhangamal123@gmail.com", "2468")
print(Member.allMembers)

# Login
Librarian1.login("Norhan Gamal", "norhangamal123@gmail.com")

# Update Info
Librarian1.update_info("Norhan", "Gamal", 23, 12345, "norhangamal123@gmail.com", "2468")
print(Librarian1.get_info(12345))

# Logout
Librarian1.logout("norhangamal123@gmail.com")

# Add Book
Librarian1.Add_book("Python Programming", "John Smith", "Programming", 123456789, 100)
Librarian1.Add_book("Java Programming", "John Smith", "Programming", 987654321, 150)
Librarian1.Add_book("C++ Programming", "John Smith", "Programming", 456789123, 200)
print(book.catalog)

# Remove Book
Librarian1.remove_book("Python Programming")
print(book.catalog)

# Check Payment
Librarian1.check_payment("Python Programming", 100, 80)
Librarian1.check_payment("Python Programming", 100, 100)
Librarian1.check_payment("Python Programming", 100, 120)

# Not the best and may have some errors but I will try to improve it later..   
