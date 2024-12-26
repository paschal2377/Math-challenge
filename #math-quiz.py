#math-quiz
# Importing necessary libraries
import random
import time  # to measure the time taken to complete the challenge
Operators = ["+","-","*","/"]
# Defining the range for numbers in the problems
Min_number = 10
Max_number = 80
Total_problems = 10 #total questions to ask

def generate_problem(): # Function to generate a random math problem
    left = random.randint(Min_number,Max_number)
    right = random.randint(Min_number,Max_number)
    operator = random.choice(Operators) #randomly choosing the operator

    expr = str(left)+""+operator+""+str(right) # Creating a string representation of the math expression
    answer = eval(expr) #Evaluating the expression

    return expr,answer
#counting wrong and correct answers
wrong_count = 0
correct_count = 0
input("Press enter to start your challenge!")
print("-------------------")
start_time = time.time() #recording the starting time

for i in range(Total_problems):
     # Generating a new math problem
    expr,answer = generate_problem()
    while True:
        
        guess = input("Question#"+str(i+1)+":"+expr+"=")
        if guess == str(answer):
            correct_count += 1
            break # Breaking out of the loop to move to the next question

        else:
            wrong_count += 1
        
            break # Breaking out of the loop as the answer was wrong
    
end_time = time.time()  #Recording the end time 
Total_time = end_time-start_time #calculating the duration
percent = (correct_count/Total_problems) * 100 #calculating correct answers in percentage

print("-----------------------")
print("Well done! You have done it in",Total_time,"seconds!")
print("You got",correct_count,"correct answers in total")
print("You achieved",percent,"% ","out of 100%")
