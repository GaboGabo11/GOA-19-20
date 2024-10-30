# asks the user to enter the savings
savings = int(input("Enter your savings:"))

# convert the user input into a float value adn update the variable
savings = float(savings)

#savings grow after 1 year at a 5% annual interest rate
balance = savings * 1.5 

#Convert the balance into  string and update the varible

balance = str(balance)

#concatente the 2 strings to produce a massage
message = "amount in 1 year:" + balance

print(message)