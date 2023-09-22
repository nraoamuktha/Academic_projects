import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

# Start a Selenium server (the remote controller)
# and scrape some data from businessofapps.com
driver = webdriver.Firefox()
driver.get("https://www.businessofapps.com/data/app-data/")

# Scrape the list of apps
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
apps_table = soup.find("table")
apps_df = pd.read_html(str(apps_table))[0]

# Choose only social and social video categories
apps_df = apps_df[apps_df['Category'].isin(['Social', 'Social, Video']) & (apps_df['Revenue ($M)'] > 10)]
apps_list = apps_df['App'].tolist()

# Scrape revenue and users time series from the website
Revenue = []
launch_date = []

for app in apps_list:
    driver.get("https://www.businessofapps.com/data/app-data/")
    web_elem = driver.find_element_by_link_text(app)
    time.sleep(3 + 0.1 * random.random())
    web_elem.send_keys(Keys.ENTER)
    time.sleep(3 + 0.1 * random.random())
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    tables = soup.find_all("table")
    launch_date.append(tables[0].find_all("tr")[0].find_all("td")[1].text.strip())

    revenue_info = pd.read_html(str(tables[1]))[0]
    revenue_info.columns = ['Date', app]
    Revenue.append(revenue_info)

# Data processing
launch_date[4] = "1 September 2017"
launch_date = pd.to_datetime(launch_date, format="%d %B %Y")

# Join the time series
Revenue_all = Revenue[0]
for i in range(1, len(Revenue)):
    Revenue_all = Revenue_all.merge(Revenue[i], on='Date', how='outer')

# Separate revenue columns, remove "billion", "million" and "$"
for app in apps_list:
    Revenue_all[app] = pd.to_numeric(Revenue_all[app].str.replace('[$,]', '', regex=True))

# Convert million to billion
for app in apps_list:
    if 'mm' in Revenue_all.columns:
        Revenue_all[app] = Revenue_all[app] / 100

# Generating a plot for the time series
import matplotlib.pyplot as plt
import seaborn as sns

Revenue_all_melted = Revenue_all.melt(id_vars='Date', var_name='App', value_name='Revenue (billion)')
plt.figure(figsize=(12, 6))
sns.lineplot(data=Revenue_all_melted, x='Date', y='Revenue (billion)', hue='App')
plt.title("Revenue of major social networking websites from 2010 to 2020")
plt.xlabel("Year")
plt.ylabel("Revenue (billion)")
plt.xticks([2010, 2015, 2020])
plt.legend(loc="lower right")
plt.show()

# Close the Selenium WebDriver
driver.quit()
