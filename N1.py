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
