class Student:
    def __init__(self, stu_id, stu_name, year, menter):
        self.id = stu_id
        self.name = stu_name
        self.year = year
        self.menter = menter
        self.menter_list = []

def search_menter (student, stu_x): ## 3
    for i in range(6):
        if (stu_x == student[i].id): return student[i].menter_list
        
    # for student in students:
    #     if stu_id == student.id:
    #         return student.menter_list
            
        
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

    # for student in students:
    #     if stu_x == student.id:
    #         for mentor in student.mentor_list:
    #             if mentor.id == stu_y:
    #                 return True
    #     if stu_y == student.id:
    #         for mentor in student.mentor_list:
    #             if mentor.id == stu_y:
    #                 return True
    # return False


    # x = findObject(stu_x)
    # y = findObject(stu_y)
    # if x in y.mentor_list or y in x.mentor_list:
    #     return True
    # return False

def findObject(student_id, students):
    for student in students:
        if student_id == student.id:
            return student
        
        
    
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
# Variable
stu_x = "65010241"; stu_y = "63010439"
print(search_menter(student, stu_x))
print(menter_or_not(student, stu_x, stu_y))