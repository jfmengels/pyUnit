

class Asserter:
	"""Object which will assert statements, and store their result.
"""

	def __init__(self):
		"""Initializes the asserter.
"""
		self.reset()


	def reset(self):
		"""Resets the internal data of the asserter so that new tests can be realized.
"""
		# End result: True if all tests succeeded, False otherwise.
		self.successFinal = True
		# Dictionary of the success result for each function.
		self.successFunc = {} # key: function name, value: success boolean
		# Dictionary of the fail messages for each function
		self.messageFunc = {} # key: function name, value: list of fail messages
		# Name of the function that is currently tested.
		self.currentFunction = ''


	def enter(self, func):
		"""Enter a new function. Should be called every time a new test
function is entered, otherwise failed functions will not be correctly shown.
func: Name of the function to enter and to prepare for.
"""
		self.currentFunction = func
		self.successFunc[func] = True
		self.messageFunc[func] = []


	def _notifyFail(self, msg=''):
		"""Notify the asserter of a failed statement.
"""
		# Fail the whole test and the current function.
		self.successFinal = False
		self.successFunc[self.currentFunction] = False
		# If there is a message, append it.
		if msg != '':
			self.messageFunc[self.currentFunction].append(msg)


	def catchException(self, exception, msg=''):
		"""Catches an exception.
exception: Catched exception.
msg: Optional message to display. Will precede the exception's message.
"""
		if msg != '':
			msg = msg + '\n' + repr(exception)
		else:
			msg = repr(exception)
		self._notifyFail(msg)
		

	def assertTrue(self, value, msg=''):
		"""Asserts that the given expression is evaluated as True.
value: Value to evaluate.
msg: Optional message to display if the assertion fails.
"""
		if not value:
			self._notifyFail(msg)


	def assertFalse(self, value, msg=''):
		"""Asserts that the given expression is evaluated as False.
value: Value to evaluate.
msg: Optional message to display if the assertion fails.
"""
		if value:
			self._notifyFail(msg)


	def fail(self, msg=''):
		"""Fails the test without condition.
msg: Optional message to display.
"""
		self._notifyFail(msg)


	def assertEquals(self, a, b, msg=''):
		"""Asserts that a equals b.
a, b: Values to evaluate.
msg: Optional message to display if the assertion fails.
"""
		if a != b:
			self._notifyFail(msg)


	def assertNotNone(self, value, msg=''):
		"""Asserts that value is not None.
value: Value to evaluate.
msg: Optional message to display if the assertion fails.
"""
		if value == None:
			self._notifyFail(msg)


	def assertNone(self, value, msg=''):
		"""Asserts that value is None.
value: Value to evaluate.
msg: Optional message to display if the assertion fails.
"""
		if value != None:
			self._notifyFail(msg)


	def __repr__(self):
		"""Represents the result of the test.
"""
		s = ''
		if self.successFinal:
			s = '[ OK ] Test'
		else:
			# Tests failed, display the results of each function.
			s = '[FAIL] Test'
			for func in self.successFunc: # for every test function
				s += '\n'
				if not self.successFunc[func]:
					# If test function failed, print error
					s += '[FAIL] ' + func
					# and error messages.
					for msg in self.messageFunc[func]:
						s += '\n\t' + msg
				else:
					s += '[ OK ] ' + func
		return s
