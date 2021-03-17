# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID - IIT: 2018434
# Student ID - UOW: w1761916

# Date:  28.11.2019

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

def trailer():
    print("Progression Outcome = Progress – module trailer ")

def retriever():
    print("Progression Outcome = Do not Progress – module retriever  ")

def excluded():
    print("Progression Outcome = Exclude ")


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
