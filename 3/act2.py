class Student :
    def __init__ (self, stu_id, stu_name) :
        self.stu_id = stu_id
        self.stu_name = stu_name
class Subject :
    def __init__ (self, sub_id, sub_name, sec, cre) :
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.sec = sec      
        self.cre = cre      
        self.stu_list = []  #ในวิชานี้มีใครเรียนบ้าง
        self.tea = ''       #อาจารย์วิชานี้ชื่ออะไร
class Teacher :
    def __init__ (self, tea_id, tea_name) :
        self.tea_id = tea_id
        self.tea_name = tea_name
# Set ค่าต่างๆ
student_name = ['louis','prae','som','beam','mark']
student_id = ['66000000', '65000000', '64000000', '63000000', '62000000']
teacher_name = ["Orachat Chitsobhuk", "Thana Hongsuwan"]
teacher_id = ["016", "017"]

stu = [Student(student_id[i] , student_name[i])for i in range(len(student_id))]
tea = [Teacher(teacher_id[i] , teacher_name[i])for i in range(len(teacher_id))]
sub = [Subject("01076105", "OOP", '16', 3) , Subject("01076105", "OOP", '17', 3)]

# ใส่ชื่อครูผู้สอนในแต่ละวิชา
sub[0].tea = tea[0].tea_name    
sub[1].tea = tea[1].tea_name

# เพิ่มนักเรียนในวิชา และ เพิ่มวิชาที่นักเรียนลง
for i in range(0,2) :   
    sub[0].stu_list.append(stu[i].stu_name)
for i in range(2,5) :
    sub[1].stu_list.append(stu[i].stu_name)

def search_stu_id(id) : 
    name = ''   # สร้างตัวแปรnameไว้เก็บชื่อ
    for i in stu :  
        if i.stu_id==id :   # ถ้าIDตรง ให้ name = ชื่อของคนที่ใช้idนั้น
            name = i.stu_name
            break
    
    lst = []    # สร้างตัวแปรlst ไว้เก็บวิชาทั้งหมดที่เรียน
    for i in sub : 
        if name in i.stu_list : # ถ้าname อยู่ในวิชานั้น ให้เพิ่มชื่อวิชาในlst
            lst.append(i.sub_name)
    return lst

def search_teacher_id(id) :
    # loopในteaกับsub 
    # ถ้าเจออาจารย์ที่มีidตรงกับค่าid และ ชื่ออาจารย์คนนั้นตรงกับชื่ออาจารย์ผู้สอนในวิชานั้น ให้return list นักเรียนวิชานั้น
    # แต่ถ้าไม่เจอ return 'not found'
    for i in range(len(tea)) :  
        for j in range(len(sub)) :
            if tea[i].tea_id == id and tea[i].tea_name == sub[j].tea :  
                return sub[j].stu_list
    return 'not found'

print(search_teacher_id('016'))
print(search_stu_id('66000000'))

# input()          
# inp = input('ใส่รหัสผู้สอน : ')
# [print(i,end=' ') for i in search_teacher_id(inp)]
# inp = input('\nใส่รหัสนศ : ')
# [print(i,end=' ') for i in search_stu_id(inp)]