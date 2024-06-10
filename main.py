class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filepath):
    #     file = open(filepath, 'w')
    #     file.write(str(self))
    #     file.close()

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filepath):
        file = open(filepath, 'w')
        file.write(str(journal))
        file.close()

if __name__ == '__main__':
    j = Journal()
    j.add_entry('Я проснулся')
    j.add_entry('Умылся')
    j.add_entry('Побрился')
    j.add_entry('Отжался')
    j.add_entry('Наступил на кота')

    print(f'Что я сегодня сделал:\n{j}')

    filepath = r'C:\Users\Константин\Desktop\journal.txt'

    PersistenceManager.save_to_file(j, filepath)

    # j.save(filepath)
    # ddd11