def fy(test):
    wo = ""
    for i in range(len(test)):
        print(i)
        if  i % 2 == 0:
            wo = wo + test[i].lower()
        else:
            wo = wo + test[i].upper()
    return wo
   

print(fy("wowDoingGreat"))