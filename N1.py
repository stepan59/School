import json
import os
DIR = ''

def full_name(data):
    for el in data:
        print(el['name'], el['middle_name'], el['surname'])

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
    for el in teachers_data:
        if teacher_name == el['name'] and teacher_srn == el['surname'] and teacher_middle_name == el['middle_name']:
            teachers_data.remove(el)
            print(el['name'], el['middle_name'], el['surname'])
            print('Уволен')
            save(teachers_data, 'Teachers_new.json')

students_data = json.load(open(os.path.join(DIR, 'Students_id.json'), 'r'))
teachers_data = json.load(open(os.path.join(DIR, 'Teachers_id.json'), 'r'))
clasnum = input('Введите номер желаемого класса :')
# поседний id студентов
for el in students_data:
   last_students_id = el['id']
# поседний id учеников
for el in teachers_data:
   last_teachers_id = el['id']


print()
print('Все ученики -')
full_name(students_data)

print()
print('Учителя -')
full_name(teachers_data)

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
        
# 3.1 добавления нового ученика
student = {'id': last_students_id+1,
            'name': 'Петр',
            "middle_name": 'Сергеевич',
            "surname": 'Иванов',
            "school": "12 гимназия",
            "class": "7 В",
            "birth_day": "21.05.1995"}
students_data.append(student)
save(students_data, 'Students_new.json')
# 3.2  добавление учителей
teacher = {'id' : last_teachers_id+1,
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
teacher_id = "4"
added_class = '4 А'
for el in teachers_data:
    if teacher_id == el['id']:
        el['class'].append(added_class)
save(teachers_data, 'Teachers_new.json')
print('Успех')

# 3.4 Добавьте возможность удаления ученика по заданному полному имени
print('3.4 Добавьте возможность удаления ученика по заданному полному имени')
print()
expel_by_name(students_data, "Артем", "Валерьевич", "Кузин")
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
dismissal_by_name(teachers_data, "Александр", "Сергеевич", "Черный")
print()

# 3.7 удаления всех учителей из указанной школы
print('3.7 удаления всех учителей из указанной школы')
print()
teacher_list = []
dismissal("12 гимназия", teachers_data, teacher_list)
print()

# 3.8 удаление указанных классов у указанного преподавателя
print('3.8 удаление указанных классов у указанного преподавателя')
teacher_id = "1"
del_class = '6 А'
for el in teachers_data:
    if teacher_id == el['id']:
        el['class'].remove(del_class)
save(teachers_data, 'Teachers_new.json')
print('Успех')


