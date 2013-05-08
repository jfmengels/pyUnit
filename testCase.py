from asserter import Asserter

class TestCase:
	def __init__(self):
		pass

	def run(self):
		self.asserter = Asserter()
		self.setUpBeforeClass()
		functions = [func for func in dir(self) \
			if func.startswith('test')]
		for func in functions:
			self.asserter.enter(func)
			self.setUp()
			getattr(self, func)()
			self.tearDown()
		self.tearDownAfterClass()
		print('Test result:', self.asserter)
		

	def setUpBeforeClass(self):
		pass

	def tearDownAfterClass(self):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

