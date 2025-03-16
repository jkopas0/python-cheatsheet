
# Example 1
age = 18

if age >= 18:
	print("You are old enough to have a driver's licence.")
else:
	print("You are not yet old enough to have a driver's licence.")

# Example 2
playtimeHours = 460

if playtimeHours > 0 and playtimeHours <= 50:
	print("Average playtime.")
elif playtimeHours > 50 and playtimeHours <= 500:
	print("You might want to stop soon.")
elif playtimeHours > 500:
	print("You need a break.")
else:
	print("How did you get negative playtime?")

# Example 3
x = 10
y = 5

if x > 0 or y < 0:
	print(True)
else:
	print(False)

# Example 4
var1 = 0
var2 = 0

if var1 == var2: pass # The `==` condition is met when var1 and var2 match.
if var1 != var2: pass # The `!` operator inverts the condition. (In this case the condition will be met if var1 and var2 do *not* match.)
if var1 > var2: pass # The `>` condition is met when var1 is more than var2.
if var1 >= var2: pass # The `>=` condition is met when var1 is more than or equal to var2.
if var1 < var2: pass # The `<` condition is met when var1 is less than var2.
if var1 <= var2: pass # The `<=` condition is met when var1 is less than or equal to var2.