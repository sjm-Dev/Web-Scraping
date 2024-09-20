
Web Scraping Project - Books to Scrape

Intro:
This project performs web scraping from the Books to Scrape website using the Selenium and BeautifulSoup libraries to extract information about books, including title, price, and availability. The extracted data can be used for market analysis, trend tracking, and understanding consumer behavior in the book industry.

Technologies Used:
Python 3.x
Selenium: For interacting with the browser and loading pages.
BeautifulSoup: For parsing HTML content and extracting data.
Pandas: For structuring and storing data in CSV format.
Chrome WebDriver: For controlling the Google Chrome browser.

Installation:
Make sure you have Python 3.x installed.
Install the necessary dependencies using pip.

Dependencies:
pip install selenium
pip install beautifulsoup4
pip install pandas
pip install webdriver-manager

Methodology:
The scraping process was designed to handle pagination, ensuring that all books listed on the site are extracted. Data cleaning techniques were applied to remove unwanted characters and whitespace from the titles, prices, and stock availability, resulting in a clean and structured dataset suitable for analysis.

Example Output:
When running the script, a CSV file will be generated with the following example data:

Title					Price	Stock
A Light in the Attic			£51.77	In stock
Tipping the Velvet			£53.74	In stock
Soumission				£50.10	In stock
Sharp Objects				£47.82	In stock
Sapiens: A Brief History of Humankind	£54.23	In stock

Results:

The data extracted from this project can provide insights into pricing strategies, inventory management, and customer demand trends in the book market. Such analyses can assist businesses in making data-driven decisions.

