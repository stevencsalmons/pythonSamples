import requests
from bs4 import BeautifulSoup
import pandas as pd

# html request to URL
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.96199000000007&lon=-83.00274999999993#.XjXF5GhKiUk')

# create beautiful soup obj that parses HTML data
soup = BeautifulSoup(page.content,'html.parser')

# find base search unit, html ID containing data
week = soup.find(id='seven-day-forecast-body')

# find specific object containers
day = week.find_all(class_='tombstone-container')

# create obj for each object property, loop through them all in container
period_names =  [day.find(class_='period-name').get_text() for day in day]
period_desc =   [day.find(class_='short-desc').get_text() for day in day]
period_temp =   [day.find(class_='temp').get_text() for day in day]

# pandas obj for formatting
weather_obj = pd.DataFrame({
    'period'            : period_names,
    'short_descriptions': period_desc,
    'temperatures'      : period_temp
})

# free to do whatever from here!
# a solid hello-world for python
print(weather_obj)