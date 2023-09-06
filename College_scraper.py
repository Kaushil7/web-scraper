import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = "https://www.ymgrad.com/search/United%20States"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the outer-most div using its class name
    outer_div = soup.find("h3", class_="UniversityCardNew__university_name___")
    print(outer_div)
    

    
