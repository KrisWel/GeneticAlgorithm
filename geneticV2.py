import random as rand
import time


f = open("DNA.TXT", "r")
data = f.read().split()
lenOfWord = len(data[0])
bestRank = len(data)
cutWord = 1

start = time.time()
while True:
    rand.shuffle(data)
    if isinstance(data[0], list):
        shortChain = data[0]
    else:
        shortChain = [data[0]]
    count = 0

    for i in range(len(data) - 1):
        if isinstance(data[i], list) and not(isinstance(data[i + 1], list)):
            if data[i][-1][cutWord:] == data[i + 1][:lenOfWord - cutWord]:
                shortChain.append(data[i + 1])
                count += 1
            else:
                break
        elif not(isinstance(data[i], list)) and isinstance(data[i + 1], list):
            if data[i][cutWord:] == data[i + 1][0][:lenOfWord - cutWord]:
                shortChain.extend(data[i + 1])
                count += 1
            else:
                break
        elif isinstance(data[i], list) and isinstance(data[i + 1], list):
            if data[i][-1][cutWord:] == data[i + 1][0][:lenOfWord - cutWord]:
                shortChain.extend(data[i + 1])
                count += 1
            else:
                break
        else:
            if data[i][cutWord:] == data[i + 1][:lenOfWord - cutWord]:
                shortChain.append(data[i + 1])
                count += 1
            else:
                break

    if len(shortChain) == bestRank:
        data = shortChain
        break

    if count != 0:
        for j in range(count + 1):
            if j == 0:
                data[j] = shortChain
            else:
                data.pop(1)
        start = time.time()

    # 360 - 80 * cutWord -> 10min | 40 - 8 * cutWord -> 1min
    if time.time() - start >= 40 - 8 * cutWord:
        cutWord += 1
        start = time.time()

    # Dla bledow pozytywnych - 7 (zeby ograniczyc ilosc niepotrzebnych slow)
    if cutWord >= lenOfWord - 7:
        break

bestResult = []
for i in data:
    if isinstance(i, list):
        bestResult.extend(i)
    else:
        bestResult.append(i)
# print(bestResult)

DNA = bestResult[0]
for j in range(len(bestResult) - 1):
    # Dla bledow pozytywnych - 7 (zeby ograniczyc ilosc niepotrzebnych slow)
    for k in range(1, lenOfWord - 7):
        if bestResult[j][k:] == bestResult[j + 1][:lenOfWord - k]:
            DNA += bestResult[j + 1][lenOfWord - k:]
            break
print("DNA chain:", DNA)
print("Length of DNA chain:", len(DNA))
# print("Best length to get:", 209)
