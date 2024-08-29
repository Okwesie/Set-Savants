'''
This is a program that allows the user to enter a logical expression and computes the dual of the expression,
converts the expressio using set notation or converts the expression into a boolean expression.

-----------------------<Group Members>------------------------------------
1. Caleb Okwesie Arthur
2. Frances Seyram Fiahagbe
3. Ernest Smart


------------User code Syntax---------------------------------------------

>> "^" represents a conjunction
>> "V" represents a disjunction
>> "-" represents negation
>> "T" represents True
>> "F" represents False

------------Output Code Syntax------------------------------------------

>> "∧" represents a conjunction
>> "∨" represents a disjunction
>> "T" represents True
>> "F" represents False
>> "∩ " represents intersection
>> "U" represents the universal set
>> "∪" represents union
>> " ' " represents complement in set theory and in boolean
>> "+" represents or in boolean
>> " . " represents and in boolean

'''

#Welcome Message
print("Hello, we are the Set Savants and welcome to our program! :)")
print("What would you like to do?")
allowed_list = ['p','q','r','s','o','(',')','V','^',' ','-','T','F', 'P', 'Q', 'R', 'S', 'O']
#Asking user what they would like to do
option = input("Enter\n1. 'dual' to compute the dual\n2. 'set' to compute the set,\n3. 'boolean' to compute the boolean or\n4. 'end' to end the program\n>>>")


#Function to convert a logical expression into a boolean expression    
def convert_to_boolean_expression(expression):
    # Replace the symbols with corresponding variables
    expression = expression.replace("o", "m")
    expression = expression.replace("p", "x")
    expression = expression.replace("q", "y")
    #expression = expression.replace("-", "'")
    expression = expression.replace("r", "z")
    expression = expression.replace("s", "w")
    
    
    # Replace ^ with ⋅ and V with +
    expression = expression.replace("^", "⋅")
    expression = expression.replace("v", "+")
    expression = expression.replace("t", "1")
    expression = expression.replace("f", "0")
    
    final_expression = convert_negative(expression)
    return final_expression

#Function to convert logical expression to its dual
def convert_to_dual(expression):
    
    #Replacing all symbols with their duals
    expression = expression.replace("^", "∨")
    expression = expression.replace("v", "∧")
    expression = expression.replace("t", "F")
    expression = expression.replace("f", "T")
    
    return expression

#Function to convert logical expression to set theory
def convert_to_set(expression):
 
    expression = expression.replace("p", "A")
    expression = expression.replace("q", "B")
    expression = expression.replace("r", "C")
    expression = expression.replace("s", "D")
    expression = expression.replace("o", "E")
    
    # Replace ^ with ∩  and V with ∪
    expression = expression.replace("^", "∩")
    expression = expression.replace("v", "∪")
    expression = expression.replace("t", "U")
    expression = expression.replace("f", "∅")
    
    final_expression = convert_negative(expression)
    return final_expression
    
def convert_negative(expression):    
    expression_list = []
    for i in expression:
        expression_list.append(i)
    
    
    #Finding all occurences of '-'
    indexOfcompliment = []
    for i in range(len(expression)):
        if expression[i] == '-':
            indexOfcompliment.append(i)
   
    
    #Replacing all '-' with " ' "
    num3 = len(indexOfcompliment)
    for i in range(num3):
        expression_list[indexOfcompliment[i]] = expression_list[indexOfcompliment[i] + 1]
        expression_list[indexOfcompliment[i]+ 1] = "'"
        
    return ''.join(expression_list)
  

while True:
    
    #If the user wants to find the dual
    if option == 'dual':
        logicalExpression = input("\nKindly enter a logical expression, enter 'V' for a disjunction, '^' for conjunction and '-' for negation, 'T' for True and 'F' for false\n Use the variables p, q, r, s or o \n>>>")
        
        #Ensuring correct input
        for i in logicalExpression:
            if i not in allowed_list:
                print("<<<input error>>> \n<<enter a logical expression with 'V' for a disjunction,>>\n<<'^' for conjunction and '-' for negation>>\n<<Use the variables p, q, r, s or o>>")
                break
        else:
            print(convert_to_dual(logicalExpression.lower()))
            option = input("\nWould you like to continue our program? \nEnter\n1. 'dual' to compute the dual\n2. 'set' to compute the set,\n3. 'boolean' to compute the boolean or\n4. 'end' to end the program\n>>>")


    #If the user wants to find the set expression
    elif option == 'set':
        logicalExpression = input("\nKindly enter a logical expression, enter 'V' for a disjunction, '^' for conjunction and '-' for negation, 'T' for True and 'F' for false\n Use the variables p, q, r, s or o \n>>>")
        
        #Ensuring correct input
        for i in logicalExpression:
            if i not in allowed_list:
                print("<<<input error>>> \n<<enter a logical expression with 'V' for a disjunction,>>\n<<'^' for conjunction and '-' for negation>>\n<<Use the variables p, q, r, s or o>>")
                break
        else:
            print(convert_to_set(logicalExpression.lower()))
            option = input("\nWould you like to continue our program? \nEnter\n1. 'dual' to compute the dual\n2. 'set' to compute the set,\n3. 'boolean' to compute the boolean or\n4. 'end' to end the program\n>>>")
            

    #If the user wants to find the boolean    
    elif option == "boolean":
        logicalExpression = input("\nKindly enter a logical expression, enter 'V' for a disjunction, '^' for conjunction and '-' for negation, 'T' for True and 'F' for false\n Use the variables p, q, r, s or o \n>>>")
        
        
        #Ensuring correct input
        for i in logicalExpression:
            if i not in allowed_list:
                print("<<<input error>>> \n<<enter a logical expression with 'V' for a disjunction,>>\n<<'^' for conjunction and '-' for negation>>\n<<Use the variables p, q, r, s or o>>")
                break
        else:
            print(convert_to_boolean_expression(logicalExpression.lower()))
            option = input("\nWould you like to continue our program? \nEnter\n1. 'dual' to compute the dual\n2. 'set' to compute the set,\n3. 'boolean' to compute the boolean or\n4. 'end' to end the program\n>>>")

    # If the user wants to end the program   
    elif option == "end":
        #To end the program
        print("Thank you for using our program")
        exit()
        
        
    else:
        #Dealing with exceptions
        print("<<input error>> \nEnter 'dual' to compute the dual,\n 'set' to compute the set,\n 'boolean' to compute the boolean or\n 'end' to end the program")
        break
