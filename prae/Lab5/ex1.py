class Student:
    def __init__(self, stu_id, stu_name):
        self.__stu_id = stu_id
        self.__stu_name = stu_name
    
    ## GET ZONE ##
    def get_id(self): # ID
        return self.__stu_id
    
    def get_name(self): # Name
        return self.__stu_name       

class Teacher:
    def __init__(self, tc_id, tc_name):
        self.__tc_id = tc_id
        self.__tc_name = tc_name
    
    ## GET ZONE ##    
    def get_id(self): # ID
        return self.__tc_id
    
    def get_name(self): # Name
        return self.__tc_name
    '''
    ## SET ZONE ##
    # def set_id(self, tc_id): # ID
    #     if tc_id.isnumeric() and len(tc_id) == 8:
    #         self.__tc_id = tc_id
    #     else:
    #         raise ValueError("Invalid Teacher ID")
        
    # def set_name(self, tc_name): # Name
    #     if tc_name.isalpha():
    #         self.__tc_name = tc_name
    #     else:
    #         raise ValueError("Invalid Teacher Name")'''       
                
class Subject:
    def __init__(self, sub_id, sub_name, credit):
        self.__sub_id = sub_id
        self.__sub_name = sub_name
        self.__sub_credit = credit
        self.__sub_teacher = None
    
    ## GET ZONE ##    
    def get_id(self): # ID
        return self.__sub_id
    
    def get_name(self): # Name
        return self.__sub_name
    
    def get_credit(self): # Credit
        return self.__sub_credit
    
    # TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา 
    def get_teacher_teach(self): # Teacher
        if self.__sub_teacher != None:
            return self.__sub_teacher
        else:
            return "Not Found"
        
    ## SET ZONE ##   
    def assign_teacher(self, teacher): # Teacher
        if isinstance(teacher, Teacher):
            self.__sub_teacher = teacher
        else:
            raise ValueError("Invalid Subject Teacher")

class Enrollment:
    def __init__(self, student, subject, grade = None):
        self.__student = student
        self.__subject = subject
        self.__grade = grade
    
    ## GET ZONE ##
    def get_student(self):
        return self.__student

    def get_subject(self):
        return self.__subject

    def get_grade(self):
        return self.__grade
    
    ## SET ZONE ##
    def set_grade(self, grade):
        if grade in ['A', 'B', 'C', 'D', 'F'] and len(grade) == 1:
            self.__grade = grade
        else:
            raise ValueError("Invalid Grade")   

students = []
subjects = []
teachers = []
enrollment_list = []

# TODO 1 : function สำหรับค้นหา instance ของวิชาใน subject_list
def search_subject_by_id(subject_id):
    for subject in subjects:
        if subject.get_id() == subject_id:
            return subject

# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id):
    for student in students:
        if student.get_id() == student_id:
            return student
    
# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(subject, student):
    if isinstance(student, Student) and isinstance(subject, Subject):
        for enrollment in enrollment_list:
            if enrollment.get_student() == student and enrollment.get_subject() == subject:
                return enrollment
        return "Not Found" 
    else:
        return "Error"

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject                
def enroll_to_subject(student, subject):
    if search_enrollment_subject_student(subject, student) != "Error" and search_enrollment_subject_student(subject, student) != "Not Found":
        return "Already Enrolled"
    elif search_enrollment_subject_student(subject, student) == "Not Found":
        enrollment_list.append(Enrollment(student, subject))
        return "Done"       
    else:
        return "Error"
        
# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student, subject):
    if search_enrollment_subject_student(subject, student) != "Error" and search_enrollment_subject_student(subject, student) != "Not Found":
        enrollment_list.remove(search_enrollment_subject_student(subject, student))
        return "Done"          
    else:
        return search_enrollment_subject_student(subject, student)        

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject):
    lst = []
    if isinstance(subject, Subject):
        for enrollment in enrollment_list:
            if enrollment.get_subject() == subject:
                lst.append(enrollment)
        return lst           
    else:
        return "Error"

# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student):
    lst = []
    if isinstance(student, Student):
        for enrollment in enrollment_list:
            if enrollment.get_student() == student:
                lst.append(enrollment)
        return lst           
    else:
        return "Error"

# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student, subject, grade):
    enroll = search_enrollment_subject_student(subject, student)
    enroll.set_grade(grade)
    return "Done"

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject):
    if isinstance(subject, Subject):
        return len(search_student_enroll_in_subject(subject))                   
    else:
        return "Not Found"

# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’] }
def get_student_record(student):
    record = {}
    for enrollment in enrollment_list:
        if enrollment.get_student() == student:
            record[enrollment.get_subject().get_id()] = [enrollment.get_subject().get_name(), enrollment.get_grade()]
    return record

# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student):
    gps = 0; credit_taken = 0
    enrolled_sub = get_student_record(student)
    for sub_id, sub_grade in enrolled_sub.items():
        subject = search_subject_by_id(sub_id)
        gps += subject.get_credit() * grade_to_count(sub_grade[1])
        credit_taken += subject.get_credit()
    return f"{gps / credit_taken:.2f}"

# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    for enrollment in filter_student_list:
        student_dict[enrollment.get_student().get_id()] = enrollment.get_student().get_name()
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    filter_subject_list = search_subject_that_student_enrolled(student)
    subject_dict = {}
    for enrollment in filter_subject_list:
        subject_dict[enrollment.get_subject().get_id()] = enrollment.get_subject().get_name()
    return subject_dict                               
                    
# สร้าง instance พื้นฐาน            
def create_instance():             
    student_id = ("66010853", "66010241", "66011758", "66010439", "66010933", "66010516", "66011682", "66011129", "66010201", "66011374")
    student_name = ("Dylan", "Villiam", "Jack", "Rose", "Gojo", "Yuji", "Jennie", "Kaine", "Liliana", "Violet")
    for i in range(10): students.append(Student(student_id[i], student_name[i]))       

    teacher_id = ("T001", "T002", "T003")
    teacher_name = ("Thana Hongsuwan", "Amnach Khawne", "Kleddao Satcharoen")
    for i in range(3): teachers.append(Teacher(teacher_id[i], teacher_name[i]))

    subject_id = ("CS101", "CS102", "CS103")
    subject_name = ("Object Oriented Programming", "Circuits and Electronics", "Charm School")
    for i in range(3): subjects.append(Subject(subject_id[i], subject_name[i], 3))

    for i in range(3): subjects[i].assign_teacher(teachers[i])

# ลงทะเบียน
def register():
    enroll_to_subject(students[0], subjects[0])  # 001 -> CS101
    enroll_to_subject(students[0], subjects[1])  # 001 -> CS102
    enroll_to_subject(students[0], subjects[2])  # 001 -> CS103
    enroll_to_subject(students[1], subjects[0])  # 002 -> CS101
    enroll_to_subject(students[1], subjects[1])  # 002 -> CS102
    enroll_to_subject(students[1], subjects[2])  # 002 -> CS103
    enroll_to_subject(students[2], subjects[0])  # 003 -> CS101
    enroll_to_subject(students[2], subjects[1])  # 003 -> CS102
    enroll_to_subject(students[2], subjects[2])  # 003 -> CS103
    enroll_to_subject(students[3], subjects[0])  # 004 -> CS101
    enroll_to_subject(students[3], subjects[1])  # 004 -> CS102
    enroll_to_subject(students[4], subjects[0])  # 005 -> CS101
    enroll_to_subject(students[4], subjects[2])  # 005 -> CS103
    enroll_to_subject(students[5], subjects[1])  # 006 -> CS102
    enroll_to_subject(students[5], subjects[2])  # 006 -> CS103
    enroll_to_subject(students[6], subjects[0])  # 007 -> CS101
    enroll_to_subject(students[7], subjects[1])  # 008 -> CS102
    enroll_to_subject(students[8], subjects[2])  # 009 -> CS103

create_instance()
register()

### Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
# print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")

# ### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
# print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

# ### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
# print("Answer : Already Enrolled")
print(enroll_to_subject(students[0], subjects[0]))
print("")

# ### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
# print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

# ### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
# print("Answer : Not Found")
print(drop_from_subject(students[8], subjects[0]))
print("")

# ### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
# print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(students[0], subjects[0])
print(list_student_enrolled_in_subject(subjects[0].get_id()))
print("")

# ### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
# print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subjects[0])
print([i.get_student().get_id() for i in lst])
print("")

# ### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
# print("Answer : 5")
print(get_no_of_student_enrolled(subjects[0]))
print("")

# ### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
# print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(students[0])
print([i.get_subject().get_id() for i in lst])
print("")

# ### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
# print("Answer : Mr. Welsh")
print(subjects[0].get_teacher_teach().get_name())
print("")

# ### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
# print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subjects[0],students[1])
print(enroll.get_subject().get_id(), enroll.get_student().get_id())
print("")

# ### Test case #12 : assign_grade
print("Test case #12 assign_grade")
# print("Answer : Done")
assign_grade(students[1],subjects[0],'A')
assign_grade(students[1],subjects[1],'B')
print(assign_grade(students[1],subjects[2],'C'))
print("")

# ### Test case #13 : get_student_record
print("Test case #13 get_student_record")
# print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(students[1]))
print("")

# ### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
# print("Answer : 3.0")
print(get_student_GPS(students[1]))