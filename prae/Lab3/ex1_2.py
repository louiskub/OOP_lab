def calc_average_score(subject_score):
    subject_score_list = subject_score.split()
    average = (sum(int(i) for i in subject_score_list[1::2]) + score) / (len(subject_score_list)//2 + 1)
    average = f"{average:.2f}"
    return str(average)
    
def add_score(subject_score, subject, score) :
    subject_score_list = subject_score.split()
    subject_score = dict(zip(subject_score_list[0::2], map(int, subject_score_list[1::2])))
    subject_score[subject] = score
    return subject_score   
    
subject_score_str = input()
subject = str(input())
score = int(input())
subject_score_list = subject_score_str.split()
print(add_score(subject_score_list, subject, score))
print(calc_average_score(subject_score_list))

'''# Taking input for key-value pairs as tuples
input_data_str = input("Enter key-value pairs : ") #(e.g., 'python 50 calculus 60')
input_data_list = input_data_str.split()

# Example usage of dict() with a list of tuples
input_data = [('python', 50), ('calculus', 60)]
subject_score = dict(input_data)
print(subject_score)'''