n = int(input())
count = x = 0
if( 0 <= n < 10):
    for i in range (4):
        count += n*(10**i) + x
        x = count - n*2
    print(count)
else:
    print("Error")
    
'''if 0 <= n < 10 :
    print(n*4 + n*30 + n*200 + n*1000)
else :
    print("Error")'''