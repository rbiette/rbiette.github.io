# Tracker new participant script
# Ryan Biette

import csv

UXtracker = []
clinicalTracker = []
newParticipant = []

print ("starting")

with open('ActiveStudyParticipants_Planning.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)


