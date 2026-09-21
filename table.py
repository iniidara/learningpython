tableData = [['apples', 'oranges', 'cherries', 'banana'], 
['Alice', 'Bob', 'Carol', 'David'], 
['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(colWidths)):
        colWidths[i] = len(max(tableData[i], key = len))
        for j in range(len(colWidths[0])):
            for i in 

printTable()