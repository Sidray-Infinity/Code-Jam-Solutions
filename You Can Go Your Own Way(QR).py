def findpath():
    cases = int(input())
    for i in range(cases):
        throw = input() # The matrix size is not required in this approach
        path = list(input())
        other = ""
        for j in range(len(path)):
            if(path[j] == "E"):
                other += "S"
            else:
                other += "E"
        print('CASE #{}: {}'.format(i+1, other))

findpath()
