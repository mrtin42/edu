def result(mf):
    if mf < 16:
        return "Pass"
    else: return "Fail"

print(f"Your result is {result(int(input('How many minor faults did you make in test? ')))}")§