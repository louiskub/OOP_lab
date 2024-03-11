class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name
        self.sub_list = []

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
                
class Subject:
    def __init__(self, sub_id, sub_name, section, credit):
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.section = section
        self.credit = credit
        self.stu_list = []
        self.teacher = ''
       
stu1 = Student("001", "Dylan")
stu2 = Student("002", "Villiam")
stu3 = Student("003", "Jack")
stu4 = Student("004", "Rose")
stu5 = Student("005", "Gojo")
student = [stu1, stu2, stu3, stu4, stu5]

teacher1 = Teacher("016", "Orachat Chitsobhuk")
teacher2 = Teacher("017", "Thana Hongsuwan")
teacher = [teacher1, teacher2]

sub1 = Subject("016", "OOP", 16, 3)
sub2 = Subject("017", "OOP", 17, 3)
subject = [sub1, sub2]
for i in range(2): subject[i].teacher = teacher[i]
for i in range(3): 
    sub1.stu_list.append(student[i])
    student[i].sub_list.append(sub1)
for i in range(3, 5): 
    sub2.stu_list.append(student[i])
    student[i].sub_list.append(sub2)

#print(sub1.stu_list)
#print(sub2.stu_list)
#print(stu1.sub_list)
search_id = input()

for i in student: 
    if search_id == i.stu_id:
        print(i.sub_list) 
for i in range(2):
    if search_id == teacher[i].teacher_id:
        print(subject[i].stu_list)