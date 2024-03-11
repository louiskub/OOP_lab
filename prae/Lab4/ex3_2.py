class Student:
    def __init__(self, stu_id, stu_name, year):
        self.id = stu_id
        self.name = stu_name
        self.year = year
        self.mentor = None
        
def searchMentor (id): ## 3
    mentor_list = []   
    for student in students:
        if id == student.id:
            x = student.mentor
            while x != None:
                mentor_list.append(x.id + ' : ' + x.name)
                x = x.mentor
    return mentor_list                  
                           
def isMentor (stu_a, stu_b): ## 4
    for student in students:
        if stu_a == student.id:
            x = student.mentor
            while x != None:
                if stu_b == x.id:
                    return True
                x = x.mentor
        if stu_b == student.id:
            x = student.mentor
            while x != None:
                if stu_a == x.id:
                    return True
                x = x.mentor
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
print(searchMentor(search_id))
print(isMentor(stu_x, stu_y))