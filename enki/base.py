import tweepy
import requests
from bs4 import BeautifulSoup as bs 




class Collector:
	def __init__(self, **kwargs):

		auth = tweepy.OAuthHandler(kwargs['consumer_key'], kwargs['consumer_secret'])
		auth.set_access_token(kwargs['token_key'], kwargs['token_secret'])
		
		try:
			self.api = tweepy.API(auth)
		except Exception as err:
			raise ('otentifikasi gagal...')

		
		self.urls = []
		self.target = None


	def get_urls(self, **kwargs):
		"""
		target: str
		count: str
		min_rt: int
		min_fav: int
		"""
		
		self.target = kwargs['target']

		tweets = self.api.user_timeline(screen_name = kwargs['target'], count = kwargs['count'], include_rts = False)

		min_rt = kwargs['min_rt']
		min_fav = kwargs['min_fav']

		for tweet in tweets:
			if tweet.favorite_count >= min_fav or tweet.retweet_count >= min_rt:
				self.urls.append(tweet.entities['urls'][0]['url'])


	def parse_text(self):
		if self.target is not None:
			if self.target == 'TirtoID':
				target_tag = 'content-text-editor'

			elif self.target == 'kompascom':
				target_tag = 'bla' # DUMMY

		for url in self.urls:
			
			print('scraping {url}')			
			html = requests.get(url).text
			soup = bs(html, 'html.parser')
			isi_konten = soup.find_all('div', target_tag)
			
			for konten in isi_konten:
				print(konten.text)


	def __getitem__(self, index):
		return self.urls[index]

