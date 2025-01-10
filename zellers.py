#User inputs a date, gets back the day of the week it landed on.

P = input("Enter the month of the date you want to know about, such as March: ")
B = input("Day: ")
D = input("Enter the century. For example, enter 19 for 1989: ")
C = input("Enter the year of the century. For example, enter 89 for 1989: ")

M = P.lower()

if M == "january":
    A = 11
elif M == "february":
    A = 12
elif M == "march":
    A = 1
elif M == "april":
    A = 2
elif M == "may":
    A = 3
elif M == "june":
    A = 4
elif M == "july":
    A = 5
elif M == "august":
    A = 6
elif M == "september":
    A = 7
elif M == "october":
    A = 8
elif M == "november":
    A = 9
elif M == "december":
    A = 10
else:
    print ("Error - you didn't follow directions when you entered your month. Please try again.")
    A = input("Enter the month of the date you want to know about, such as January: ")


if A == 11 or A == 12:
    C -= 1


W = (13 * A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2 * D
R = Z % 7


if R < 0:
    R += 7


if R == 0:
    print (str(P) + " " + str(B) + ", " + str(D) + str(C) + " was on a Sunday.")
elif R == 1:
    print (str(P) + " " + str(B) + ", " + str(D) + str(C) + " was on a Monday.")
elif R == 2:
    print (str(P) + " " + str(B) + ", " + str(D) + str(C) + " was on a Tuesday.")
elif R == 3:
    print (str(P) + " " + str(B) + ", " + str(D) + str(C) + " was on a Wednesday.")
elif R == 4:
    print (str(P) + " " + str(B) + ", " + str(D) + str(C) + " was on a Thursday.")
elif R == 5:
    print (str(P) + " " + str(B) + ", " + str(D) + str(C) + " was on a Friday.")
elif R == 6:
    print (str(P) + " " + str(B) + ", " + str(D) + str(C) + " was on a Saturday.")


