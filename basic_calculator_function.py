def basic_calculator(a,b,operation):

  if (a.isnumeric() & b.isnumeric()):
    a=float(a)
    b=float(b)
    if operation == "add":
      result = a + b
    elif operation == "subtract":
      result = a - b
    elif operation == "divide":
      result = a / b
    elif operation == "multiply":
      result = a * b
    else:
      result = "Operations supported: add, subtract, divide, multiple only"
    
  else:
    result = "Please enter a valid number for a & b"
    

  return result