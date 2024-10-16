
# b = input("Valoarea lui b ")
# h = input("Valoarea lui h ")
#
# result = 0.5 * int(b) * int(h)
#
# print("aria triunghiului este =", result)
#

# parola_corecta = 7710
# numar_utilizator = input("Introduceți un număr: ")
# ghicit_corect = (int(numar_utilizator) == parola_corecta)
# print("Ați ghicit parola:", ghicit_corect)

# print("*".center(7, " "))
# print("***".center(7," "))
#
# x = int(5)
# print(x.__pow__(2))

# print ("Tell me anything ...")
# anything = input()
# print ("Hmmm...", anything, "... Really?")
#
# anything = input("Zi-mi orice ....")
# print("Hmmm...", anything, "pe bune?")

# anything = float(input("Introdu un numar: "))
# something = anything ** 2.0
# print(anything, "la puterea a2a este: ", something)


# leg_a = float(input("Introdu Cateta 1: "))
# leg_b = float(input("Introdu Cateta 2: "))
# ipo = (leg_a**2 + leg_b**2) ** .5
# print ("Ipotenuza este: ", ipo)

# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print ("Thank you!")
# print("\nYour name is "+fnam +" "+lnam + ".")

# print("+" + 10 * "-" + "+")
# print(("|" + " "*10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

# leg_a = float(input("Input first leg lenght: "))
# leg_b = float(input("Input second leg lenght: "))
# print("Hypotenuse lenght is " + str((leg_a**2 + leg_b**2) ** .5))

#
# x=int(input("Input test value: "))
# print("The result is: ", 1/(x+1/(x+1/(x+(1/x)))))

hours=int(input("Hours: "))
minutes=int(input("Minutes: "))
duration=int(input("Duration: "))

total_minutes = minutes + duration
new_minutes = total_minutes % 60
extra_hours = total_minutes // 60
new_hours = (hours + extra_hours) % 24

print(new_hours, ":", new_minutes)