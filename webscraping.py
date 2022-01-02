import requests
import pandas as pd
#import numpy as np
import bs4 as bs

header ={"Accept-Language":"en-US,en;q=0.5"}

url = 'https://deliveroo.co.uk/'
results = requests.get(url)


soup = bs.BeautifulSoup(results.content, "html.parser")

# the data we need to extract
list_of_menu = []

menu = soup.find_all('span',class_ = 'HomepageFeaturedCollectionTile-dca78627621916a1')
#print(menu)
#for types in menu:
 #   list_of_menu.append(types.text)
[list_of_menu.append(types.text) for types in menu]
#print(list_of_menu)

df = pd.DataFrame(list_of_menu)
df.columns = ['Menu_items']
print(df)
#print(df.head())