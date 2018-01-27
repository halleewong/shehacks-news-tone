from bs4 import BeautifulSoup
import requests
class Scraper(object):
	
	def __init__(self):
		pass

	def scrape_mirror(self,url):
		articles_scraped = []
		# articles_dictionary = {}
		# article_number = []
		
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		# print soup

		required_content = []
		for p in soup.find_all("p", {'class':'vjs-modal-dialog-description'}): 
		    p.decompose()

		for el in soup.find_all('p'):
			required_content.append(el.get_text())
		
		articles = ''.join(required_content)
		
		
		# return articles_scraped
		# articles_dict = dict(zip(article_number, articles_scraped))
		# print articles_dictionary
		return articles
