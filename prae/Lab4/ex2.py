class Student:
    def __init__(self, stu_id, stu_name):
        self.id = stu_id
        self.name = stu_name

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
        self.teacher = None
        self.stu_list = []
        
def search_teacher (teacher_id): ## 1
    for subject in subjects:
        if teacher_id == subject.teacher.id:
            return [student.name for student in subject.stu_list]
    
def search_student (student_id): ## 2
    subjects_list = []
    for subject in subjects:
        for student in subject.stu_list:
            if student_id == student.id:
                subjects_list.append(str(subject.section) + " : " + subject.name)
    return subjects_list
      

student_id = ("66010853", "65010241", "64010758", "63010439", "66010933")
student_name = ("Dylan", "Villiam", "Jack", "Rose", "Gojo")
students = [Student(student_id[i], student_name[i]) for i in range(5)]       

teacher_id = ("016", "017")
teacher_name = ("Orachat Chitsobhuk", "Thana Hongsuwan")
teachers = [Teacher(teacher_id[i], teacher_name[i]) for i in range(2)]

sub1 = Subject("01076105", "Object Oriented Programming", 16, 3)
sub2 = Subject("01076105", "Object Oriented Programming", 17, 3)
subjects = [sub1, sub2]
sub1.teacher = teachers[0]
sub2.teacher = teachers[1]
sub1.stu_list = [students[i] for i in range(3)] 
sub2.stu_list = [students[i] for i in range(3, 5)]

print(search_teacher(teachers[1].id))
print(search_student(students[1].id))