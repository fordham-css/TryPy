'''
jeeves.py
----------
Robot to suggest outfit based on the weather
	- Variables
	- Conditionals
----------
Python Demo Workshop, March 22nd 2017
'''
#### Declaring variables in Python
# Good news: No need to lock variable to a type!
# Bad news: No real implementation of constant variable types...

# Integer Data Type
LOW_THRESHOLD = 35
HIGH_THRESHOLD = 80
JACKET_THRESHOLD = 40
SHORTS_THRESHOLD = 65

print('It is your robots first day on the job, so please introduce yourself: ')

# Declare and initialize a variable from user input
# String Data Type
name = raw_input('> ')

print('Great! He will be with you now..')

# Format print statement with name as paramater
print('Good day {0}'.format(name)) # Will place name in first position (zero indexed)
print('My name is Jeeves, your personal robot butler. Shall we settle on an outfit for today?')

# Get current weather temperature and condition
temp = raw_input('Now what is the temperature outside today?\n > ')
temp = int(temp) # IMPORTANT: raw_input returns a string, need to type cast to an int

condition = raw_input('Now would you say it is clear, cloudy, or overcast?\n > ')

# Error Checking on condition
condition = condition.lower() # For the purposes of comparison
if condition != 'clear' and condition != 'cloudy' and condition != 'overcast':
	print('You are being ridiculous..\nI shall not work with someone with such rude manner!')

	exit(1) # !! IF WE GOT HERE WE MESSED UP !! *#

### Branch to determine what outfit to wear

# Report on current temperature
if temp > HIGH_THRESHOLD:
	print('Goodness me it is hot today!')

elif temp < LOW_THRESHOLD:
	print('Sounds like a cold day outside, better bundle up!')

else:
	print('Seems like a moderate day today')

# Decide on what to wear based on weather condition
# Boolean Data Type
good_weather = True

if condition == 'cloudy' or condition == 'overcast':
	good_weather = False

if good_weather: # Will execute if good_weather == True
	if temp >= SHORTS_THRESHOLD:
		print('Fabulous news! It is nice enough outside to wear shorts! Rock a clean tee and get outside!')

	elif temp <= JACKET_THRESHOLD:
		print('Better bundle up, if you have to go outside definitely bring a jacket')

	else:
		print('Your call, remember jeans and a sweater bring it together')

else: # Executes on good_weather == False
	if temp >= SHORTS_THRESHOLD:
		print('Tough spot...try wearing dri fit shorts with a light rain jacket') 

	elif temp <= JACKET_THRESHOLD:
		print('Gonna be a tough go. Definitely go with a jacket, hat, and boots if need be')

	else:
		print('Try the layered look. Lightweight sweater under a rain jacket')

print('Hope you have a great day {0}!!!'.format(name))