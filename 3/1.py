def add_score(subject_score, subject, score):
    subject_score[subject] = score
def calc_average_score():
    return '{:,.2f}'.format(sum(subject_score.values()) / len(subject_score))

subject_score = {'math' : 10,'engl' : 20,'scie' : 30,
                 'thai' : 40,'comp':50}
print(calc_average_score())
print(sum(subject_score.values()) , len(subject_score))