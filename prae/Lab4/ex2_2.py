class Student:
    def __init__(self, stu_id, stu_name):
        self.id = stu_id
        self.name = stu_name
        self.sub_list = []

class Teacher:
    def __init__(self, tc_id, tc_name):
        self.id = tc_id
        self.name = tc_name
                
class Subject:
    def __init__(self, sub_id, sub_name, section, credit):
        self.id = sub_id
        self.name = sub_name
        self.section = section
        self.credit = credit
        self.stu_list = []
        self.teacher = ''
        
def search_tc_id (teacher, id): ## 1
    for i in range(2):
        if id == teacher[i].id and subjects[i].teacher == teacher[i].name:
            return subjects[i].stu_list
    
def search_stu_id (student, id): ## 2
    for i in student: 
        if id == i.id: return i.sub_list  

student_id = ("66010853", "65010241", "64010758", "63010439", "66010933")
student_name = ("Dylan", "Villiam", "Jack", "Rose", "Gojo")
students = [Student(student_id[i], student_name[i]) for i in range(5)]       

teacher_id = ("016", "017")
teacher_name = ("Orachat Chitsobhuk", "Thana Hongsuwan")
teachers = [Teacher(teacher_id[i], teacher_name[i]) for i in range(2)]

sub1 = Subject("01076105", "Object Oriented Programming", 16, 3)
sub2 = Subject("01076105", "Object Oriented Programming", 17, 3)
subjects = [sub1, sub2]

for i in range(2): subjects[i].teacher = teachers[i]
for i in range(3): 
    sub1.stu_list.append(students[i])
    students[i].sub_list.append(sub1)
for i in range(3, 5): 
    sub2.stu_list.append(students[i])
    students[i].sub_list.append(sub2)

print(search_tc_id(teachers, "016"))
#print(search_stu_id(student, "66010853"))