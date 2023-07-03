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

# List all mobile phones 
import re

start_word = "Add to Compare"
end_word = "("

escaped_start_word = re.escape(start_word)
escaped_end_word = re.escape(end_word)

pattern = f"{escaped_start_word}(.*?){escaped_end_word}"
matches = re.finditer(pattern, text)
name = []

for match in matches:
    project = match.group(1).strip()
    name.append(project)

print(name)


