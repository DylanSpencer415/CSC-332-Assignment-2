import time
import random
from tkinter import *
from functools import partial

def main():
    window = Tk()
    window.title("Merge Sort")

    Label(window, text="Unsorted Array").grid(row=1, pady=(12,0), sticky=W)
    Label(window, text="Sorted Array").grid(row=1, column=1, pady=(12,0), sticky=W)
    
    listbox1 = Listbox(window, width=20)
    scrollbar1 = Scrollbar(window, orient=VERTICAL)
    listbox1.config(yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=listbox1.yview)
    listbox1.grid(row=2, sticky=W)
    scrollbar1.grid(row=2, sticky=E+NS)

    listbox2 = Listbox(window, width=22)
    scrollbar2 = Scrollbar(window, orient=VERTICAL)
    listbox2.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=listbox2.yview)
    listbox2.grid(row=2, column=1)
    scrollbar2.grid(row=2, column=1, sticky=E+NS)

    Label(window, text="Enter array number (1-9):").grid(row=0)
    entry = Entry(window)
    entry.grid(row=0, column=1)
    Button(window, text="Retrieve and Sort", command=partial(display, entry, listbox1, listbox2)).grid(row=0, column=2)
    
    window.mainloop()

def display(entry, listbox1, listbox2):
    try:
        size = int(Entry.get(entry))
        entry.delete(0, END)
        
        listbox1.delete(0, END)
        listbox2.delete(0, END)
        
        if size in range(1,10):
            array = generateNumbers(-10000, 10000, 1000 * size)
            for x in array:
                listbox1.insert(END, x)
                
            #sortedArray, time = mergeSort(array)
            #generateResults(sortedArray, time)
        else:
            listbox1.insert(END, "Invalid input")
            listbox2.insert(END, "Invalid input")
    except:
        entry.delete(0, END)
        
        listbox1.delete(0, END)
        listbox2.delete(0, END)
        listbox1.insert(END, "Invalid input")
        listbox2.insert(END, "Invalid input")

def generateNumbers(rangeMin, rangeMax, size):
    array = random.sample(range(rangeMin, rangeMax), size)
    return array

##  Rob already did this I just have to add it in, so don't do this
#def mergeSort(array):

##  Creates the output spreadsheet
##  Needs to check if spreadsheet is already generated because this will be used more than once
##  If not yet generated, generate the file and column headers and call addResult
##  If already generated, call addResult
#def generateResults(sortedArray, time):

##  Add result to existing spreadsheet
##  First call calculateResults to get values for all 4 columns
##  Use test data for now
#def addResults(sortedArray, time):

##  Returns 4 values for each column in spreadsheet
##  Use test data for now
#def calculateResults(sortedArray, time):
    
if __name__ == "__main__":
    main()
