import re

Exit = "no"
valid_pattern = r'^[\d+\-*/(). ]+$' 

while Exit != "yes":
    Expression = input("Enter expression: ")
    
    if not re.match(valid_pattern, Expression):
        print("Error: Invalid characters in expression")
    else:
        try:
            Result = eval(Expression)
            print(f"Result = {Result}")
        except Exception as e:
            print(f"Error: {e}")
    
    Exit = input("Exit ?(yes/no): ")
