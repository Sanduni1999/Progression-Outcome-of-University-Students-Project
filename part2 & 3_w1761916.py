# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID - IIT: 2018434
# Student ID - UOW: w1761916

# Date:  28.11.2019

staff_user=input("Do you want to check a progression outcome of a student?\n If yes, enter y\n If no, enter q\nEnter:")

progresses=0
trailing=0
retrieve=0
exclude=0

while staff_user=="y":

    while True:     #this loop will run because the condition is already true.
        while True:     #this loop will run because the condition is already true.
            while True:     #this loop will run because the condition is already true.
                pass_credits=input("Number of credits at Pass:")
                try:
                    pass_credits= int(pass_credits)
                    break   #from this, process will come out from the specific loop
                except ValueError:
                    print("Integers required")
                    continue    #from this, continue the loop
            if pass_credits%20!=0:
                print("Range Error")
                continue    #from this, continue the loop
            break   #from this, process will come out from the specific loop
    
        while True:
            while True:
                defer_credits=input("Number of credits at Defer:")
                try:
                    defer_credits=int(defer_credits)
                    break
                except ValueError:
                    print("Integers required")
                    continue
            if defer_credits%20!=0:
                print("Range Error")
                continue
            break
    
        while True:
            while True:
                fail_credits=input("Number of credits at Fail:")
                try:
                    fail_credits=int(fail_credits)
                    break
                except ValueError:
                    print("Integers required")
                    continue
            if fail_credits%20!=0:
                print("Range Error")
                continue
            break

        total_credits=[pass_credits,defer_credits,fail_credits]
        if sum(total_credits)!=120:
            print("Total Incorrect")
            continue
        break
    
    
    
    def progress():
        print("Progression Outcome = Progress ")
        global progresses
        progresses+=1

    def trailer():
        print("Progression Outcome = Progress – module trailer ")
        global trailing
        trailing+=1

    def retriever():
        print("Progression Outcome = Do not Progress – module retriever  ")
        global retrieve
        retrieve+=1

    def excluded():
        print("Progression Outcome = Exclude ")
        global exclude
        exclude+=1
        

    if pass_credits==120 and defer_credits==0 and fail_credits==0:
        progress()
    
    elif pass_credits==100 and defer_credits==20 or defer_credits==0 and fail_credits==0 or fail_credits==20:
        trailer()

    elif pass_credits==80 and defer_credits==40 and fail_credits==0:
        retriever()
    elif pass_credits==80 and defer_credits==20 and fail_credits==20:
        retriever()
    elif pass_credits==80 and defer_credits==0 and fail_credits==40:
        retriever()
    elif pass_credits==60 and defer_credits==60 and fail_credits==0:
        retriever()
    elif pass_credits==60 and defer_credits==40 and fail_credits==20:
        retriever()
    elif pass_credits==60 and defer_credits==20 and fail_credits==40:
        retriever()
    elif pass_credits==60 and defer_credits==0 and fail_credits==60:
        retriever()
    elif pass_credits==40 and defer_credits==80 and fail_credits==0:
        retriever()
    elif pass_credits==40 and defer_credits==60 and fail_credits==20:
        retriever()
    elif pass_credits==40 and defer_credits==40 and fail_credits==40:
        retriever()
    elif pass_credits==40 and defer_credits==20 and fail_credits==60:
        retriever()
    elif pass_credits==40 and defer_credits==0 and fail_credits==80:
        excluded()
    elif pass_credits==20 and defer_credits==100 and fail_credits==0:
        retriever()
    elif pass_credits==20 and defer_credits==80 and fail_credits==20:
        retriever()
    elif pass_credits==20 and defer_credits==60 and fail_credits==40:
        retriever()
    elif pass_credits==20 and defer_credits==40 and fail_credits==60:
        retriever()
    elif pass_credits==20 and defer_credits==20 and fail_credits==80:
        excluded()
    elif pass_credits==20 and defer_credits==0 and fail_credits==100:
        excluded()
    elif pass_credits==0 and defer_credits==120 and fail_credits==0:
        retriever()
    elif pass_credits==0 and defer_credits==100 and fail_credits==20:
        retriever()
    elif pass_credits==0 and defer_credits==80 and fail_credits==40:
        retriever()
    elif pass_credits==0 and defer_credits==60 and fail_credits==60:
        retriever()
    elif pass_credits==0 and defer_credits==40 and fail_credits==80:
        excluded()
    elif pass_credits==0 and defer_credits==100 and fail_credits==20:
        excluded()
    elif pass_credits==0 and defer_credits==0 and fail_credits==120:
        excluded()

    print()
    staff_user=input("Do you want to check a progression outcome of a student?\n If yes, enter y\n If no, enter q\n Enter:")
    
else:
    total=[progresses,trailing,retrieve,exclude]


#Horizontal Histogram
    print("Progress ",total[0],end="  ")
    for j in range(total[0]):
        print("*",end="")
    print()

    print("Trailing ",total[1],end="  ")
    for j in range(total[1]):
        print("*",end="")
    print()

    print("Retreiver",total[2],end="  ")
    for j in range(total[2]):
        print("*",end="")
    print()

    print("Excluded ",total[3],end="  ")
    for j in range(total[3]):
        print("*",end="")
    print()

    print()
    
    print(sum(total),"outcomes in total.")
    print()

#vertically histogram
    print("Progress",end=" ");print("Trailing",end=" ");print("Retreiver",end=" ");print("Excluded")
    
    for j in range(total[0]):
        print("   *")
        print(end="")
    print(end="             ")

    for j in range(total[1]):
        print("*")
        print(end="             ")
    print(end="        ")

    for j in range(total[2]):
        print("*")
        print(end="                     ")
    print(end="          ")

    for j in range(total[3]):
        print("*")
        print(end="                               ")
    
    
    
