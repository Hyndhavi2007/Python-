# String -> Int
age_str = "25"
age_int = int(age_str)
print(age_int + 5)

# String -> float
price_str = "99.99"
price = float(price_str)
print(price * 2)

# int/float -> str
score = 95.98
label = "Your Score: " + str(score)
print(label)

# int -> bool
print(bool(0))
print(bool(5))
print(bool(-1))

# str -> bool
print(bool(""))
print(bool("hi"))
# DANGER - these will crash:
# int("hello")     ← ValueError
# int("3.14")      ← ValueError (use float first, then int)
print(int(float("3.14")))

