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
# You can do a lot of things with a reponse like get the JSON of the page,
# get the HTML of a page, etc...
response = requests.get('http://brainyquote.com/search_results.html?q={}'
                        .format(author))

# Check to ensure page was downloaded correctly
# Will raise an exception if error occurred (non 200 response code)
# Good practice to call right after making a request
response.raise_for_status()

# Create a BeautifulSoup Object
# Allows us to parse the HTML retrieved from brainyquote.com
# You can specify the parser to use, other option include an
# XML parser
results = bs4.BeautifulSoup(response.text, 'html.parser')

# Select the quotes
# Returns a list of Tag objects that are located in a div named "quotesList"
# and are links (<a> tags)
# Tag objects are like dictionaries in the way you can retireve values
# from the tag's elements, as shown below
# There are a number of ways to specify what elements of a document to
# retrieve, consult the BeautifulSoup documentation for more details
quotes = results.select('#quotesList a')

print('Found the following quotes for {}: \n'.format(author))

for quote in quotes:
    # Quotes are in tags with <title> == 'view quote'
    # select() methods will return value of <title> tag
    if quote.get('title') == 'view quote':
        print(quote.getText())  # Method to print inner text of tag
        print('-')*75
