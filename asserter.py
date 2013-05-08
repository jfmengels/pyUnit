

class Asserter:
	def __init__(self):
		self.reset()

	def reset(self):
		self.val = True
		self.resFunc = {}
		self.resMsg = {}
		self.currentFunction = None

	def enter(self, func):
		self.currentFunction = func
		self.resFunc[func] = True
		self.resMsg[func] = []

	def notifyFail(self, msg=''):
		self.resFunc[self.currentFunction] = False
		self.val = False
		if msg != '':
			self.resMsg[self.currentFunction].append(msg)

	def assertTrue(self, b, msg=''):
		if not b:
			self.notifyFail(msg)

	def assertFalse(self, b, msg=''):
		if b:
			self.notifyFail(msg)

	def fail(self, msg=''):
		self.notifyFail(msg)

	def assertEquals(self, a, b, msg=''):
		if a != b:
			self.notifyFail(msg)

	def assertNotNone(self, val, msg=''):
		if val == None:
			self.notifyFail(msg)

	def assertNone(self, val, msg=''):
		if val != None:
			self.notifyFail(msg)

	def __repr__(self):
		s = ''
		if self.val:
			s = '[ OK ] Test'
		else:
			s = '[FAIL] Test'
			for func in self.resFunc:
				s += '\n'
				if not self.resFunc[func]:
					s += '[FAIL] ' + func
					for msg in self.resMsg[func]:
						s += '\n\t' + msg
				else:
					s += '[ OK ] ' + func
		return s
