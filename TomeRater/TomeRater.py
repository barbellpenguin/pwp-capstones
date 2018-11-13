#!/usr/bin/python3


#Create a User Class
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    #TypeError Unhashable
    def __hash__(self):
        return hash((self.name, self.email))


    #Return user's email
    def get_email(self):
        return self.email

    #Change email associated with a user
    def change_email(self, address):
        self.email = address
        print(self.name + " email has been updated to " + self.email)

    #Print user info
    def __repr__(self):
        return (self.name + " has address " + self.email + ".")

    #Compare users to see if they're the same
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            self.name = self.name
            self.email = self.email

    #Show books the user has read
    def read_book(self, book, rating=None):
        self.books[book] = rating        

    def get_average_rating(self):
        rating_scores = 0
        book_count = 0
        for item in self.books.keys():
            book_count +=1
            if self.books[item] is not None:            
                rating_scores += self.books[item]
        return (rating_scores / book_count)

#Create a Book Class
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    #Return book title
    def get_title(self):
        return self.title
 
    #Return isbn
    def get_isbn(self):
        return self.isbn

    #Set isbn to a new number and print the update
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print(self.title + "'s isbn has been updated.")

    #Add ratings to self.ratings list
    def add_rating(self, rating):
        try:
            if (0 <= rating <= 4):
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
        except TypeError:
            print("Invalid Type")

    #Compare books to see if they're the same
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            other_book = self

    #Show book's average rating by the users
    def get_average_rating(self):
        rating_scores = 0
        avg_rating = 0
        for value in self.ratings:
            rating_scores += value
        try: 
            avg_rating = rating_scores / len(self.ratings)
        except ZeroDivisionError:
            print("Empty ratings list.")
        return avg_rating

    #TypeError Unhashable
    def __hash__(self):
        return hash((self.title, self.isbn))

    #show book and isbn
    def __repr__(self):
        return (self.title + " with isbn " + str(self.isbn))
    
#Create Fiction Subclass
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    #Return author
    def get_author(self):
        return self.author

    #Show title by author
    def __repr__(self):
        return (self.title + " by " + self.author)


#Create Non-Fiction Subclass
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    #Return subject
    def get_subject(self):
        return self.subject

    #Return level
    def get_level(self):
        return self.level

    #Show book by subject and level
    def __repr__(self):
         return (self.title + ", a " + self.level + " manual on " + self.subject)


#Create TomeRater Class
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    #create a new book and return book object
    def create_book(self, title, isbn):
        print(title + " has been added to the catalog.")
        return Book(title, isbn)

    #create a fiction novel
    def create_novel(self, title, author, isbn):
        print(title + " has been added to the catalog.")
        return Fiction(title, author, isbn)

    #create a non-fiction book
    def create_non_fiction(self, title, subject, level, isbn):
        print(title + " has been added to the catalog.")
        return Non_Fiction(title, subject, level, isbn)

    #add a book to a user's record 
    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else: 
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email = email))

    #add a user with list of books they've read 
    def add_user(self, name, email, user_books=None):
        if email not in self.users:
            user = User(name, email)
            self.users[email] = user
            print("{name} has been added with email {email}.".format(name = name, email = email))
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)
            else:
                pass 
        else:
            print("That user already exists.") 

    #print all the book objects
    def print_catalog(self): 
        print("Catalog of Books:")
        for book in self.books.keys():
            print(book)

    #print all the user objects
    def print_users(self):
        print("List of Users:") 
        for user in self.users.values():
            print(user)

    #return the book that's been read the most
    def get_most_read_book(self):
        highest_book = 0 
        highest_book_name = ""
        for book in self.books.keys():
            if self.books[book] > highest_book:
                highest_book = self.books[book]
                highest_book_name = book.title
        return ("The most read book is " + highest_book_name)

    #return the book with the highest average rating
    def highest_rated_book(self):
        avg_rating = 0
        best_book = ""
        for book in self.books.keys():
            if book.get_average_rating() > avg_rating:
                avg_rating = book.get_average_rating()
                best_book = book.title
        return ("The highest rated book is " + str(best_book) + " with average rating of " + str(avg_rating))

    #return the user with the highest average rating
    def most_positive_user(self): 
        happy_user_rating = 0
        happy_user = ""
        for user in self.users.values():
            if user.get_average_rating() != None:
                avg_rating = user.get_average_rating()
                if avg_rating > happy_user_rating:
                    happy_user = user.name
                    happy_user_rating = avg_rating
        return ("The happiest user is " + happy_user + " with a rating of " + str(happy_user_rating))
