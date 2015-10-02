__author__ = 'stepan'
import json
f = open('Students.json', 'r')
file = open('Teachers.json', 'r')
data = json.load(f)
d = json.load(file)
i = 0
teachers_name = input("Введите имя учителя - ")
teachers_surname = input("Введите фамилию учителя - ")
for el in d:
    if el['name'] == teachers_name and el['surname'] == teachers_surname:
        i = 1
        break
    else:
        i = 0
print(i)
if i != 1:
    print("Нет такого учителя")
else:
    print('Все в порядке')

print()
