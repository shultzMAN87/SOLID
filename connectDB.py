import pyodbc

# Настройка строки подключения
server = 'DESKTOP-MNLTOU4'
database = 'MyDB'
username = 'sa'
password = 'QaZ951623'
driver = '{ODBC Driver 18 for SQL Server}'

# Создание строки подключения
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'


# Функция для подключения к базе данных
def get_connection():
	try:
		conn = pyodbc.connect(connection_string, autocommit=True)
		return conn
	except pyodbc.Error as ex:
		print("Ошибка при подключении к базе данных:", ex)
		return None


# Функция для выполнения запроса
def execute_query(connection, query):
	try:
		cursor = connection.cursor()
		cursor.execute(query)
		# while cursor.nextset():  # NB: This always skips the first resultset
		# 	try:
		# 		results = cursor.fetchall()
		# 		break
		# 	except pyodbc.ProgrammingError:
		# 		continue
		results = cursor.fetchall()
		cursor.close()
		return results
	except pyodbc.Error as ex:
		print("Ошибка при выполнении запроса:", ex)
		return None


class EmployeeManagement:
	def __init__(self, second_name, name, surname, position):
		self.name = name
		self.second_name = second_name
		self.surname = surname
		self.position = position

	def get_employees_list(self):
		conn = get_connection()
		if conn:
			employees_list = list()

			query1 = "SELECT* from _Reference92;"
			results1 = execute_query(conn, query1)
			if results1:
				for row in results1:
					employees_list.append(f'ФИО: {row._Description}; должность: {row._Fld101}')

			conn.close()

			return employees_list
		else:
			raise Exception("Не удалось подключиться к базе данных.")

	def save_employees_list_to_file(self):
		conn = get_connection()
		if conn:
			employees_list = list()

			query1 = "SELECT* from _Reference92;"
			results1 = execute_query(conn, query1)
			if results1:
				for row in results1:
					employees_list.append(f'ФИО: {row._Description}; должность: {row._Fld101}')

			conn.close()

			filepath = r'C:\Users\Константин\Desktop\Сотрудники.txt'

			file = open(filepath, 'w')
			file.write('\n'.join(employees_list))
			file.close()

			return employees_list
		else:
			raise Exception("Не удалось подключиться к базе данных.")

	def update_salary(self, salary):
		conn = get_connection()
		if conn:
			query = (f'UPDATE _Reference92 SET _Fld103 = {salary} WHERE _Fld101 = \'{self.position}\'')

			results = execute_query(conn, query)
			conn.close()
			if results:

				return True
			else:
				return False

		else:
			raise Exception("Не удалось подключиться к базе данных.")

	def add_employee(self):
		conn = get_connection()
		if conn:
			query = (f'INSERT INTO _Reference92 '
					 f'(_IDRRef, _Marked, _PredefinedID, _Code, _Description, '
					 f'_Fld93, _Fld94, _Fld95, _Fld96, _Fld97, _Fld98, _Fld99, _Fld101, _Fld102, _Fld103, _Fld104) '
					 f'VALUES ('
					 f'CONVERT(binary(16), NEWID()), '
					 f'0, '
					 f'CONVERT(binary(16), \'\'), '
					 f'(SELECT FORMAT(MAX(_Code) + 1, \'d9\') FROM _Reference92), '
					 f'\'{self.second_name} {self.name} {self.surname}\', '
					 f'\'{self.second_name}\', '
					 f'\'{self.name}\', '
					 f'\'{self.surname}\', '
					 f'47, '
					 f'\'20220401\', '
					 f'\'00010101\', '
					 f'0, '
					 f'\'{self.position}\', '
					 f'\'А\');'
					 f'39800, '
					 f'35, ')

			results = execute_query(conn, query)
			conn.close()
			if results:

				return True
			else:
				return False

		else:
			raise Exception("Не удалось подключиться к базе данных.")

employees = EmployeeManagement('Безгалкин', 'Игорь', 'Ахматович', 'Механик')
# empl_list = employees.get_employees_list()
#
# for elem in empl_list:
# 	print(elem)

# employees.save_employees_list_to_file()

# employees.add_employee()

employees.update_salary(36900)








#################################
# Liskov Substitution Principle #
#################################

# class Rectangle:
#     def __int__(self, width, height):
#         self.width = width
#         self.height = height




# class Journal:
#     def __init__(self):
#         self.entries = []
#         self.count = 0
#
#     def add_entry(self, text):
#         self.count += 1
#         self.entries.append(f'{self.count}: {text}')
#
#     def __str__(self):
#         return '\n'.join(self.entries)
#
#     # def save(self, filepath):
#     #     file = open(filepath, 'w')
#     #     file.write(str(self))
#     #     file.close()
#
# class PersistenceManager:
#     @staticmethod
#     def save_to_file(journal, filepath):
#         file = open(filepath, 'w')
#         file.write(str(journal))
#         file.close()
#
# if __name__ == '__main__':
#     j = Journal()
#     j.add_entry('Я проснулся')
#     j.add_entry('Умылся')
#     j.add_entry('Побрился')
#     j.add_entry('Отжался')
#     j.add_entry('Наступил на кота')
#
#     print(f'Что я сегодня сделал:\n{j}')
#
#     filepath = r'C:\Users\Константин\Desktop\journal.txt'
#
#     PersistenceManager.save_to_file(j, filepath)