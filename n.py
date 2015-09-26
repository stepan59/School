__author__ = 'stepan'
import json
f = open('Students.json', 'r')
file = open('Teachers.json', 'r')
data = json.load(f)
d = json.load(file)