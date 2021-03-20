# What is this?
## Its a webscrapper for cyber articles on Forbes:
This web scrapper will create a CSV file for the most recent cyber articles on the Forbes website, including the headline, the summary and the date.
I made this so I can write notes/important key points beside each row(article) after I finish reading them without having to copy paste the headline and the data and a mini-summary each time, all I have to do is run a file and I get all the latest cyber articles by date. 

** If you decide to do this, remember to change the name of your file or else running the .py file will not save any of your notes. I name them by the date I read them on. 


# How to Set Up:
Ensure these libraries are installed on your system:
1. [In your command prompt], install the BeautifulSoup librairy 
```
pip install beautifulsoup4
```
2. Ensure to install to install lxlm library
```
pip install lxlm
```
3. Ensure to install to install requests library
```
pip install requests
```
4. Ensure to install to install html5lib library
```
pip install html5lib
```

# Installing

1.) Download this repo via the `Clone or download` button or clone it via the git CLI:

```
git clone https://github.com/adizeina/forbes-cyber-scraper.git
```

3.) Start the webscrapping program by running `scrape.py`, either manually in a python interpreter or via python CLI:
```
python scrape.py
```

Here is the CSV file of the result of the program the day I ran it last!
```
scraped_data.csv
```

