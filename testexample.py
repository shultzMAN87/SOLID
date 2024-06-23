import csv
import os
import shutil

class FileStatManager:

	def __init__(self) -> None:
		self.txt_stat = FileStats("txt")
		self.txt_stat = FileStats("csv")

	def read_txt_stats(self, file_path):
		with open(file_path, 'r') as f:
			self.txt_stat.increase(lines=len(f.readlines()))
		print("the txt stats were updates")

	def read_csv_stats(self, file_path):
		with open(file_path, 'r') as f:
			reader = csv.reader(f)
			lines = [len(l) for l in reader]
			self.csv_stat.increase(lines=len(lines), columns=max(len(line) for line in lines))
		print("the csv stats were updates")

	def choose_file(self):
		while True:
			file_path = input("Enter a path")
			if os.path.isfile(file_path):
				break
			else:
				print("Invalid path")

		if file_path.endswith('.txt'):
			self.read_txt_stats(file_path)
		elif file_path.endswith('.csv'):
			self.read_csv_stats(file_path)

	def clean_stats(self):
		while True:
			answ = input("R u sure? (y/n)")
			if answ == 'y':
				self.txt_stat = FileStats("txt")
				self.csv_stat = FileStats("csv")
				print("stats were cleaned")
				break
			elif answ == 'n':
				print("stats were preserved")
				break

	def show_stats(self):
		print("The TXT stats:")
		print(self.txt_stat)
		print("The CSV stats:")
		print(self.csv_stat)

	def clean_folder(self):
		while True:
			folder_path = input("Enter path folder")
			if os.path.isdir(folder_path):
				break
			else:
				print("Invalid folder path")

		while True:
			answ = input("R u sure? (y/n)")
			if answ == 'y':
				try:
					shutil.rmtree(folder_path)
					break
				except:
					print("Ooops, cannot clean the folder")
			elif answ == 'n':
				print("folder was preserved")
				break


class FileStats:

	def __init__(self, *exts) -> None:
		self.files_num = 0
		self.exts = exts
		if "txt" in self.exts or "csv" in self.exts:
			self.total_lines = 0
			if "csv" in self.exts:
				self.total_columns = 0

	def increase(self, **params):
		self.files_num += 1
		if "txt" in self.exts or "csv" in self.exts:
			self.total_lines += params["lines"]
			if "csv" in self.exts:
				self.total_columns += params["columns"]

	def __str__(self) -> str:
		res = f"file number = {self.files_num};"
		if "txt" in self.exts or "csv" in self.exts:
			res = f"{res}\ntotal lines = {self.total_lines};"
			if "csv" in self.exts:
				res = f"{res}\ntotal columns = {self.total_columns};"

		return res

mngr = FileStatManager()
mngr.choose_file()
mngr.choose_file()
mngr.show_stats()