"""""
Website used for reference: http://books.toscrape.com/
Some of the classes/tags are based on the website html I'm using right now. 
Not all websites would be using the same classes/tags.
So first step would be to analyse the website html and make the changes accordingly.
Either you can inspect the html page, or parse the page and then print and prettify it.
"""""

from bs4 import BeautifulSoup
import requests
import csv

#function to web scrape the details
def scrape_details(url):
    response = requests.get(url) #send a request to the url, not all websites allowe webscraping
    response.raise_for_status()  #exception for HTTP errors
    soup = BeautifulSoup(response.text, 'html.parser') #parsing the HTML content using BeautifulSoup
    products = soup.find_all('article', class_='product_pod')
    product_details = [] #creating a list

    for product in products:
        title = product.h3.a['title'] 
        price = product.select_one('.price_color').get_text(strip=True)
        rating = product.p['class'][1] 
        product_details.append([title, price, rating]) #appending to the list

    return product_details

# Write the data to a CSV file
def save_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file: #creating a new file, change modes based on necessity
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price', 'Rating in stars'])  #header of the csv file
        writer.writerows(data)
        
#Welcoming Statement
print(f"Hello! Welcome to Product Detail Scraper.\nInsert the url of an e-commerce website of your choice.\nGet all the details of the products organised to a csv file for easier readability!\nWe will be using the concept of webscraping here\nPLEASE NOTE: Not all websites allow webscraping!\n")
url = input("Enter the url of the website: ")
print(f"\nCollecting data.....\n")

#calling of functions defined above
try:
    details = scrape_details(url) #scraping details
    if not details:
        print("No products found. Website Structure might have changed.") #explained above
    else:
        file = 'details.csv'
        save_csv(details, file)
        print("Details have been saved to csv file.")
        
except requests.RequestException as e:
    print(f"An error occurred while fetching the URL: {e}")
