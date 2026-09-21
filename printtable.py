tableData = [['apples', 'oranges', 'cherries', 'banana'], 
['Alice', 'Bob', 'Carol', 'David'], 
['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i], key=len))
    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            data = tableData[i][j]
            print(data.rjust(colWidths[i]), end = " ")
        print()

printTable()