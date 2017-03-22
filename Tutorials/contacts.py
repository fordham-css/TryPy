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
    def __init__(self, name, phone, address, email, nickname):
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
    print('You are going to add a contact to your book...')

    # Get new contact information
    name = raw_input('Please enter the persons name: ')
    phone = raw_input('Please enter the telephone number: ')
    address = raw_input('Please enter the address: ')
    email = raw_input('Please enter the email: ')
    nick = raw_input('Please enter the nickname (or leave blank for none): ')


    # Account for no nickname
    if nick == '':
        nick = None

    # Create new Contact Instance
    contact = Contact(name, phone, address, email, nick)

    # Save to DB
    db[phone] = contact # Store contact as value with key being phone number

    return True

# print_DB
# READ
# Prints all currently stored in DB
def print_DB(db):
    print('Printing database...')

    # Loop through dictionary to print values
    for value in db.values():
        print('Name: {}'.format(value.name))
        print('Phone: {}'.format(value.phone))
        print('Address: {}'.format(value.address))
        print('Email: {}'.format(value.email))

        if value.nickname:
            print('Nickname: {}'.format(value.nickname))

        print '-' * 75


# edit_contact
# UPDATE
# Edits a contact accessed through key [phone number]
def edit_contact(db):
    print('Going to update a record in the database...')

    # Print out key/value pairs
    # iteritems() will return a list of tuples that contain the key in the first position
    # and value in the second
    for key, value in db.iteritems():
        print '-' * 75
        print('Contact name: {}'.format(value.name))
        print('Contact phone number: {}'.format(key))
        print '-' * 75

    idx = raw_input('Please enter the phone number of the contact to edit: ')

    try:
        contact = db[idx]
        print('Going to update {}...'.format(contact.name))

        # Phone number is not reassigned due to its use as primary key
        # -> Is there a way around this?
        contact.name = raw_input('Please enter new name of contact: ')
        contact.address = raw_input('Please enter the new address: ')
        contact.email = raw_input('Please enter the new email: ')
        contact.nickname = raw_input('Please enter the new nickname (or leave blank for none): ')

        if contact.nickname == '':
            contact.nickname = None

        db[idx] = contact

        return True

    # ERROR CASE[3]: Contact with matching key not found in DB
    except KeyError:
        print('No contact found with phone number to edit: {}'.format(idx))
        print('Exiting update function...')

        return False


#delet_contact
# DELETE
# Deletes a particular contact from the DB
def delete_contact(db):
    print('Going to delete a record in the database...')

    # Print out key/value pairs
    for key, value in db.iteritems():
        print '-' * 75
        print('Contact name: {}'.format(value.name))
        print('Contact phone number: {}'.format(key))
        print '-' * 75

    idx = raw_input('Please enter the phone number of the contact to delete: ')

    try:
        contact = db[idx]

        # Confirm user wants to delete contact
        confirm = raw_input('Are you SURE you want to delete {} from your contacts? (y/n):'.format(contact.name))

        if confirm.lower() == 'y':
            del db[idx] # Deletes key/value pair in DB on key
            print('Deleted {} OK'.format(contact.name))
            return True

        else:
            print('{} will stay in DB...'.format(contact.name))

    # ERROR CASE[4]: Contact with matching key not found in DB
    except KeyError:
        print('No contact found with phone number to delete: {}'.format(idx))
        print('Exiting delete function...')

        return False


# main
# Driver of program; Calls other functions that do stuff
def main():
    db = open_DB()

    # Main Loop to control flow of program
    while True:
        print '*' * 75
        print('Main Menu')
        print '*' * 75
        print('Please select a command: ')
        print('1. Add a contact')
        print('2. Print the database')
        print('3. Edit a contact information')
        print('4. Delete a contact')
        print('5. Exit program')

        # Get user choice to run desired function
        choice = raw_input('> ')

        try:
            choice = int(choice)
            flag = True

            ### No switch/case in Python, so gonna have to do this the long way...
            # EXIT CASE
            if choice == 5:
                print('Thanks for stopping by!')
                break

            # Store a new contact
            elif choice == 1:
                flag = store_contact(db)

            # Print DB
            elif choice == 2:
                print_DB(db)

            # Edit Contact
            elif choice == 3:
                flag = edit_contact(db)

            # Delete Contact
            elif choice == 4:
                flag = delete_contact(db)

            # ERROR[5]: User enters in option not covered in menu
            else:
                print('ERROR[5]: Please enter a valid command (1-5)')
                flag = False

            if flag:
                print('[Operation successful...]')

        # ERROR CASE[4]: User enters string in Main Menu
        except ValueError:
            print('ERROR[4]: Menu choice must be an int, not a string')


    isClosed = close_DB(db)

    if isClosed:
        print('Closed {} OK'.format(DB_NAME))

# Entry Point of Script
if __name__ == '__main__':
    main()
