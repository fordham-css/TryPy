'''
conatcts.py
----------
Contact Book Application to CRUD personal contacts via a shelve DB
    - Functions
    - Objects
    - Modules
----------
Python Demo Workshop, March 22nd 2017
'''
### Import Modules
import shelve # Database Management Module [https://docs.python.org/2/library/shelve.html]
import os

# Database Name
DB_NAME = '.Contacts.db'

### Contact Class
# Python Class definiton of model used to represent personal contacts
class Contact():

    # Constructor Method
    def __init__(self, name, phone, address, email, nickname=None):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.nickname = nickname

# open_DB
# Returns open instance of shelve object
def open_DB():
    try:
        db = shelve.open(DB_NAME)

        # Syntax to check if db was opened properly
        # Verbose condition needed, as first time DB is opened it is empty
        #   -> Checking <if db> would not display confirmation, even though its true
        if db is not None:
            print('Opened DB to read: {0}'.format(DB_NAME))

        return db

    # ERROR CASE[1]: Unable to open Database
    except Exception:
        print('ERROR[1]: Unable to open Database')
        print('Exception information: {0}'.format(e))

        exit(1) # !! IF WE GOT HERE WE MESSED UP !! *#


# close_DB
# Closes instance of shelve object
def close_DB(db):
    try:
        db.close()
        return True

    # ERROR CASE[1]: Unable to close Database
    except Exception:
        print('ERROR[2]: Unable to open Database')
        print('Exception information: {0}'.format(e))

        exit(2) # !! IF WE GOT HERE WE MESSED UP !! *#


# store_contact
# CREATE
# Creates and saves new Contact object to DB
def store_contact(db):
    pass


# print_DB
# READ
# Prints all currently stored in DB
def print_DB(db):
    pass


# edit_contact
# UPDATE
# Edits a contact accessed through key [phone number]
def edit_contact(db):
    pass


#delet_contact
# DELETE
# Deletes a particular contact from the DB
def delete_contact(db):
    pass


# main
# Driver of program; Calls other functions that do stuff
def main():
    pass

# Entry Point of Script
if __name__ == '__main__':
    main()
