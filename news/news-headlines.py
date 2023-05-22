from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

website = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
path = "/Users/Tiger/Desktop/python/automation/chromedriver_mac_arm64/chromedriver"

# headless
options = Options()
options.add_argument("--headless=new")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(
    by="xpath", value="//td[@class='titleColumn']//a")

titles = []
links = []

for container in containers:
    title = container.text
    link = container.get_attribute("href")

    titles.append(title)
    links.append(link)


print(len(titles))
print(len(links))


my_dict = {"title": titles, "link": links}
df_headlines = pd.DataFrame(my_dict)
file_name = f"excel/headline-{month_day_year}.csv"
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()
