numbers = [int(e) for e in input()]
def count_minus(str) :
    return len([e for e in str if e<0])
print(count_minus(numbers))