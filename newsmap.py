from bs4 import BeautifulSoup as bs
import requests as req

class Reuter:
	def __init__(self):
		pass
		
	def retrieve_headlines():
		'''
		Returns a dict of the URLs associated with the top 10 trending headlines retrieved from self.base_url
		'''
		r = req.get('https://www.reuters.com')
		assert r.status_code == req.codes.ok, 'Got error code {}'.format(r.status_code)
		
		text = r.text
		soup = bs(text, features="lxml")
		dirty_lines = soup.find_all(class_='story-title')
		dirty_links = soup.find_all('a href')
		clean_lines = [n.get_text() for n in dirty_lines]
#		clean_links = []
#		clean_links = [x.get_text() for x in dirty_links if dirty_lines in dirty_links]
#		for x in dirty_links:
#			print(x)
#			if x in dirty_lines:
#				clean_links.append(x.strip())
			
		for i in range(10):
			print(clean_lines[i].strip())
#			print(clean_links[i])
			print()
			
	
	def parse_headline():
		'''
		Iterates over the dict from retrieve_headlines and gets the location per headline. Should be saved as a dict as {headline: location}.
		Needs location/city names/etc from a library (unknown atm).  
		'''
		pass
	

if __name__ == '__main__':
	re = Reuter
	re.retrieve_headlines()