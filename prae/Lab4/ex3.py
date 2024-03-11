class Student:
    def __init__(self, stu_id, stu_name, year):
        self.id = stu_id
        self.name = stu_name
        self.year = year
        self.mentor = None
        
def find_object(id, objects):
    for object in objects:
        if id == object.id: 
            return object
        
def search_mentor (id): ## 3
    mentor_list = []
    student = find_object(id, students) 
    x = student.mentor
    while x != None:
        mentor_list.append(x.id + ' : ' + x.name)
        x = x.mentor
    return mentor_list                  
                           
def is_mentor (stu_x, stu_y): ## 4
    x = find_object(stu_x, students)
    y = find_object(stu_y, students)
    stu1 = x; stu2 = y
    if x.year > y.year: 
        stu1 = y; stu2 = x    
    m = stu1.mentor
    while m != None:
        if stu2 == m:
            return True
        m = m.mentor    
    return False              
    
# Student instances
student_id = ("66010853", "65010241", "64010758", "63010439", "66010933", "65010716")
student_name = ("Dylan", "Villiam", "Jack", "Rose", "Gojo", "Yuji")
students = []
for i in range(6): 
    if i == 4 or i == 5: 
        students.append(Student(student_id[i], student_name[i], i-3))
    else: 
        students.append(Student(student_id[i], student_name[i], i+1))
for i in range(6):
    if i != 3 and i != 5: students[i].mentor = students[i+1]
       
# Variable
search_id = "66010853"
stu_x = "63010439"; stu_y = "65010241"
print(search_mentor(search_id))
print(is_mentor(stu_x, stu_y))