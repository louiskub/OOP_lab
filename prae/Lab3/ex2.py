def add_score(subject_score, student, subject, score) :
    if student not in subject_score : 
        subject_score[student] = {}
    subject_score[student][subject] = score
    return subject_score

def calc_average_score(subject_score) :
    average_dict = {}
    for student, subject in subject_score.items() :
        average_dict[student] = f"{sum(subject.values()) / len(subject):.2f}"
    return average_dict

subject_score = {'65010001' : {'python' : 50}}
student = '65010001'
subject = 'cal'
score = 60
print(add_score(subject_score, student, subject, score))
print(calc_average_score(subject_score))