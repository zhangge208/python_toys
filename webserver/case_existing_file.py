class case_existing_file(base_case):
	'''File exists.'''

	def test(self, handler):
		return os.path.isfile(handler.full_path)

 	def act(self, handler):
 		self.handle_file(handler, handler.full_path)