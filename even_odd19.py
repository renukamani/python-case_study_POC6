for i in range(100) :
    i = i+1
    if i == 50 :
        break
    elif i in [10,20,30,40,50] :
        continue
    elif i % 2== 0 :
        print(i)

i = 1
while i <= 100 :
    if i == 90 :
        break
    elif i in [60,70,80,90] :
        i += 1
        continue
    elif i % 2 == 0 :
        print(i)
    i += 1
