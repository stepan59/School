import json

f = open('Students.json', 'r')
file = open('Teachers.json', 'r')
data = json.load(f)
d = json.load(file)
clasnum = input('Введите номер желаемого класса :')

# dd

print()
print('Все ученики -')
for el in data:
    print(el['name'])

print()
print('Учетеля -')
for el in d:
    print(el['name'])

print()
print('Ученики из заданого класса - ')
for el in data:
    if (el['class']) == clasnum:
        print(el['name'], el['surname'])

print()
school = []
print('Номера школ -')
for el in d:
    school.append(el['school'])
for el in set(school):
    print(el)

print()
ls = []
print('Однофамильцы - ')
for el in data:
    ls.append(el['surname'])
for el in ls:
    if ls.count(el) > 1:
        print(el)

print()
teachers_name = input("Введите имя учителя - ")
teachers_surname = input("Введите фамилию учителя - ")
