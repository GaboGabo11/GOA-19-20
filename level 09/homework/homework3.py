# convert the values into numbers

wins = int(input("enter your wins:"))
ties = int(input("enter your ties"))



#1 win = 3 point
#1 tie = 1 point
#calculate the score

win1 = wins + 3



score = win1 + ties

message = "your Score is " + str(score)

print(message)