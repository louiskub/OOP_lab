def count_minus(str) :
    count = [i for i in str if i < 0]
    return len(count)

str = [int(i) for i in input().split()]
print(count_minus(str))

'''for i in range (len(str)) :
        if str[i] < 0 :
            count += 1'''