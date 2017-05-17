"""
	practice on load and write to .csv
"""


import csv


class file_manager():

	def __init__(self, reader=None, writer=None):
		self.reader = []
		self.writer = []
	
	def load_file(self):
		with open("test.csv") as csvfile:
			reader = csv.reader(csvfile)

	
	
def main():
	test_manager = file_manager()
	spamfile = test_manager.load_file()
	print(spamfile)
	for row in spamfile:
		print("{} ".format(row))


