import sys
input = sys.stdin.readline

testcase = int(input())

def squared_distance(x, y):
    return (x[0]-y[0]) ** 2 + (x[1]-y[1]) ** 2

for _ in range(testcase):
    ans = 0
    coordinates = list(map(int, input().split()))
    start, end = coordinates[0:2], coordinates[2:]
    planet_count = int(input())
    planets = [list(map(int, input().split())) for _ in range(planet_count)]

    for planet in planets:
        center, radius_squared = planet[0:2], planet[2:]

        start_in = squared_distance(start, center) < radius_squared
        end_in = squared_distance(end, center) < radius_squared

        if start_in != end_in:
            ans += 1

    print(ans)