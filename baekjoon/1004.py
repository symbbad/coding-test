import sys
input = sys.stdin.readline

testcase = int(input())

def between(x, y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**(1/2)

for _ in range(testcase):
    ans = 0
    coordinates = list(map(int, input().split()))
    planet = int(input())
    planets = [list(map(int, input().split())) for _ in range(planet)]
    for i in range(len(planets)):
        if between(coordinates[0:2], planets[i][0:2]) > planets[i][2] and between(coordinates[2:], planets[i][0:2]) < planets[i][2]:
            ans += 1
        elif between(coordinates[0:2], planets[i][0:2]) < planets[i][2] and between(coordinates[2:], planets[i][0:2]) > planets[i][2]:
            ans += 1
    print(ans)