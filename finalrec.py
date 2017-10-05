import random
import csv

import gui
myList = gui.gui()
#print myList

allUsers=[]
userMovies=[]
with open('ratings.csv', 'rb') as csvfile:
    something = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in something:
        temp = str(row[0].split(',')[0])
        if temp in myList:
            if row[0].split(',')[2] > 4:
                userMovies.append(str(row[0].split(',')[1]))

finalMovies=[]

with open('movies.csv', 'rb') as csvfile:
    something = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in something:
        temp = str(row[0].split(',')[0])
        if temp in userMovies:
            myMovie = row
            temp2 = str(myMovie[1:-1])
            finalMovies.append(temp2[2:-2])

for i in range(5):
    print random.choice(finalMovies)