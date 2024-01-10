def add_score(subject_score, student, subject, score):
    subject_score[student] = {subject : score}
    return subject_score
def calc_average_score():
    dct = {}
    for key,val in subject_score.items() :
        dct[key] = '{:,.2f}'.format(sum(val.values()) / len(val))
    return dct
subject_score = { '66010660' : {'math' : 10,'engl' : 20,'scie' : 30, 'thai' : 40,'comp':50},
                  '66010670' : {'math' : 15,'engl' : 25,'scie' : 35, 'thai' : 45,'comp':55}  }
print(calc_average_score())