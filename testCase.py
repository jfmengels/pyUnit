from asserter import Asserter

class TestCase:
	"""Model for a unit test.
"""

	def run(self):
		"""Run the tests. Executes every function whose name starts
with 'test'.
"""
		if self.asserter == None:
			self.asserter = Asserter()
		self.asserter.reset()
		functions = [func for func in dir(self) \
			if func.startswith('test')]
		self.setUpBeforeClass() # One-time global set up.

		# Execute every function.
		for func in functions:
			# Notify the asserter a new function is beginning.
			self.asserter.enter(func)
			self.setUp()
			try:
				getattr(self, func)() # Launch function
			except Exception as exc: # Catch uncaught exceptions
				self.asserter.catchException(exc)
			self.tearDown()
		self.tearDownAfterClass() # Final tear down
		print('Test result:', self.asserter) # Print result
		

	def setUpBeforeClass(self):
		"""One-time set up before all the test functions are launched.
"""
		pass

	def tearDownAfterClass(self):
		"""One-time tear down, called when all the tests have been realized.
"""
		pass

	def setUp(self):
		"""Set up ressources. Is called before every function launch.
"""
		pass

	def tearDown(self):
		"""Tear down ressources. Is called after every function launch.
"""
		pass

