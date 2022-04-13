import numpy as np
import random as rand


def occurInArr(array, value, counting):
    for i in array:
        if i == value:
            counting -= 1
            if counting == 0:
                return True
    return False


def countingSameWord(array, value):
    count = 0
    for i in array:
        if i == value:
            count += 1
    return count


def swapRandom(array):
    first = rand.randint(0, len(array)-1)
    second = rand.randint(0, len(array)-1)
    array[first], array[second] = array[second], array[first]


crossChance = 0.45
mutationChance = 0.05
generationSize = 400

f = open("DNA.TXT", "r")
data = np.array(f.read().split())

lenOfWord = len(data[0])
maxRank = len(data) - 1
generationX = []
nextGen = []

for i in range(generationSize):
    rand.shuffle(data)
    generationX.append(data.copy())
del data

bestRank = maxRank * 10 + 1
bestChain = []
endAll = False
for i in range(100):
    identityMark = []
    for i in generationX:
        sumOfGen = 0
        for j in range(len(i) - 1):
            for k in range(1, lenOfWord + 1):
                if i[j][k:] == i[j + 1][:lenOfWord - k]:
                    sumOfGen += k
                    break
        identityMark.append(sumOfGen)
        if sumOfGen < bestRank:
            bestChain = i
            bestRank = sumOfGen
        if bestRank == maxRank:
            endAll = True
            break
    if endAll:
        break

    for x in range(generationSize):
        parent1 = rand.randint(0, generationSize - 1)
        parent2 = rand.randint(0, generationSize - 1)
        while parent1 == parent2:
            parent2 = rand.randint(0, generationSize - 1)

        child = [None] * (maxRank + 1)
        if rand.random() < crossChance:
            segmentIndex = rand.randint(0, maxRank - 1)
            segmentLength = rand.randint(1, maxRank - segmentIndex)
            for i in range(segmentIndex, segmentIndex + segmentLength - 1):
                child[i] = generationX[parent1][i]
            j = 0
            for i in generationX[parent2]:
                if j == segmentIndex:
                    j = segmentIndex + segmentLength - 1
                if not occurInArr(child, i, countingSameWord(generationX[parent2], i)):
                    child[j] = i
                    j += 1
        else:
            child = generationX[parent1].copy()

        for i in child:
            if rand.random() < mutationChance:
                swapRandom(child)

        nextGen.append(np.array(child).copy())

    generationX = nextGen
    nextGen = []

print("Our best rank:", bestRank)
print("Worst posibility:", maxRank*10)
print("Best posibility:", maxRank)

DNA = bestChain[0]
for i in range(len(bestChain)-1):
    for j in range(1, len(bestChain[0])):
        if bestChain[i][j:] == bestChain[i+1][:len(bestChain[0])-j]:
            DNA += bestChain[i+1][len(bestChain[0])-j:]
print("Our best chain:", DNA)
print("Length of chain:", len(DNA))
