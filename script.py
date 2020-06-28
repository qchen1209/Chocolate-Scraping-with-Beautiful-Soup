import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html")

soup = BeautifulSoup(webpage.content, "html.parser")

soup.find_all(attrs={"td": "Rating"})
Rating = soup.select(".Rating")

ratings = []
for td in Rating[1:]:
  ratings.append(float(td.get_text()))

plt.hist(ratings)
plt.show()

Company = soup.select(".Company")

company_tags = []
for td in Company[1:]:
  company_tags.append(td.get_text())

d = {"Company": company_tags, "Ratings": ratings}
df = pd.DataFrame.from_dict(d)

mean_vals = df.groupby("Company").Ratings.mean()
ten_best = mean_vals.nlargest(10)
print(ten_best)

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")

for td in cocoa_percent_tags[1:]:
  percent = td.get_text().strip('%')
  cocoa_percents.append(percent)

df['CocoaPercentage'] = cocoa_percents

plt.scatter(df.CocoaPercentage, df.Ratings)

plt.show()
