#Scraping data from flipkart website
import requests
from bs4 import BeautifulSoup

# Add the url
url = 'https://www.flipkart.com/search?q=mobile+phone+5g'

# Make a request to the website
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

#raw format or html format of scraped text
# print(soup)
# soup

# Find and extract specific elements from the HTML in text form
text = soup.get_text()
# print(text)

# Finding specific device
start_word = "Add to Compare"
end_word = "("
start_index = text.find(start_word)
end_index = text.find(end_word, start_index + len(start_word))
name = ''
if start_index != -1 and end_index != -1:
    name = text[start_index + len(start_word):end_index].strip()

print(name)


