class Student :
    def __init__ (self, stu_id, stu_name, stu_menter) :
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_menter = stu_menter    # id ของพี่รหัส

# Set ค่า
student_name = ['louis','prae','som','beam','mark']
student_id =     ['66000000', '65000000', '64000000', '63000000', '62000000']
student_menter = ['65000000', '64000000', '63000000', '62000000', '']
stu = [Student(student_id[i] , student_name[i], student_menter[i] )for i in range(0,5)]

def search_name(id) :
    for i in stu :  # loop ใน stu
        if i.stu_id == id : #ถ้าidตรง returnชื่อ
            return i.stu_name
def search_index(id):
    for i in range(len(stu)) :   # loop ใน stu
        if stu[i].stu_id == id : #ถ้าidตรง returnตำแหน่งที่เจอ
            return i
def checkMenter(id) :
    for i in stu :
        if i.stu_id == id and i.stu_menter != '':   #ถ้าidตรง และ ต้องมีmenter
            lst = [i.stu_menter +' : '+ search_name(i.stu_menter)] # สร้างlst โดยมีทั้งชื่อและidในนั้น
            recur = checkMenter(i.stu_menter)   #เรียกฟังชั่นตัวเอง โดยพาสค่าIdของMenter
            if recur != 'none':                 #ถ้า recur!='none' ให้เอาลิสมารวมกัน
                lst = lst+recur
            return lst                          
    return 'none'   #ถ้าไม่เข้าตรงif returnไม่มี
        
def isRelated(id1,id2) :                   
    # id2ตัวแรกของid คือรหัสปี    
    # ถ้าหากปีมีมากกว่า ก็ให้เรียกใช้ฟังชั่นcheckMenterโดยพาสIdของปีที่มากกว่าไป
    # หลังจากนั้นเชคว่าใน Stringยาวๆ มีIdของปีที่น้อยกว่าอยู่ข้างในนั้นมั้ย
    if id1[0:2] > id2[0:2] :                    
        return id2 in str(checkMenter(id1))
    elif id1[0:2] < id2[0:2] :
        return id1 in str(checkMenter(id2))
    else :
        return False

print(checkMenter('64000000'))
print(isRelated('66000000','64000000'))
