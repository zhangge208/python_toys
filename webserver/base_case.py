class base_case(object):
	'''Parent for case handlers.'''
	def handle_file(self, handler, full_path):
		try:
			with open(full_path, 'rb') as reader:
				content = reader.read()
			handler.send_content(content)
		except IOError as msg:
			msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)

    def indec_path(self, handler):
    	return os.path.join(header.full_path, 'index.html')

    def test(self, handler):
    	assert False, 'Not implemented.'

    def act(self, handler):
    	assert False, 'Not implemented'