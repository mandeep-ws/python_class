with open("veg.txt","a+") as myfile:
    myfile.seek(0)
    myfile.write("Ghiya")
    myfile.write("\ntikka")
    myfile.seek(0)
    myfile.write("Ghiya")
    myfile.write("\ntikkai")
    print(myfile.read())

