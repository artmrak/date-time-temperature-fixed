import sqlite3
from bs4 import BeautifulSoup
import requests, lxml

html = requests.get('https://www.timeanddate.com/weather/ukraine/zaporizhia')
soup = BeautifulSoup(html.text, 'lxml')


temp = soup.select_one('#qlook .h2').text
Time_date = soup.select_one('#wtct').text
print('Zaporizhia forecast:')
print(Time_date,',', temp)


connection = sqlite3.connect("Database.sl3", 5)
cur = connection.cursor()


#cur.execute("CREATE TABLE first_table (name TEXT);")
#cur.execute("INSERT INTO first_table (name) VALUES ('temp');")
#cur.execute("INSERT INTO first_table (name) VALUES ('Time_date');")


for i in cur.execute("SELECT rowid, name FROM first_table WHERE rowid=1;"):
    print(i)


connection.commit()
connection.close()
