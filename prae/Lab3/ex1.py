def add_score(subject_score, subject, score) :
  subject_score[subject] = score
  return subject_score

def calc_average_score(subject_score) : 
  return f"{sum(subject_score.values()) / len(subject_score):.2f}" 
    
subject_score = {'python' : 50}
subject = 'cal'
score = 60
print(add_score(subject_score, subject, score))
print(calc_average_score(subject_score))