class Student:
    def __init__(self, stu_id, stu_name, year, menter):
        self.id = stu_id
        self.name = stu_name
        self.year = year
        self.menter = menter
        self.sub_list = []
        self.menter_list = []

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
        if id == teacher[i].id and subject[i].teacher == teacher[i].name:
            return subject[i].stu_list
    
def search_stu_id (student, id): ## 2
    for i in student:
        if id == i.id: return i.sub_list 

def search_menter (student, stu_x): ## 3
    for i in range(6):
        if (stu_x == student[i].id): return student[i].menter_list
        
def menter_or_not (student, stu_x, stu_y): ## 4
    for i in range(6):
        if stu_x == student[i].id:
            for j in student[i].menter_list:
                for k in j:
                    if stu_y == k: return True
        elif stu_y == student[i].id:
            for j in student[i].menter_list:
                for k in j:
                    if stu_x == k: return True
    return False 

# Student instances
student_id = ("66010853", "65010241", "64010758", "63010439", "66010933", "65010716")
student_name = ("Dylan", "Villiam", "Jack", "Rose", "Gojo", "Yuji")
student = []
for i in range(6): 
    if i == 3: student.append(Student(student_id[i], student_name[i], i+1, '-'))
    elif i == 4: student.append(Student(student_id[i], student_name[i], i-3, [student_id[i+1], student_name[i+1]]))
    elif i == 5: student.append(Student(student_id[i], student_name[i], i-3, '-'))
    else: student.append(Student(student_id[i], student_name[i], i+1, [student_id[i+1], student_name[i+1]]))
for i in range(6): student[i].menter_list.append(student[i].menter)
for i in range(6):
    count = 0
    for j in range(6):
        if student[j].id in student[i].menter_list[count] and student[j].menter != '-':
            student[i].menter_list.append(student[j].menter)
            count += 1         

# Teacher instances
teacher_id = ("016", "017")
teacher_name = ("Orachat Chitsobhuk", "Thana Hongsuwan")
teacher = [Teacher(teacher_id[i], teacher_name[i]) for i in range(2)]

# Subject instances
sub1 = Subject("01076105", "Object Oriented Programming", 16, 3)
sub2 = Subject("01076105", "Object Oriented Programming", 17, 3)
subject = [sub1, sub2]
for i in range(2): subject[i].teacher = teacher[i].name
for i in range(3): 
    sub1.stu_list.append(student[i].name)
    student[i].sub_list.append(sub1.name)
for i in range(3, 6): 
    sub2.stu_list.append(student[i].name)
    student[i].sub_list.append(sub2.name)

# Variable
stu_x = "65010241"; stu_y = "63010439"
print(search_tc_id(teacher, "016"))
print(search_stu_id(student, "65010716"))
print(search_menter(student, stu_x))
print(menter_or_not(student, stu_x, stu_y))