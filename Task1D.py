#Task 1: Data Structures Implementation (lists and data frames for managing books and
#members).
#Initialize two data structures to keep track of books and members both represented as lists. The system
#features two functions (You must create these functions): add_book and add_member. The add_book
#function takes three parameters (book_id, title, author, status) and appends a new book dictionary to
#the books list. The add_member function, on the other hand, requires two parameters (member_id,
#name) and appends a new member dictionary to the members list. Each member dictionary includes an
#empty list for borrowed_books to track the IDs of books each member has borrowed.
#Sequence hint: initialize two variables as lists, then create two functions as per the above requires. An
#example of the appending part of the question is as follows:
#books.append({
 #"book_id": book_id,
 #"title": title,
 #"author": author
 #})
#You must use the same procedure for all appends!
#Task 1 A:
#uppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a
#book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. How would these
#additions reflect in the books and members lists, and what would the output look like if you printed
#oth lists immediately after these additions?
#Hint: call the functions and write a print statement for them
#Task 1 B:
#Rewrite the entire task 1 and task 1B without using parameters and arguments in your functions.
#ask 1 C:
#Rewrite the entire task 1B without using functions
#ask 1 D:
#Rewrite the entire Task 1 C using Data frames instead of lists

import pandas as pd
book=[]
member=[]
books_df = pd.DataFrame(columns=["book_id","title","author","status"])
members_df =pd.DataFrame(columns=["member_id","name"])

books_df = books_df.append({"book_id": 2024001,
                             "title": "Python Programming", 
                             "author": "Jacob Zuma",
                               "status": "available"},
                                 ignore_index=True)

members_df = members_df.append({"member_id": 1,
                                 "name": "Anelisa Maleka",
                                   "borrowed_books": []},
                                     ignore_index=True)

print("book Dataframe")
print(books_df)

print("\nmember Dataframe")
print(members_df)


