# VoiceCode / Sublime Text (2|3) Integration Package

This is a Sublime Text plugin that lets [VoiceCode](http://voicecode.io) control [Sublime Text](https://www.sublimetext.com)

This integration is needed because many VoiceCode voice commands are more sophisticated than simply pressing keys or clicking the mouse. For example, a command that *selects the next curly brace*, or a command that *extends the current selection(s) forward until the next comma*, etc.

## Setup

First make sure the commandline utility for Sublime Text is installed and working https://www.sublimetext.com/docs/3/osx_command_line.html

## Adding your own commands

If you want to add new commands that are not already included in this package, just add something similar to the following in a user extension file for Sublime Text.

```python
import sublime, sublime_plugin

class SelectPreviousWordCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pos = self.view.sel()[0].begin()
		all_previous = [r for r in self.view.find_all('\w+') if r.begin() < pos]
		if all_previous:
			region = all_previous[-1]  # return nearest
			if region:
				self.view.sel().clear()
				self.view.sel().add(region)
```

Then, in your VoiceCode user commands, you can call this Sublime Text command as follows:

```coffeescript
@exec "subl --command 'select_previous_word'"
```


### Triggering existing Sublime Text commands

In VoiceCode simply do something like:

```coffeescript
@exec "subl --command 'goto_line {\"line\": 10}'"
```
