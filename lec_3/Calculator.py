Exit = "no"
Operations = ["+", "-", "*", "/", "%"]
def Addition(Operand1, Operand2) :
    return Operand1 + Operand2
def Subtraction(Operand1, Operand2) :
    return Operand1 - Operand2
def Multiplication(Operand1, Operand2) :
    return Operand1 * Operand2
def Division(Operand1, Operand2) :
    return Operand1 / Operand2
def Modulus(Operand1, Operand2) :
    return Operand1 % Operand2

while Exit != "yes":
    Operand1 = 0
    Operand2 = 0
    Operation = "None"
    Result = 0
    Operand1 = float(input("Operand 1 : "))
    Operand2 = float(input("Operand 2 : "))
    while Operation not in Operations :
        Operation = input("Operation (+, -, *, /, %) : ")
    if Operation == "+" :
        Result = Addition(Operand1, Operand2)
    if Operation == "-" :
        Result = Subtraction(Operand1, Operand2)
    if Operation == "*" :
        Result = Multiplication(Operand1, Operand2)
    if Operation == "/" :
        Result = Division(Operand1, Operand2)
    if Operation == "%" :   
        Result = Modulus(Operand1, Operand2)  
    print(f"Result = {Result}")         
    Exit = input("Exit ?(yes/no) : ")
