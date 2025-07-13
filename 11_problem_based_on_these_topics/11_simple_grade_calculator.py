'''
Problem: The Simple Grade Calculator
Imagine you're a junior data analyst, and your task is to help your school automate a very basic grade calculation process for a single student.

Your Goal: Write a Python program that:
    Greets the user and asks for the student's name.
    Asks how many subjects the student has taken.

    Then, for each subject, it should:
        Prompt the user to enter the grade (a number) for that subject.
        Add this grade to a running total.

    After collecting all grades, it should calculate the average score.
    Finally, based on the average score, it should determine and print the student's final status:
        If the average is 90 or above: Print "[Student Name], you achieved an A! Excellent work!"
        If the average is between 70 and 89 (inclusive): Print "[Student Name], you achieved a B. Good job!"
        If the average is between 50 and 69 (inclusive): Print "[Student Name], you achieved a C. Keep working hard!"
        If the average is below 50: Print "[Student Name], unfortunately, you did not pass. You need to re-attempt."

    Make sure to print the student's name, total number of subjects, and their calculated average score before the final status message.
    Add comments to your code to explain different sections.
'''

# Actionable steps
'''
1. We will greet the user using Print funciton
2. We will ask user his/her name using input function
3. We will ask them about number of subjects using int input function and using subject_counter to store the value.
4. We will ask about each subject's name using for loop and use current_subject
5. We will ask about the grades he/she has got in each subject using for loop and use current_grade
6. We will display total grades from total_grade_sum
7. We will display average grade
8. We will display where he/she stands.

'''
print('\nHello Buddy! Welcome to this Simple Grade Calculator which will tell you about your average grades and also your final status')
name = input("\nBefore we continue, Can you please tell your name: ")
print('\nThanks for telling me your name,',name)
subject_counter = int(input("\nCan you tell me the total number of subjects: "))
current_subject = 0
total_grade_sum = 0
current_grade = 0


for current_subject in range(1,subject_counter+1):
    match(current_subject):
        case 1:
            subject1 = input("\nWhat is the name of first subject: ")
            grade1 = int(input("Enter your grade: "))
            current_subject += 1
        case 2:
            subject2 = input("\nWhat is the name of second subject: ")
            grade2 = int(input("Enter your grade: "))
            current_subject += 2
        case 3:
            subject3 = input("\nWhat is the name of third subject: ")
            grade3 = int(input("Enter your grade: "))
            current_subject += 3
        case 4:
            subject4 = input("\nWhat is the name of fourth subject: ")
            grade4 = int(input("Enter your grade: "))
            current_subject += 4
        case 5:
            subject5 = input("\nWhat is the name of fifth subject: ")
            grade5 = int(input("Enter your grade: "))
            current_subject += 5
        case 6:
            subject6 = input("\nWhat is the name of sixth subject: ")
            grade6 = int(input("Enter your grade: "))
            current_subject += 6

    

for current_grade in range(1,subject_counter+1):
    match(current_grade):
        case 1:
            total_grade_sum += grade1
        case 2:
            total_grade_sum += grade2
        case 3:
            total_grade_sum += grade3
        case 4:
            total_grade_sum += grade4
        case 5:
            total_grade_sum += grade5
        case 6:
            total_grade_sum += grade6

avg_grade = total_grade_sum/subject_counter
print('\nYour total sum of grades is: ',total_grade_sum)
print('\nAverage Grade: ',avg_grade)
if(avg_grade<50):
    print("\nUnfortunately, You did not pass, You need to re-attempt")
elif(69>avg_grade>= 50):
    print("\nYou achieved a \"C\", keep working hard!")
elif(89>avg_grade>=70):
    print("\nYou achieved a \"B\", Good Job!")
elif(avg_grade<90):
    print("\nHoorey! You have got an \"A\", that's wonderful!")