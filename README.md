# Book Scraper

## Overview
This project is a simple web scraper that extracts book information from the website [Books to Scrape](http://books.toscrape.com/). The scraper collects data such as the title, price, and rating of each book and saves it to a CSV file for further analysis.

## Features
- Fetches book data from the specified URL.
- Parses the HTML content using BeautifulSoup.
- Handles request failures with retries.
- Calculates the average price of the books.
- Identifies the most common rating among the books.
- Saves the collected data to a CSV file.

## Requirements
To run this project, you need to have Python installed along with the following libraries:
- `pandas`
- `requests`
- `beautifulsoup4`

You can install the required libraries using pip:

```bash
pip install pandas requests beautifulsoup4