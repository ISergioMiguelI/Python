import re

print("Our magical calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    equation = input("Enter equation:")
    if equation == 'quit':
        global run
        global previous
        equation =""
        if previous == 0:
            print("Goodbye, human.")
        else:
            equation  = input(str(previous))
            
        if equation == 'quit':
            print("Goodbye, human.")    
            
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        
        if previous == 0:
            previous = eval(equation)
            
        else:
            previous = eval(str(previous) + equation)
        
        print("Result" , previous)
    
    
while run:
    performMath()
    