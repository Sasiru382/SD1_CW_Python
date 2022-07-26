# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1899317
# Date: 15/04/2022
#---------------------------------------------------------------------------------------------------------------------

def credit_value(massage0,massage1="Out of range",massage2="Integer required"): # Function for input validation
     while True:
          try:
              value = int(input("Please enter your credits at "+ massage0 +" : "))
              if (value <= 120 and value % 20 == 0):
                   break
              else:
                   print(massage1)
                   continue
          except ValueError:
              print(massage2)
              continue
     return value
def main(p,t,r,e,version_control):
    while True:
        credit_pass  = credit_value("Pass")
        credit_defer = credit_value("defer")
        credit_fail  = credit_value("fail")
        total= credit_pass + credit_defer + credit_fail
        if (total == 120):
                if (credit_pass == 120):                                                                             
                      outcome="Progress"
                      p+=1
                elif (credit_pass == 100):                              
                      outcome="Progress (module trailer)"
                      t+=1
                elif (credit_fail >= 80):                              
                      outcome="Exclude"
                      e+=1
                else:                              
                      outcome="Do not progress – module retriever"
                      r+=1
                print(outcome)                
                if ( version_control =='1'):
                        break
                while True:
                        print("\nWould you like to enter another set of data ? ")
                        choice = input("Enter 'y' for yes or 'q' to quit and view results : ")
                        if(choice.lower() == 'y'):
                                main(p,t,r,e,version_control)
                        elif(choice.lower() == 'q'):
                                print('-'*65,'\n',"\tHorizontal Histogram\n")
                                print(" Progress ",p,":","*" * p,'\n',
                                      "Trailer  ",t,":","*" * t,'\n',
                                      "Exclude  ",e,":","*" * e,'\n',
                                      "Retriever",r,":","*" * r)
                                print('\n',p+t+r+e," outcomes in total.\n")
                                print('-'*65)
                        else:
                                print("Please Enter y or q")
                                continue
                        break           
        else: 
                print("Total incorrect")
                continue
        break
while True:    
    print("\tWellcome to Programme\n")
    print("Enter 1 for Student Version. \nEnter 2 for Staff Version.\nEnter q to exit.\n")
    version_control=input("Enter version number: ")
    if version_control=='1' or version_control=='2':
                main(0,0,0,0,version_control)           # pass argument to p,t,r,e as 0      
    elif version_control=='q':
                break
    else:
                print("Enter Version number 1 or 2")
