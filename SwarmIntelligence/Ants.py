import random

verticesСount = begin = end = currentVertex = int
edgesList = {}
probabilitiesList = {}

#  пишем путь
def printEdges():
    for edge in edgesList:
        print(edge, ' ', edgesList[edge][0], ' ', edgesList[edge][1], sep='')
    print()

# читаем граф
def Graph(fileName):
    global verticesСount, begin, end, currentVertex, probabilitiesList
    file = open(fileName, 'r')
    info = file.readline().split()
    verticesСount = int(info[0])
    begin = int(info[1])
    currentVertex = int(begin)
    end = int(info[2])
    for line in file:
        edge = line.split('-')
        edgesList[str(edge[0]) + '-' + str(int(edge[1]))] = [random.randint(1, 10), 1]
    file.close()

    printEdges()

Graph('input.txt')
# чем больше муравьев и итераций то в последних итерациях муравьи намного чаще будут брать короткий путь
print('Введите количество муравьев: ', end='')
antsCount = int(input())
print('Введите количество итераций: ', end='')
iters = int(input())
# Счетчик муравьев выбравшие тот или иной путь
AntsTake1245 = 0
AntsTake135 = 0
length1245 = "неизвестно"
length135 = "неизвестно"
for iter in range(iters):
    print('Итерация (', iter + 1, '/', iters, '):', sep='')
    for ant in range(antsCount):  # для каждого муравья
        currentVertex = begin
        path = str(currentVertex)
        pathLen = 0
        visitedVertices = [currentVertex]
        while currentVertex != end:
            denominator = 0
            for edge in edgesList:
                if (int(edge.split('-')[0]) == currentVertex) and not (int(edge.split('-')[1]) in visitedVertices):
                    denominator += edgesList[edge][1] / edgesList[edge][0]
                    probabilitiesList[int(edge.split('-')[1])] = 100 * (edgesList[edge][1] / edgesList[edge][0])
            if probabilitiesList.__len__() == 0:
                print('Путь', path, 'завел в тупик.')
                exit(0)

            probability = random.randint(1, 100)  # вероятность
            nextVertex = False  # следующая вершина
            summ = 0
            for i in probabilitiesList:
                probabilitiesList[int(i)] = probabilitiesList[int(i)] / denominator
                summ += probabilitiesList[int(i)]
                if not nextVertex:
                    if probability <= summ:
                        pathLen += edgesList[str(currentVertex) + '-' + str(i)][0]
                        path += '-' + str(i)
                        currentVertex = i
                        visitedVertices.append(i)
                        nextVertex = True
                        break

            probabilitiesList.clear()
        if path == "1-2-4-5":
            AntsTake1245 = AntsTake1245 + 1
            length1245 = str(pathLen)
        else:
            AntsTake135 = AntsTake135 + 1
            length135 = str(pathLen)
        # показать каждого муравья
        # print('\tМуровей (', ant + 1, '/', antsCount, '):   ', path, ' ', pathLen, sep='')
        dT = 3 / pathLen
        for edge in edgesList:
            if (edgesList[edge][1] * 0.95) > 1:
                edgesList[edge][1] = edgesList[edge][1] * 0.95
            if path.find(edge) >= 0:
                edgesList[edge][1] += dT
    print("Длина пути 1-2-4-5: " + str(length1245))
    print("Длина пути 1-3-5: " + str(length135))
    print("Кол-во муравьев которые пошли по пути 1-2-4-5: " + str(AntsTake1245))
    print("Кол-во муравьев которые пошли по пути 1-3-5: " + str(AntsTake135))
    AntsTake1245 = 0
    AntsTake135 = 0
    printEdges()


