# Excercise 3.1.11 LAB 
## fixing repo 


income = float(input("Enter the annual income: "))  

if income < 85528:
    tax = income * 0.18 - 556.02
elif income > 85528 :
    tax = 14839.02 + ((income - 85528) * 0.32) 
    
tax = round(tax, 0)

print("Your tax is: ", tax, "thalers")        
    