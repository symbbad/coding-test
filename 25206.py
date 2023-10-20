score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

total_value = 0
total_multiply = 0
for _ in range(20):
    title, value, score_alpa = input().split()
    value = float(value)
    if score_alpa != "P":
        total_value += value
        total_multiply += value* float(score[score_alpa])

result = round(total_multiply / total_value, 6)

print(result)

'''
conversion = format(grand_point_avg, '.6f')


'''