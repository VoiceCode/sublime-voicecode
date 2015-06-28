import sublime, sublime_plugin

class SelectNextNumberCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pos = self.view.sel()[0].end()
		region = self.view.find('(?:\d*\.)?\d+', pos)

		if region.a == -1:
			region.a = pos
			region.b = pos

		self.view.sel().clear()
		self.view.sel().add(region)

class SelectNextWordCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pos = self.view.sel()[0].end()
		region = self.view.find('\w+', pos)

		if region.a == -1:
			region.a = pos
			region.b = pos

		self.view.sel().clear()
		self.view.sel().add(region)

class SelectPreviousWordCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pos = self.view.sel()[0].begin()
		all_previous = [r for r in self.view.find_all('\w+') if r.begin() < pos]
		if all_previous:
			region = all_previous[-1]  # return nearest
			if region:
				self.view.sel().clear()
				self.view.sel().add(region)


	
