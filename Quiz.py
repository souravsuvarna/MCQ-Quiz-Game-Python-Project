print("---Welcome---")

score = 50

player = input("Enter your Name: ")

print("\nHello "+player+", Welcome to the Quiz Game")

print("\n\t----NOTE---\n->Total 5 Questions.\n->Each Question Carries 10 Points\n->You earn 10 points for CORRECT answer\n->10 points will be deducted for WRONG answers")

print("\n\t---Badges---\n->MASTER:- If Score = 50\n->CHAMPION:- If Score = 40 \n->Scholar:- Score = 30\n->Genius:- Score = 20  ")

print("\n\tALL THE BEST!!")
enter = int(input("\nPress 1 to start:"))

if enter==1:

    print("Lets Begin!!")

    print("\nQUESTION 1: Which is the capital of India?\nOptions:\n1.Bengaluru\t2.Kolkata\n3.Delhi\t\t4.Goa")

    choice = int(input("Enter your Choice(1/2/3/4):-"))
    
    if choice == 3:
        print("\nCorrect Answer!! You Earned 10 Points")
       
    else:
        score=score-10
        print("\nWrong, Delhi is the Capital of India")

else:
    quit()
        
##Ouestion 1 completed

enter = int(input("\nPress 1 to Next Question:-"))

if enter == 1:
    print("\nQUESTION 2: Which is the National Animal of India?\nOptions:\n1.Deer\t2.Tiger\n3.Cow\t4.Elelphant")
    
    choice = int(input("Enter your Choice(1/2/3/4):-"))
    
    if choice == 2:
        print("\nCorrect Answer!! You Earned 10 Points")
        
    else:
        score=score-10
        print("\nWrong, Tiger is the National animal of India")
else:
    print("\nQuestion Skipped")       
##Question 2 completed
        
enter = int(input("\nPress 1 to Next Question:-"))

if enter == 1:
    print("\nQUESTION 3: C is Object Oriented Programming Language.\nOptions:\n1.TRUE\t2.FALSE")
    
    choice = int(input("Enter your Choice(1/2/3/4):-"))
    
    if choice == 2:
        print("\nCorrect Answer!! You Earned 10 Points")
        
    else:
        score=score-10
        print("\nWrong , C is Not a OOP Language it's a Procedure Oriented Language")
else:
    print("\nQuestion Skipped")        
##Question 3 Completed
        
enter = int(input("\nPress 1 to Next Question:-"))

if enter == 1:
    print("\nQUESTION 4: Which of the following does not supports pointers?\nOptions:\n1.Java & C++\t2.C & Java\n3.C & Python\t4.Java & Python")
    
    choice = int(input("Enter your Choice(1/2/3/4):-"))
    
    if choice == 4:
        print("\nCorrect Answer!! You Earned 10 Points")
        
    else:
        score=score-10
        print("\nWrong , C & C++ supports pointer, Where as java and python does not")  
else:
    print("\nQuestion Skipped")        
##Question 4 Completed

enter = int(input("\nPress 1 to Next Question:-"))

if enter == 1:
    print("\nQUESTION 5: Which of the following is DML Command?\nOptions:\n1.Alter\t\t2.Delete\n3.Create\t4.Select")
    
    choice = int(input("Enter your Choice(1/2/3/4):-"))
    
    if choice == 2:
        print("\nCorrect Answer!! You Earned 10 Points")
        
    else:
        score=score-10
        print("\nWrong , Delete is DML Command") 
else:
    print("\nQuestion Skipped")
            
print("\nQuiz Completed")

## Result Declaration

print("\n\t---RESULT---")
print("\nYour Score =",score)
if score==50 :
    print("\nCongratulations "+player+" You Earned 'MASTER' Badge ")

elif score==40 :
    print("\nCongratulations "+player+" You Earned 'CHAMPION' Badge ")
    
elif score==30 :
    print("\nCongratulations "+player+" You Earned 'Scholor' Badge ")

elif score==20 :
    print("\nCongratulations "+player+" You Earned 'Genius' Badge ") 
    
else:
    print("\nSorry "+player+" You not earned any badge , Good Try!! ")
    
##End
