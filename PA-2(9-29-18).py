import time
import random
import csv
import math
import os.path
from tkinter import *
from functools import partial

def main():
    window = Tk()
    window.title("Merge Sort")

    Label(window, text="Enter array number (1-9):").grid(row=0)
    
    entry = Entry(window)
    entry.grid(row=0, column=1)

    Button(window, text="Retrieve and Sort", command=partial(display, entry)).grid(row=0, column=2)
    
    window.mainloop()

def display(entry):
    try:
        size = int(Entry.get(entry))
        
        if size in range(1,10):
            array = generateNumbers(-10000,10000,1000 * size)
            #sortedArray, time = mergeSort(array)
            #generateResults(sortedArray, time, str(len(sortedArray)/1000)+'_MergeSort_Time.cvs')
            print("That is a valid number")
        else:
            print("That is not a valid number")
    except:
        print("That is not a valid number")

def generateNumbers(rangeMin, rangeMax, size):
    return random.sample(range(rangeMin, rangeMax), size)

##  Rob already did this I just have to add it in, so don't do this
#def mergeSort(array):

##  Creates the output spreadsheet
##  Needs to check if spreadsheet is already generated because this will be used more than once
##  If not yet generated, generate the file and column headers and call addResult
##  If already generated, call addResult
def generateResults(sortedArray, elapsedTime, fileName):
    #value 1
    n = len(sortedArray)
    #value 2
    nlogN = n * (math.log10(n))
    #value 3
    timeSpent = 0
    for i in range(len(elapsedTime)):
        timeSpent = timeSpent + elapsedTime[i]
    #value 4
    x = (nlogN / timeSpent)
    y = 0
    while (x >= 10):
        x = x/10
        y += 1
    x = int(x)

    #prepare strings 
    s1 = str(timeSpent) + ' ms'
    s2 = str(x) + '*10^' + str(y)

    #if file does not exist
    if(os.path.isfile(fileName) == False):
        ##create csv file and write data
        with open(fileName, mode='w') as csv_file:
            fieldnames = ['Input Size N', 'Value of N*logN', 'Time Spent', 'Value of (N*logN)/time']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'Input Size N': n, 'Value of N*logN': nlogN, 'Time Spent': s1, 'Value of (N*logN)/time': s2})
    #addResults(sortedArray, time)

##  Add result to existing spreadsheet
##  First call calculateResults to get values for all 4 columns
##  Use test data for now
#def addResults(sortedArray, time):

##  Returns 4 values for each column in spreadsheet
##  Use test data for now
#def calculateResults(sortedArray, time):

if __name__ == "__main__":
    main()
