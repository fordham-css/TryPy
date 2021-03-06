'''
scrapy.py
----------
Program to retrieve quotes from a given author from the
website Brainyquote.com
    - Web Scraping
    - Requests
----------
'''
import requests  # For sending requests
import bs4  # For parsing HTML

# Get the author to search for
author = raw_input('Author to search for: ')

# Send a request to brainyquote.com with the author formatted in the URL
# get() method will return a Response object
# You need to pass get() the URL of the site you are trying to get the HTML of
# You can do a lot of things with a Reponse object like get the JSON of the page,
# get the HTML of a page, etc...
response = requests.get('http://brainyquote.com/search_results.html?q={}'
                        .format(author))

# Check to ensure page was downloaded correctly
# Will raise an exception if error occurred (non 200 response code)
# Good practice to call right after making a request
response.raise_for_status()

# Create a BeautifulSoup Object
# Allows us to parse the text retrieved from brainyquote.com
# You can specify the parser to use, by default BeautifulSoup 
# uses the HTML parser (XML parsing also available)
results = bs4.BeautifulSoup(response.text, 'html.parser')

# Select the quotes
# Returns a list of Tag objects that are located in a div named "quotesList"
# and are links (<a> tags)
# Since we are looking for the quotes from a given author's result page,
# they are found as a link inside of an element on the page with an id
# of quotesList. The select() method will return a list of all the HTML
# tags that fit both criteria
# Tag objects are like dictionaries in the way you can retireve values
# from the tag's elements, as shown below
# There are a number of ways to specify what elements of a document to
# retrieve, consult the BeautifulSoup documentation for more details
quotes = results.select('#quotesList a')

print('Found the following quotes for {}: \n'.format(author))

for quote in quotes:
    # Quotes are in tags with <title> == 'view quote'
    # get() method will return value of <title> tag
    if quote.get('title') == 'view quote':
        print(quote.getText())  # Method to print inner text of tag
        print('-')*75
