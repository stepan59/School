import json
import os
DIR = ''

def get_teachers(teacher_name,teacher_data):
    name, surname = teacher_name.split(" ")
    for teacher in teacher_data:
        if teacher["name"] == name and teacher["surname"] == surname:
            return teacher

def save(data,file_name):
    file = open(os.path.join(DIR, file_name), 'w', encoding='utf8')
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()



students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))
teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))
clasnum = input('Введите номер желаемого класса :')


print()
print('Все ученики -')
for el in students_data:
    print(el['name'])

print()
print('Учетеля -')
for el in teachers_data:
    print(el['name'])

print()
print('Ученики из заданого класса - ')
for el in students_data:
    if (el['class']) == clasnum:
        print(el['name'], el['surname'])

print()
school = []
print('Номера школ -')
for el in teachers_data:
    school.append(el['school'])
for el in set(school):
    print(el)

print()
ls = []
print('Однофамильцы - ')
for el in students_data:
    ls.append(el['surname'])
for el in ls:
    if ls.count(el) > 1:
        print(el)

print()
i = 0
# teachers_name = input("Введите имя учителя - ")
# teachers_surname = input("Введите фамилию учителя - ")
# teachers_name = 'Александр'
# teachers_surname = "Черный"
# for el in teachers_data:
#     if el['name'] == teachers_name and el['surname'] == teachers_surname:
#         i = 1
#         clas = el['class']
#         print(clas)
#         break
#     else:
#         i = 0
# if i != 1:
#     print("Нет такого учителя")
# else:
#     print('Все в порядке')
# 2.1 добавления нового ученика
student = {'name': 'Петр',
            "middle_name": 'Сергеевич',
            "surname": 'Иванов',
            "school": "12 гимназия",
            "class": "7 В",
            "birth_day": "21.05.1995"}
students_data.append(student)
# 2.2  добавление учителей
save(students_data, 'Students_new.json')

teacher = {
    "name": "Максим",
    "middle_name": "Евгеньевич",
    "surname": "Козлов",
    "school": "67 школа",
    "class": [
      "6 А",
      "8 Б",
      "7 В"
    ],
    "birth_day": "07.08.1985"
  }
teachers_data.append(teacher)
save(teachers_data, 'Teachers_new.json')

# 2.3 добавлять классы (которые он ведет) к указанному преподавателю
teachers_data_n = json.load(open(os.path.join(DIR, 'Teachers_new.json'), 'r'))
teacher_name = "Максим"
teacher_srn = "Козлов"
class_list = ['6 А', "8 Б", "7 В", '7 А']
for el in teachers_data_n:
    if teacher_name == el['name'] and teacher_srn == el['surname']:
        el['class'] = class_list
        save(teachers_data_n, 'Teachers_new.json')

# 2.4 Добавьте возможность удаления ученика по заданному полному имени
students_data_n = json.load(open(os.path.join(DIR, 'Students_new.json'), 'r'))
students_name = "Артем"
students_middle_name = "Валерьевич"
students_srn = "Кузин"
for el in students_data:
    if students_name == el['name'] and students_srn == el['surname'] and students_middle_name == el['middle_name']:
        students_data.remove(el)
        save(students_data, 'Students_new.json')