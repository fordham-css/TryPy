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
