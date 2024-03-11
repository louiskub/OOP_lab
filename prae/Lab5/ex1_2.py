def is_alphabetic_string(str):
    for char in str:
        if char.isalpha() or char.isspace():
            continue
        else:
            return False
    return True

class Student:
    def __init__(self, stu_id, stu_name):
        self.__stu_id = stu_id
        self.__stu_name = stu_name
    
    ## GET ZONE ##
    def get_id(self): # ID
        return self.__stu_id
    
    def get_name(self): # Name
        return self.__stu_name
    
    ## SET ZONE ##
    def set_id(self, stu_id): # ID
        if stu_id.isnumeric() and len(stu_id) == 8:
            self.__stu_id = stu_id
        else:
            raise ValueError("Invalid Student ID")
           
    def set_name(self, stu_name): # Name
        if stu_name.isalpha():
            self.__stu_name = stu_name
        else:
            raise ValueError("Invalid Student Name")       

class Teacher:
    def __init__(self, tc_id, tc_name):
        self.__tc_id = tc_id
        self.__tc_name = tc_name
    
    ## GET ZONE ##    
    def get_id(self): # ID
        return self.__tc_id
    
    def get_name(self): # Name
        return self.__tc_name
    
    ## SET ZONE ##
    def set_id(self, tc_id): # ID
        if tc_id.isnumeric() and len(tc_id) == 8:
            self.__tc_id = tc_id
        else:
            raise ValueError("Invalid Teacher ID")
        
    def set_name(self, tc_name): # Name
        if tc_name.isalpha():
            self.__tc_name = tc_name
        else:
            raise ValueError("Invalid Teacher Name")       
                
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
    
    def get_teacher(self): # Teacher
        return self.__sub_teacher
    
    ## SET ZONE ##
    def set_id(self, sub_id): # ID
        if sub_id.isnumeric() and len(sub_id) == 8:
            self.__sub_id = sub_id
        else:
            raise ValueError("Invalid Subject ID")
        
    def set_name(self, sub_name): # Name
        if sub_name.isalpha():
            self.__sub_name = sub_name
        else:
            raise ValueError("Invalid Subject Name") 
      
student_id = ("66010853", "65010241", "64010758", "63010439", "66010933")
student_name = ("Dylan", "Villiam", "Jack", "Rose", "Gojo")
students = [Student(student_id[i], student_name[i]) for i in range(5)]       

teacher_id = ("00000016", "00000017", "00000018")
teacher_name = ("Thana Hongsuwan", "Amnach Khawne", "Kleddao Satcharoen")
teachers = [Teacher(teacher_id[i], teacher_name[i]) for i in range(3)]

sub1 = Subject("01076105", "Object Oriented Programming", 3)
sub2 = Subject("01076107", "Circuits and Electronics", 3)
sub3 = Subject("90642999", "Charm School", 3)
subjects = [sub1, sub2, sub3]

#students[1].set_name("June")
#students[0].set_id("6601020")
for student in students:
    print(student.get_id(), student.get_name())