
'''
This is a calculator script, that takes input in a form of a normal equation with operators such as - + / * ( ) and ** and provides a result of such equation.
In this script, to execute calculations, Infix Notatation is converted to a Postfix Notation. From Postfix Notations calculations are performed.
Example equation: ((1+2)**2-3*4/(-1+2))
'''

##################################################################################################################
### Function that chekcs whether a user wants to calculate another equation

def wanna_calculate():
    
    xyz=''
    
    while xyz.lower() not in ['y','n']:
        
        if xyz.lower() not in ['y','n']:
            xyz=input('Do you want to calculate another equation? Y or N: ')

        if xyz.lower() not in ['y','n']:
            print('Wrong input.')
        else:
            if xyz.lower()=='y':
                return True
            else:
                return False

##################################################################################################################
### Geting an input from a user in form of a standard infix equation and formating it to form a infix equation list (each operator and each number is a separate element on a list)

def equation_input_and_format():

    input_check = True

    while input_check:

        input_check = False
        equation = input('Please provide an equation to be calculated: ')
        eq_form = []

        # Sorting the equation to form a list with numbers and operators
        for num in range(0, len(equation)):

            #Checking if a number is float or not and appending to sorted list eq_form
            if equation[num].isnumeric() or equation[num] == '.':
                if eq_form != [] and (eq_form[-1].isnumeric() or '.' in eq_form[-1]):
                    eq_form[-1] = eq_form[-1] + equation[num]
                elif len(eq_form) == 1 and eq_form[0] == ('-' or '+'):
                    eq_form[-1] = eq_form[-1] + equation[num]
                elif len(eq_form) >= 3 and eq_form[-1] == ('-' or '+') and eq_form[-2] == '(':
                    eq_form[-1] = eq_form[-1] + equation[num]
                else:
                    eq_form.append(equation[num])

            #Appending Mathematical Operators to an eq_form list
            elif equation[num] in ['+' , '-' , '*' , '/' , ')', '(']:
                if equation[num] == '*' and eq_form[-1] == '*':
                    eq_form[-1] = eq_form[-1] + equation[num]
                else:
                    eq_form.append(equation[num])

            #Deleting spaces
            elif equation[num] == ' ':
                    pass

            #Any other input is not supported by the script
            else:
                print(f'Wrong input. {equation[num]} is not a valid input.')
                input_check = True
                break

    return eq_form

##################################################################################################################
### Function that returns precedence value for math operators such as + - / ** *

def precedence(name):
    if name == '+':
        return 2
        
    elif name == '-':
        return 2
        
    elif name == '/':
        return 3
        
    elif name == '*':
        return 3
        
    elif name == '**':
        return 4

##################################################################################################################
### Function converting infix to postfix notation, both in list-form (each operator and each number is a separate element on a list)

def post_fix_notation(eq_if):
    
    #Start values
    eq_pf = []
    op_stack = []
    
    #Going through all objects in infix equation list
    for num in eq_if:
        
        #Checking if object is numeric '1' or '1.1' etc., and appending it to post fix equation list
        if any(map(str.isdigit, num)):
            eq_pf.append(num)
        
        #Checking the object is one of the oprators and appending it to a operator stack respecting precedence
        elif num in ['+' , '-' , '*' , '/' , '**']:
            
            if op_stack == [] or op_stack[-1] == '(' or precedence(op_stack[-1]) < precedence(num):
                op_stack.append(num)
                
            elif precedence(op_stack[-1]) >= precedence(num):
                
                while op_stack != [] and op_stack[-1] != '(' and precedence(op_stack[-1]) >= precedence(num):
                    eq_pf.append(op_stack.pop())
                    
                else:
                    op_stack.append(num)
        
        #Checking if the object is left parenthesis and appending to a list
        elif num == '(':
            
            op_stack.append(num)
            
        #Checking if the object is right parenthesis, poping operators from operator stack as long as matching left parenthesis is found    
        elif num == ')':
            
            while op_stack[-1] != '(':
                eq_pf.append(op_stack.pop())
            
            else:
                op_stack.pop()
            
    #Poping all remaining operators from operator stack and appending to the postfix equation list
    while op_stack != []:
        eq_pf.append(op_stack.pop())
        
    return eq_pf

##################################################################################################################
### Function that takes in string math operator and string number and calculates a value of an equation
        
def execute(name, num1, num2):
    if name == '+':
        return num1 + num2
        
    elif name == '-':
        return num1 - num2
        
    elif name == '/':
        return num1 / num2
        
    elif name == '*':
        return num1 * num2
        
    elif name == '**':
        return num1 ** num2

##################################################################################################################
### Function Calculating Post Fix Equations that are provided in a form of a list with each operator and ich number as a seperate object

def post_fix_equation_calculation(eq_pf):

    while len(eq_pf) > 1:
        
        #Getting first operator on the list
        cur_op = next(i for i in eq_pf if i in ['+' , '-' , '*' , '/' , '**'])
        cur_op_index = next(eq_pf.index(i) for i in eq_pf if i in ['+' , '-' , '*' , '/' , '**'])
        
        #Executing calculations implied by current operator on two antecedent numbers
        new_number = execute(cur_op, float(eq_pf[cur_op_index - 2]), float(eq_pf[cur_op_index - 1]))
        
        #Adjusting eq_pf list with executed calculations
        eq_pf[cur_op_index] = new_number
        eq_pf.pop(cur_op_index - 1)
        eq_pf.pop(cur_op_index - 2)
        
    return eq_pf[0]


############################################################################################ MAIN SCRIPT
############################################################################################ MAIN SCRIPT
############################################################################################ MAIN SCRIPT

calculate = True

while calculate:
    
    try:
        eq_if = equation_input_and_format()
        eq_pf = post_fix_notation(eq_if)
        result = post_fix_equation_calculation(eq_pf)
        print(f'The result is: {result}')
        
    except ZeroDivisionError:
        print("Sorry, can't divide by 0.")

    except :
        print("Sorry, there is something wrong with the equation that you entered, please correct it and input again.")
    
    calculate = wanna_calculate()
        
print('Thanks, see ya!')

