import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = "https://www.ymgrad.com/search/United%20States/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find elements using CSS selectors and extract information
    # Replace these lines with the specific tags and attributes of the website you're scraping
    titles = soup.find_all("h2", class_="title")
    links = soup.find_all("a", class_="link")
    
    # Process and print the extracted data
    for title, link in zip(titles, links):
        title_text = title.get_text()
        link_url = link["href"]
        print(f"Title: {title_text}")
        print(f"Link: {link_url}")
else:
    print("Failed to retrieve the webpage")

