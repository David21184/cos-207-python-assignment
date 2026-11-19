Scores = [85, 90, 78, 92, 88] # list of int
Course = "WSU-COS 207"         #str
mean = sum(Scores) / len(Scores)  # float
passed = mean >= 80               # bool
for value in (Scores, Course, mean, passed):
    print(f"{type(value).__name__:6} {value}")
    print(f"{Course}: n={len(Scores)}, mean = {mean:.2f}")