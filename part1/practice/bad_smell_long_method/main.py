# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


class Filter:
    def __init__(self, str_file: str):
        self.str_file = str_file

    def get_users(self) -> list[dict]:
        data = self._read(self.str_file)
        sorted_data = self._sort(data)
        filtered_data = self._filter(sorted_data)
        return filtered_data

    @staticmethod
    def _read(str_file: str) -> list[dict]:
        list_users = [x.split(';') for x in str_file.split('\n')]
        list_users_dict = [{'name': name, 'age': int(age)} for name, age in list_users]
        return list_users_dict

    @staticmethod
    def _sort(data: list[dict]) -> list[dict]:
        return sorted(data, key=lambda person: person['age'])

    @staticmethod
    def _filter(sorted_data: list[dict]) -> list[dict]:
        return [person for person in sorted_data if person['age'] > 10]


if __name__ == '__main__':
    users_filter = Filter(csv)
    print(users_filter.get_users())
