def sent(user_input):
    if user_input[0].islower():
        x = user_input[0].upper()
        user_input = user_input.replace(user_input[0],x,1)
        if user_input.startswith(("How","Why","When","What")):
            user_input = "{}{}".format(user_input , "?")
        else:
            user_input = "{}{}".format(user_input ,".")
    else: 
        user_input = "{}{}".format(user_input ,".")

    
    return user_input 


result = []

while True:
    user_input = " "
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        result.append(sent(user_input))

print(" ".join(result))

    




    
    

    
        
    