num1 = 0
num2 = 0
i = ""
val = 0

def add(n1, n2):
    value = n1 + n2
    return value
def sub(n1,n2):
    value = n1 - n2
    return value
def mul(n1, n2):
    value = n1 * n2
    return value 
def div(n1, n2):
    value = n1 / n2
    return value 
def exp(n1, n2):
    z = n2
    n2 = int(n2)
    for n in range(n2):
        n1 = n1 * z
    value = n1
    return value
def ck(value):
    if (value % 1) == 0:
        value = int(value)
    return value
def out(sumType, answer):
    print("Function: ", sumType)
    print("Answer: ", answer)

print("CALCULATOR LOADING")
print("~~~~~~~~~~~~~~~~~~")
print("If you would like to quit at any point enter (q)")
print("")

while True:
    print("________")
    print("What function would you like to perform? ")
    print("Add (a) | Sub (s) | Mul (m) | Divide (d) | Exponent (e)")
    i = input(": ")
    if i == "q":
        quit()
    
    print("Enter the first number")
    num1 = input(": ")
    print("Enter the second number / exponent")
    num2 = input(": ")

    if i == "a":
        val = add(float(num1), float(num2))
        var = ck(val)
        out("Addition", var)
    elif i == "s":
        val = sub(float(num1), float(num2))
        var = ck(val)
        out("Subtraction", var)
    elif i =="m":
        val = mul(float(num1), float(num2))
        var = ck(val)        
        out("Multiplication", var)
    elif i == "d":
        val = div(float(num1), float(num2))
        var = ck(val)        
        out("Division", var)
    elif i == "e":
        val = exp(float(num1), float(num2))
        var = ck(val)        
        out("Exponent", var)
