import requests,bs4
import datetime
import pytz
def show_temprature_of_faridabad(url):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    res = requests.get(url)
    res.raise_for_status()
    scrap_data = bs4.BeautifulSoup(res.text)

    element = scrap_data.select('.tempe')
    print("Date of ForeCast: ", current_time)
    print()
    day_shifts = ['Noon', 'Evening', 'Night']
    
    count =0
    for data in element:
        print(f"Temprature of Faridabad {day_shifts[count]}: ",data.get_text())
        count+=1


show_temprature_of_faridabad(url = "https://www.weathercrave.com/weather-forecast-india/city-3289/weather-forecast-faridabad-today")