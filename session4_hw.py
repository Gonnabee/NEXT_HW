from bs4 import BeautifulSoup
import requests as req
import pandas as pd

target_url = "http://opentutorial.org/course/1"
res = req.get(target_url)
soup = BeautifulSoup(res.text, "html.parser")

li_comment = soup.find_all(class_="comment_content")
li_comment_cleaned = [e.text.strip() for e in li_comment]
li_name = soup.select('div.name.time > strong')
li_name_cleaned = [e.text for e in li_name]
li_time = soup.select('div.name.time > a')
li_time_cleaned = [e.text for e in li_time]

container = {
    'name': li_name_cleaned,
    'time': li_time_cleaned,
    'comments': li_comment_cleaned,
}

df_table = pd.DataFrame(container)
print(df_table)
