"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    persons = [{'name':'Tom', 'age':'18', 'job': 'builder'},
               {'name':'Jhon', 'age':'25', 'job': 'teacher'},
               {'name':'Peter', 'age':'31', 'job': 'buisnesman'},
               {'name':'Mary', 'age':'37', 'job': 'lawer'}]
    with open('persons.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for person in persons:
            writer.writerow(person)

if __name__ == "__main__":
    main()
