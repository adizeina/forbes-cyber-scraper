from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.forbes.com/search/?sort=recent&q=cyber&sh=2b4c4737279f').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('scraped_data.csv', 'w') #w for write
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary','date'])


for article in soup.find_all('article'): #will return a list 

	headline = article.h2.a.text
	summary = article.find('div', class_='stream-item__description').text
	date = article.find('div', class_ ='stream-item__date').text

	# next goal: loop through each page and access views = article.find('span', class_ = 'pageviews').text

	print(headline)
	print(summary)
	print(date)
	csv_writer.writerow([headline, summary,date])

csv_file.close()



