class Student :
    def __init__ (self, stu_id, name) :
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.sub = []
class Subject :
    def __init__ (self, sub_id, sub_name, sec, cre) :
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.sec = sec
        self.cre = cre
        self.stu_list = []
        self.teacher = ''
class Teacher :
    def __init__ (self, teacher_id, teacher_name) :
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_sub = ''
stu_name = ['louis','prae','som','beam','mark']
stu = [Student('00'+str(i) , stu_name[i])for i in range(0,5)]
tea = [Teacher('200','KruMuay'),Teacher('201','KruRuay')]
sub = [Subject("01076105", "OOP", 16, 3) , Subject("01076105", "OOP", 17, 3)]
sub[0].teacher = tea[0].teacher_name
sub[1].teacher = tea[1].teacher_name
for i in range(0,2) :
    sub[0].student_list.append(stu[i].name)
    stu[i].sub.append(sub[0].subject_name)
for i in range(2,5) :
    sub[1].student_list.append(stu[i].name)
    stu[i].sub.append(sub[0].subject_name)

def search_stu_id(id) : 
    [print(i.sub) for i in stu if i.stu_id==id]
def search_teacher_id(id) :
    [print(sub[i].student_list) for i in range(2) if tea[i].teacher_id == id and tea[i].teacher_name == sub[i].teacher]

# id = input('id : ')
# if id[0] == '2':

# elif id[0] == '0':
search_stu_id('000')
search_teacher_id('200')