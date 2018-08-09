from base import Collector
from config import config, target

def run():
	collector = Collector(token_key=config['token_key'], 
						  token_secret=config['token_secret'],
						  consumer_key=config['consumer_key'],
						  consumer_secret=config['consumer_secret'])

	collector.get_urls(target='TirtoID', min_rt=5, min_fav=5, count=50)
	collector.parse_text()

if __name__ == '__main__':
	run()