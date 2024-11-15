import requests,bs4
import pandas as pd

download_data = requests.get("https://www.amazon.in/gp/bestsellers/books/")
download_data.raise_for_status()
scrap_raw_text = bs4.BeautifulSoup(download_data.text)
rank_data = scrap_raw_text.select('.zg-bdg-text')
book_name = scrap_raw_text.select('._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y')
book_ratings = scrap_raw_text.select('.a-icon-alt')
book_price = scrap_raw_text.select('.p13n-sc-price')

scraped_data_dict = {
    
    'rank':[],
    'book_name':[],
    'ratings':[],
    'price':[]  
    
}

for ranks in range(len(rank_data)):
    scraped_data_dict["rank"].append(rank_data[ranks].get_text())

for names in range(len(book_name)):

    scraped_data_dict["book_name"].append(book_name[names].get_text())

for ratings in range(len(book_ratings)):
    scraped_data_dict["ratings"].append(book_ratings[ratings].get_text())

for price in range(len(book_price)):
    scraped_data_dict["price"].append(book_price[price].get_text())



df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in scraped_data_dict.items() ]))
df.to_csv("top_50_best_selling_books9.csv")       