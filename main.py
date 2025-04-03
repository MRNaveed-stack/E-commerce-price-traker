import pandas as pd
import requests,time
from bs4 import BeautifulSoup

# This is the url of mock website which we will fetch
url = "http://books.toscrape.com/"
from time import sleep
#Add retries for failed requests
try:
  response = requests.get(url,headers={"User-Agent": "Mozilla/5.0"})
  response.raise_for_status() 
# Going to parse its content using python library
  soup = BeautifulSoup(response.text,"html.parser")
  books = []  #we have to initialize a list to store data 
# iterate through every single info and # using CSS selector also

  for book in soup.select("article.product_pod") :
    title = book.h3.a["title"]
    price = soup.select_one("P.price_color").text.replace("Â£", "")
    rating = book.select_one("p.star-rating")["class"][1]
    books.append({"Title": title, "Price (£)": price, "Rating": rating})
    time.sleep(1) 
except requests.exceptions.RequestException as e:
  print(f"Request failed: {e}")
  sleep(5)
#using pandas to make code readable and save it in csv
df = pd.DataFrame(books)
df["Price (£)"] = df["Price (£)"].astype(float)

# Calculate the average price from the 'Price (£)' column
print("\n=== Analysis Results ===")
average_price = df['Price (£)'].mean()
# Find the most common rating from the 'Rating' column
most_common_rating = df['Rating'].mode()[0]
# Print the results in a user-friendly format
print(f"The average price of the items is: £{average_price:.2f}")
print(f"The most common rating among the items is: {most_common_rating} stars")
df.to_csv("books_data.csv",index = False)
print("Data saved to books_data.csv!")



   


