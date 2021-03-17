# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID - IIT: 2018434
# Student ID - UOW: w1761916

# Date:  28.11.2019

test1=[120,0,0]
test2=[100,20,0]
test3=[100,0,20]
test4=[80,20,0]
test5=[60,40,20]
test6=[40,40,40]
test7=[20,40,60]
test8=[20,20,80]
test9=[20,0,100]
test10=[0,0,120]

def progress():
    print("Progression Outcome = Progress ")
    print()
    
def trailing():
    print("Progression Outcome = Progress – module trailer  ")
    print()
    
def retreiver():
    print("Progression Outcome = Do not Progress – module retriever ")
    print()
    
def excluded():
    print("Progression Outcome = Exclude ")
    print()

test=["Pass","Defer","Fail"]
print(test)
print()

if test1[0]==120 and test1[1]==0 and test1[2]==0:
    print(test1)
    progress()
    
if test2[0]==100 and test2[1]==20 and test2[2]==0:
    print(test2)
    trailing()
    
if test3[0]==100 and test3[1]==0 and test3[2]==20:
    print(test3)
    trailing()
    
if test4[0]==80 and test4[1]==20 and test4[2]==0:
    print(test4)
    retreiver()
    
if test5[0]==60 and test5[1]==40 and test5[2]==20:
    print(test5)
    retreiver()
    
if test6[0]==40 and test6[1]==40 and test6[2]==40:
    print(test6)
    retreiver()
    
if test7[0]==20 and test7[1]==40 and test7[2]==60:
    print(test7)
    retreiver()
    
if test8[0]==20 and test8[1]==20 and test8[2]==80:
    print(test8)
    progress()
    
if test9[0]==20 and test9[1]==0 and test9[2]==100:
    print(test9)
    excluded()
    
if test10[0]==0 and test10[1]==0 and test10[2]==120:
    print(test10)
    excluded()

