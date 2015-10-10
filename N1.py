import json
import os
DIR = ''

def get_teachers(teacher_name, teacher_data):
    name, surname = teacher_name.split(" ")
    for teacher in teacher_data:
        if teacher["name"] == name and teacher["surname"] == surname:
            return teacher

def save(data, file_name):
    file = open(os.path.join(DIR, file_name), 'w', encoding='utf8')
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()
# уничтожение ученика
def expel(students_class, students_data, students_list):
    for el in students_data:
        if el['class'] != students_class:
            students_list.append(el)
        else:
            print(el['name'], el['middle_name'], el['surname'])
            print('Выгнан')
        save(students_list, 'Students_new.json')
# увольнение учителя
def dismissal(school, teachers_data, teachers_list):
    for el in teachers_data:
        if el['school'] != school:
            teachers_list.append(el)
        else:
            print(el['name'], el['middle_name'], el['surname'])
            print('Уволен')
        save(teacher_list, 'Teachers_new.json')

def expel_by_name(students_data, students_name, students_middle_name, students_srn):
    for el in students_data:
        if students_name == el['name'] and students_srn == el['surname'] and students_middle_name == el['middle_name']:
            students_data.remove(el)
            print(el['name'], el['surname'], el['middle_name'])
            print("Выгнан")
        save(students_data, 'Students_new.json')
def dismissal_by_name(teachers_data, teacher_name, teacher_middle_name, teacher_srn):
    class_list = ['6 А', "8 Б", "7 В", '7 А']
    for el in teachers_data:
        if teacher_name == el['name'] and teacher_srn == el['surname'] and teacher_middle_name == el['middle_name']:
            teachers_data.remove(el)
            print(el['name'], el['middle_name'], el['surname'])
            print('Уволен')
            save(teachers_data, 'Teachers_new.json')

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


# 3.1 добавления нового ученика
student = {'name': 'Петр',
            "middle_name": 'Сергеевич',
            "surname": 'Иванов',
            "school": "12 гимназия",
            "class": "7 В",
            "birth_day": "21.05.1995"}
students_data.append(student)
# 3.2  добавление учителей
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

# 3.3 добавлять классы (которые он ведет) к указанному преподавателю
print('3.3 добавлять классы (которые он ведет) к указанному преподавателю')
teachers_data_n = json.load(open(os.path.join(DIR, 'Teachers_new.json'), 'r'))
teacher_name = "Максим"
teacher_srn = "Козлов"
added_class = '4 А'
for el in teachers_data_n:
    if teacher_name == el['name'] and teacher_srn == el['surname']:
        el['class'].append(added_class)
        print(el['class'])
    save(teachers_data_n, 'Teachers_new.json')
print('Успех')

# 3.4 Добавьте возможность удаления ученика по заданному полному имени
print('3.4 Добавьте возможность удаления ученика по заданному полному имени')
print()
students_data_n = json.load(open(os.path.join(DIR, 'Students_new.json'), 'r'))
expel_by_name(students_data_n, "Артем", "Валерьевич", "Кузин")
print()

# 3.5 удаление всех учеников из класса
print('3.5 удаление всех учеников из класса')
print()
students_list = []
expel('6 А', students_data, students_list)
print()

# 3.6 удаление учителя по полному имени(Ф.И.О.)
print('3.6 удаление учителя по полному имени(Ф.И.О.)')
print()
teachers_data_n = json.load(open(os.path.join(DIR, 'Teachers_new.json'), 'r'))
dismissal_by_name(teachers_data_n, "Александр", "Сергеевич", "Черный")
print()

# 3.7 удаления всех учителей из указанной школы
print('3.7 удаления всех учителей из указанной школы')
print()
teacher_list = []
dismissal("12 гимназия", teachers_data, teacher_list)
print()

# 3.8 удаление указанных классов у указанного преподавателя


