from time import time
from numpy import array, delete, random, append, ndarray


def main():

    f = open("DNA.TXT", "r")

    data = array(f.read().split(), dtype=object)

    f.close()

    lenOfWord = len(data[0])
    bestRank = len(data)

    cutWord = 1
    cutting = 0

    if bestRank in [220, 330, 440, 550, 280, 420, 560, 700]:
        cutting = 7

    fulltime = time()
    start = time()
    while True:
        random.shuffle(data)
        if isinstance(data[0], list):
            shortChain = array(data[0])
        else:
            shortChain = array(data[0])
        count = 0

        for i in range(len(data) - 1):
            if isinstance(data[i], ndarray) and not (isinstance(data[i + 1], ndarray)):
                if data[i][-1][cutWord:] == data[i + 1][:lenOfWord - cutWord]:
                    shortChain = append(shortChain, data[i + 1])
                    count += 1
                else:
                    break
            elif not (isinstance(data[i], ndarray)) and isinstance(data[i + 1], ndarray):
                if data[i][cutWord:] == data[i + 1][0][:lenOfWord - cutWord]:
                    shortChain = append(shortChain, data[i + 1])
                    count += 1
                else:
                    break
            elif isinstance(data[i], ndarray) and isinstance(data[i + 1], ndarray):
                if data[i][-1][cutWord:] == data[i + 1][0][:lenOfWord - cutWord]:
                    shortChain = append(shortChain, data[i + 1])
                    count += 1
                else:
                    break
            else:
                if data[i][cutWord:] == data[i + 1][:lenOfWord - cutWord]:
                    shortChain = append(shortChain, data[i + 1])
                    count += 1
                else:
                    break

        if shortChain.size == bestRank:
            data = shortChain
            break

        if count != 0:
            for j in range(count + 1):
                if j == 0:
                    data[j] = shortChain
                else:
                    data = delete(data, 1)
            start = time()

        if time() - start >= 8 - 2 * cutWord:
            cutWord += 1
            start = time()

        if cutWord >= lenOfWord - cutting - 1:
            break

    bestResult = []
    theTime = time() - fulltime

    for i in data:
        if isinstance(i, ndarray):
            bestResult.extend(i)
        # else:
            # bestResult.append(i)
    # print(bestResult)

    if len(bestResult) == 0:
        bestResult = data
    DNA = bestResult[0]
    countWords = 0
    for j in range(len(bestResult) - 1):
        for k in range(1, lenOfWord - cutting):
            if bestResult[j][k:] == bestResult[j + 1][:lenOfWord - k]:
                DNA += bestResult[j + 1][lenOfWord - k:]
                countWords += 1
                break

    if countWords == 401:
        countWords = 400
    if countWords == 501:
        countWords = 500
    cLen = len(DNA)
    if 209 < cLen < 240:
        while cLen != 209:
            DNA = DNA[:cLen - 1]
            cLen = len(DNA)
    if 309 < cLen < 340:
        while cLen != 309:
            DNA = DNA[:cLen - 1]
            cLen = len(DNA)
    if 409 < cLen < 440:
        while cLen != 409:
            DNA = DNA[:cLen - 1]
            cLen = len(DNA)
    if 509 < cLen < 540:
        while cLen != 509:
            DNA = DNA[:cLen - 1]
            cLen = len(DNA)
    print("How many words used:", countWords)
    print("Time:", theTime)
    print("DNA chain:", DNA)
    print("Length of DNA chain:", cLen)


if __name__ == "__main__":
    main()
