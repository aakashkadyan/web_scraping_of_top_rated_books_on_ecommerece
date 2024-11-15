# 1. Web scraping of Top Selling Books from Amazon

Amazon is one of the largest online marketplaces, and it frequently updates its list of top-selling books.
This project uses web scraping to collect up-to-date information on these bestsellers, allowing for analysis of current book ranking, pricing, book name and ratings.


**Note**: This project is for educational purposes. Web scraping Amazon or any other website without permission may violate their Terms of Service.
Please refer to Amazon’s policies and consider using their official APIs if available.

**Features:**

Scrapes details of Amazon’s top-selling books, including:

1. Book Name
2. Ranking
3. Price (Hardcover, Paperback, Kindle, etc.)
4. Ratings
5. Saves the extracted data in a CSV file format for easy access and analysis.
6. Can be scheduled to run periodically to collect updated data.

**Technologies Used:**

1. *Python*: Programming language used to implement the scraper.
2. *BeautifulSoup*: For parsing HTML and extracting data from web pages.
3. *Requests*: For sending HTTP requests to Amazon’s website.
4. *Pandas*: For structuring and exporting data to CSV.

**Installation / Run script:**
1. Change path according to your directory.
2. Run Command "python top_selling_books.py"


# 2. Web Scraping of Weather forecasting from Weathercrave

This project performs web scraping on WeatherCrave (www.weathercrave.com) to collect up-to-date weather forecast data for specified locations.
The collected data includes temperature and other relevant weather metrics.

**Note**: This project is for educational purposes. Web scraping of any website without permission may violate their Terms of Service.
Please refer to Weathercrave’s policies and consider using their official APIs if available.

**Features:**

Scrapes detailed weather information for specified locations, including:
1. Temperature of your City (Morning, Noon & Evening)
2. Saves the extracted data in a structured CSV for easy access and analysis.
3. Option to scrape data for multiple days or a custom forecast range.

**Technologies Used:**

1. *Python*: Programming language used to implement the scraper.
2. *BeautifulSoup*: For parsing HTML and extracting data from web pages.
3. *Requests*: For sending HTTP requests to Amazon’s website.

**Installation / Run script:**
1. Change path according to your directory.
2. You can modified this script as per your city or other weather information you want to check.
3. Run Command "python weather_forecast.py"
