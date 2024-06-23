#################################
#SINGLE RESPONSIBILITY PRINCIPLE#
#################################
import csv
import os
import shutil

class FileStatUI:

	def __init__(self) -> None:
		self.stat_mngr = FileStatManager()
		self.cleaner = FolderCleaner

	def choose_file(self):
		while True:
			file_path = input("Enter a path")
			if os.path.isfile(file_path):
				break
			else:
				print("Invalid path")

		res = self.stat_mngr.choose_file(file_path)
		if res:
			print(res)
		else:
			print("the stats were updated")

	def clean_stats(self):
		while True:
			answ = input("R u sure? (y/n)")
			if answ == 'y':
				self.stat_mngr.clean_stats()
				print("stats were cleaned")
				break
			elif answ == 'n':
				print("stats were preserved")
				break

	def show_stats(self):
		stats = self.stat_mngr.get_stats()
		print(stats)

class FileStatManager:

	def __init__(self) -> None:
		self.txt_stat = FileStats("txt")
		self.txt_stat = FileStats("csv")

	def read_txt_stats(self, file_path):
		try:
			with open(file_path, 'r') as f:
				self.txt_stat.increase(lines=len(f.readlines()))
			return False
		except Exception as e:
			return str(e)

	def read_csv_stats(self, file_path):
		try:
			with open(file_path, 'r') as f:
				reader = csv.reader(f)
				lines = [len(l) for l in reader]
				self.csv_stat.increase(lines=len(lines), columns=min(lines))
			return False
		except Exception as e:
			return str(e)

	def choose_file(self, file_path):
		if file_path.endswith('.txt'):
			return self.read_txt_stats(file_path)
		elif file_path.endswith('.csv'):
			return self.read_csv_stats(file_path)

	def clean_stats(self):
		self.txt_stat = FileStats("txt")
		self.csv_stat = FileStats("csv")

	def get_stats(self):
		res = ""
		res = f"{res}The TXT stats:\n"
		res = f"{res}{self.txt_stat}\n"
		res = f"{res}The CSV stats:\n"
		res = f"{res}{self.csv_stat}\n"
		return res

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


class FolderCleaner:

	@staticmethod
	def clean_folder(folder):
		try:
			shutil.rmtree(folder)
			return False
		except Exception as e:
			return str(e)


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

ui = FileStatUI()
ui.choose_file()
ui.choose_file()
ui.show_stats()