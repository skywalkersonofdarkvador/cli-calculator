while True:
    try:
        num1 = float(input("enter first number: "))
        op = input("Enter operator (+, -, *, **, /, //, %): ")
        num2 = float(input("enter second number: "))
        
        if op == "+":
            results = num1 + num2
        
        elif op == "-":
            results = num1 - num2
            
        elif op == "*":
            results = num1 * num2
            
        elif op == "**":
            results = num1 ** num2
        
        elif op == "/":
            if num2 == 0:
                print("Error: Can't divide by zero")
                continue
            else:
                results = num1 / num2
        
        elif op == "//":
            results = num1 // num2
            
        elif op == "%":
            if num2 == 0:
                print("Error: Can't divide by zero")
                continue
            results = num1 % num2
            
        else:
            raise ValueError("Invalid Operator")
        
        print(f"{num1} {op} {num2} = {results}")
        
    except ValueError as ve:
        print("Error:", ve)
        continue
    
    again = input("Do you have another calculation (yes/no)? ").lower()
    if again != "yes":
        print("Goodbye")
        break