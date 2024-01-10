# # • ให้แก้ไขคลาส student โดยเพิ่มข้อมูล พี่รหัส (student_menter) หมายถึงนักศึกษาที่เป็นพี่รหัสขึ้นไป 1
# # ชั้นปีเท่านั้น
# # • ให้สร้าง instance ของ นศ. 4 คนขึ้นไป เช่น a เป็นปี 1, b เป็นปี 2 และเป็นพี่รหัสของ a
# # c เป็นปี 3 และเป็นพี่รหัสของ b ส่วน d เป็นปี 4 และเป็นพี่รหัสของ c การสร้าง Instance ให้ใช้รหัส
# # นักศึกษา 8 หลัก และเลข 2 ตัวแรกตามชั้นปีจริง
# # – ให้เขียนฟังก์ชัน #3 โดยเมื่อป้อนรหัสนักศึกษา x แล้วตอบว่ามีพี่รหัส เป็นใครบ้าง โดยให้
# # ตอบให้ครบ เช่น ถ้าป้อน a ให้ตอบ b, c, d ถ้าป้อน b ให้ตอบ c, d โดยให้แสดงทั้งรหัส
# # นักศึกษาและชื่อ ในการแสดงให้แสดงกรณีไม่มีพี่รหัสด้วย
# # – ให้เขียนฟังก์ชัน #4 โดยเมื่อป้อนรหัสนักศึกษา Student x และ student y ให้ตรวจสอบว่าเป็น
# # สายรหัสกันหรือไม่ ให้ตอบเป็น True และ False
# # • โปรแกรมอาจแยกเขียนจากโปรแกรม 4.2 ก็ได้

class Student :
    def __init__ (self, stu_id, stu_name, stu_menter) :
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_menter = stu_menter
        self.sub = []
student_name = ['louis','prae','som','beam','mark']
student_name.append('')
student_id = ['66000000', '65000000', '64000000', '63000000', '62000000']
student_id.append('')
stu = [Student(student_id[i] , student_name[i], student_id[i+1])for i in range(0,5)]
#dict2.update(dict1)

def search_name(id) :
    for i in stu :
        if i.stu_id == id :
            return i.stu_name

def checkMenter(id) :
    for i in stu :
        if i.stu_id == id and i.stu_menter != '': 
            lst = [i.stu_menter +' : '+ search_name(i.stu_menter)]
            recur = checkMenter(i.stu_menter)
            if recur != 'none':
                lst = lst+recur
            return lst
    return 'none'
        
def isRelated(id1,id2) : 
    for i in stu :
        if i.stu_id == id1 : 
            menter1 = search_name(i.stu_menter)
            name1 = i.stu_name
        elif i.stu_id == id2 :
            menter2 = search_name(i.stu_menter)
            name2 = i.stu_name
    # print(menter1,name1)
    # print(menter2,name2)
    return name1 == menter2 or menter1 == name2

print(checkMenter('66000000'))
print(isRelated('66000000','64000000'))
