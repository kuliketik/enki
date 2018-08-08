class Collector:
	def __init__(self, **kwargs):
		
		self.key = 
		self.token_secret = 
		self.key_secret = 
		self.twit = do_auth(token=kwargs['token'], 
							key=kwargs['key'], 
							key_secret=kwargs['token_secret'], 
							token_secret=kwargs['key_secret']
)

	def get_tweets(self, target):
		for tweet in twit.get_tweet(likes=10, retweet=10, comments=10):
			do_save(tweet)


class TaskAdder:
	def __init__(self) -> None:
		self.tasks = []

	def add_task(self, **kwargs):
		"""
		argumen:
			name: str
			pattern: str
		"""
		self.tasks.append(dict(url=kwargs['url'], target=kwargs['target']))

	def __getitem__(self, index):
		return self.tasks[index]


class ExecTask:
	def ___init__(self, jobs):
		self.jobs = []

	def add_job(self, jobs):
		self.jobs = jobs 

	def do_parse(self):
		print('jobs: ', self.jobs)



if __name__ == '__main__':
	tasker = TaskAdder()
	tasker.add_task(url='http://detik.com', target='div.target.bla')
	tasker.add_task(url='http://detik.com', target='div.target.bla')

	job_doer = ExecTask()
	job_doer.add_job(tasker.tasks)
	#job_doer.do_parse()

	for task in tasker:
		print(task['url'], '-->', task['target'])

	#print(tasker.tasks)