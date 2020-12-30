# program which tries to in a simple fashion, model disease spread
# 12/23/2020
# not sure how to go about updating this plot as disease spreads

import random
import matplotlib.pyplot as plt
import time


random.seed(1)                  # locks the randomness for reproducibility while Im still working on it
limit = 30                      # number of rows and columns(keep under 50 for quicker speed)
numbSick = 5                    # number of those who are sick
numbImmune = 1               # 900 is roughly the number that can be immune
percentageImmunity = numbImmune/(limit**2.0)
i = 0
dt = 1
time = 10
counter = 0

infectedCol = []                            # experimenting
infectedRow = []


rows, cols = (limit,limit)
arr = [[0 for rows in range(limit)] for cols in range(limit)]




print(arr)

while i<numbSick:                                # randomly plots sick(red) people
    sickCol = 0
    sickRow = 0

    sickCol = random.randint(0,limit-1)
    sickRow = random.randint(0,limit-1)

    if (sickCol,sickRow) in arr:
        pass
    else:
        if arr[sickCol][sickRow] != 1 and arr[sickCol][sickRow] != 2:
            arr[sickCol][sickRow] = 1
            print(sickCol, sickRow)

            i += 1

while i<numbImmune:                                # randomly plots immune/vaccinated(blue) people
    immuneCol = 0
    immuneRow = 0

    immuneCol = random.randint(0,limit-1)
    immuneRow = random.randint(0,limit-1)

    if arr[immuneCol][immuneRow] ==1:              # if a dot is sick, it remains sick
        pass
    else:
        if (immuneCol, immuneRow) not in arr:
            arr[immuneCol][immuneRow] = 2
        else:
            if arr[immuneCol][immuneRow] != 2:
                arr[immuneCol][immuneRow] = 2
                # print(immuneCol,immuneRow)
    i += 1
for dt in range(time):
    plt.pause(0.05)
    for j in range(limit):                          # these for loops are meant to plot the graph
        for k in range(limit):

            if arr[j][k] == 0:
                plt.scatter(j,k,color=['white'])
            elif arr[j][k] == 1:
                plt.scatter(j,k,color=['red'])
            elif arr[j][k] == 2:
                plt.scatter(j,k,color=['blue'])
    plt.draw()

    infectedRow = []
    infectedCol = []
    for l in range(limit-1):                          # these for loops are meant find the infected ones in the array
        for m in range(limit-1):
            if arr[l][m] == 1:
                infectedRow.append(l)
                infectedCol.append(m)

    for h in range(len(infectedRow)):




        b = -1
        a = -1
        while b <= 1:                            # loop which spreads infection except those that are vaccinated (blue)
            a = -1

            while a <= 1:

                if b == 0 and a == 0:
                    a += 1
                if arr[infectedRow[h] + b][infectedCol[h] + a] == 2:
                    pass
                else:
                    arr[infectedRow[h] + b][infectedCol[h] + a] = 1

                a += 1
            b += 1

    print(infectedRow)
    print(infectedCol)







print("Ratio of immune to total number:",percentageImmunity)


