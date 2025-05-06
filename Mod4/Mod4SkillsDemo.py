'''
Before you start recording your video:

Write a program that takes a student's grade (e.g. 91) and uses an
if-elif-else statement to tell them the grade point average they'd
receive in this class. Use the grading table in the Syllabus to
complete this problem.

When you've finished creating your program, start recording:

Explain your code at a high-level, scrolling through all the code,
if it isn't visible on the screen all at once. (No need to read
through every word.)
Test at least 3 branches of your if-elif-else statement to demonstrate
it's functioning as expected.
As you test your code, explain why the if-elif-else statement is
functioning the way it is, as if you were explaining it to a student
who was learning about this for the first time. This will require you
to trace through the code (line by line) as you explain it.
'''

grade = int(input("Please enter your grade: "))

if grade>=96 and grade<=100:
    print("Congradulations you got an A! 4.0")
elif grade>=93 and grade<=95:
    print("You got a A- 3.7")   
elif grade>=90 and grade<=92:
    print("You got a B+ 3.3")   
elif grade>=87 and grade<=89:
    print("You got a B 3.0")    
elif grade>=83 and grade<=86:
    print("You got a B- 2.7")   
elif grade>=80 and grade<=82:
    print("You got a C+ 2.3")   
elif grade>=77 and grade<=79:
    print("You got a C 2.0")    
elif grade>=73 and grade<=76:
    print("You got a C-, but hey you passed. 1.7")  
elif grade>=70 and grade<=72:
    print("You got a D+, sad days. 1.3") 
elif grade>=67 and grade<=69:
    print("You got a D, sad days. 1.0") 
elif grade>=63 and grade<=66:
    print("You got a D-, sad days. 0.7") 
elif grade<=62:
    print("You got a F, what happened? 0.3")
