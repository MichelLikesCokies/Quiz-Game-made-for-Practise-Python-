#Importing needed modules
import keyboard #Imported for Pausing syntax for testing purpose
import os #Imported for clearing above outputs by os.system('cls')
import random #Imported for ramdomizing question list

intro = True

while intro:
 #Introducing The Project
 print("""  
 ===========================================
 =       Welcome To This Fun Quiz Game!    =          
 =                                         =                      
 =         Options: Type Start or Exit to  =                  
 =                 continue the game       =
 =                                         =
 ===========================================
 """)

 intro_a = input("What you want to do? (Not Case Sensative) \n") #Asking the user whether they want to quit the quiz or start
 intro_a = str(intro_a.upper()) #Converting it to uppercase to make it non-case sensitive
 if intro_a=="START":
     intro = False
 elif intro_a=="EXIT":
     exit()
 else:
     print(" ") #This is for making a gap 
     print("Error: Please type start or exit")
     input('Press <ENTER> to continue')
     os.system('cls')
     continue

intro = False
os.system('cls')

# </Introduction> XD
# Creating Class for questions

class QA:
   def __init__(self, question, options, correct_answer, hint):  #Just for defining what questions, options and hint are
        self.question = question
        self.options = options #THIS MUST BE UPPER-CASE
        self.correct_answer = correct_answer
        self.hint = hint
        
   def ask(self):
      answered1= True
      while answered1:
        print(self.question)
        print(" ") #This is for making a gap 
        print("Options: " + self.options) 
        print("""
Type 'Hint' for hint
        """)  
        
        
        temp = input("Your Answer: ")
        answer1 = str(temp.upper()) #Converting it to uppercase for non-case sensitive
        if answer1==self.correct_answer:
            print("""
            
            Correct! Let's move to next one!
            
            """)
           
            input('Press <ENTER> to continue')
            os.system('cls')
            answered1 = False
        elif answer1=="HINT":
             print("""
""" +
self.hint  
             )
             input("Press ENTER to continue")
             os.system('cls')
             continue
        else:
            print("""

            Wrong! Please try again.
            
            """)
            input("Press [ENTER] to Continue")
            os.system('cls')
            continue
            
        
#Making objects 
#Class Varibles = (question, options, correct_answer, hint)

#REMEMBER: Correct Answers should be capital letters

#Questions
q1 = QA("What two words are used in machine for testing or training?", "A: Testing Now B: My Messege C: Hello World", "HELLO WORLD", "No hint for this sry")
q2 = QA("Python is_______ language", "A: Server B: Database C: Programming", "PROGRAMMING", "Error Loding Hint: Just kidding... No hint idea yet :(")
q3 = QA("AI stands for_________", "A: Art Introduction B: Articial Intelligence C: All Important", "Articial Intelligence", "google it")
q4 = QA("Which is the safest country?", "A: India B: America C: Holland", "HOLLAND", "its in the name of 2020 SPIDER MAN cast/actor")

#Exucting Ask Function 

ask = [             # Putting in a list to ramdomize them
    q1.ask,         
    q2.ask,         # NOTE: It will not be ramdomized if there is () however we put it when exucting in a for loop
    q3.ask,         # Suppose l is the element of loop in ask list. We'll have l() in it.
    q4.ask
    ]
    
random.shuffle(ask) #Finally ramdomizing it

for a in ask:
    a()             # As you can see we have () here in a 
    
Finished = True


while Finished:
    print("""
Congratulations! You've beaten every questions!
""")
    input("Press [Enter] to Continue.")
    Finished = False    
    
