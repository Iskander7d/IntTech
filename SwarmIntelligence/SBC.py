from random import random, randint

def readGraph():
    file = open('input.txt', 'r')
    brief = file.readline().split()
    verticesСount = int(brief[0])
    begin = int(brief[1])
    currentVertex = int(begin)
    end = int(brief[2])

    edgesDict = {}
    for line in file:
        edges = line.split('-')
        edgesDict[str(edges[0]) + '-' + str(int(edges[1]))] = randint(1, 10)

    file.close()

    return verticesСount, begin, end, edgesDict


vertices, begin, end, edgesDict = readGraph()
print (begin, end)
for key, value in edgesDict.items():
    print(key, value)


weight135 = edgesDict['1-3'] + edgesDict['3-5']
weight1245 = edgesDict['1-2'] + edgesDict['2-4'] + edgesDict['4-5']



paths = []
currentVertex = begin
bees = 500
iterations = 10

scouts = int(bees * 0.1)
inactive = bees - scouts
probMistake = 0.1


cnt1245 = 0
cnt135 = 0
for i in range(iterations):
    for scout in range(scouts):
        pathWeight = 0
        path = str(currentVertex)
        while currentVertex != end:
            possibleVW = {}
            for key in edgesDict.keys():
                if currentVertex == int(key.split('-')[0]):
                    possibleVertex = int(key.split('-')[1])
                    tmp = str(currentVertex) + '-' + str(possibleVertex)
                    possibleVW[tmp] = edgesDict[tmp]
            prob = random()
            if prob < probMistake: # made a mistake
                nextVertex = max(possibleVW, key=possibleVW.get)[2]
            else:
                nextVertex = min(possibleVW, key=possibleVW.get)[2]
                probMistake *= 0.95

            pathWeight += edgesDict[str(currentVertex) + '-' + str(nextVertex)]
            currentVertex = int(nextVertex)
            path += '-' + str(currentVertex)

        if '2' in path:
            cnt1245 += 1
        else:
            cnt135 += 1

        #не обязательно
        print('ant {0} choose path: {1}'.format(scout,  path))
        print('chosen path weight: ', pathWeight)
        currentVertex = begin
    scouts += int(bees * 0.1)

print('1-3-5 weight: ', weight135)
print('1-3-5 total: ', cnt135)

print('1-2-4-5 weight: ', weight1245)
print('1-2-4-5 total: ', cnt1245)








