# Copyright (C) 2018  LuciaSoftware and it's contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.

class Logger(object):
	def __init__(self):
		self.entries=[]
	
	def reset(self):
		self.entries=[]
	
	
	def add_entry(self, the_entry):
		self.entries.append(the_entry)
	
	def write(self, filename, should_reset=False):
		with open(filename, "a") as f:
			if len(self.entries) > 0:
				for i in self.entries:
					f.write(i+"\n")
			if should_reset:
				self.reset()