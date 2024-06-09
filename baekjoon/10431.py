P = int(input())

for _ in range(P):
    data = list(map(int, input().split()))
    T = data[0]
    heights = data[1:]
    
    total_steps = 0
    sorted_students = []
    
    for height in heights:
        steps = 0

        for i in range(len(sorted_students)):
            if sorted_students[i] > height:
                sorted_students.insert(i, height)
                steps = len(sorted_students) - i - 1
                break
        else:
            sorted_students.append(height)
        
        total_steps += steps
    
    print(T, total_steps)