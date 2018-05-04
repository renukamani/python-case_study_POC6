word = raw_input("enter the word")
word = word.lower()
count = 0
for i in word :
    if i == "e" :
        count = count + 1
if count == 2 :
    print("true")
else :
    print("false")
