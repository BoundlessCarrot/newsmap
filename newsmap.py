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
		lines = [n.get_text() for n in soup.find_all(class_='story-title')]
		links = [x.get('href') for x in soup.find_all('a', href=True) if x.p['class'] == 'story-title']

		for i in range(10):
			print(lines[i].strip())
			print(links[i])
			print()
#			
	
	def parse_headline():
		'''
		Iterates over the dict from retrieve_headlines and gets the location per headline. Should be saved as a dict as {headline: location}.
		Needs location/city names/etc from a library (unknown atm).  
		'''
		pass
	

if __name__ == '__main__':
	re = Reuter
	re.retrieve_headlines()