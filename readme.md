# Devops Challenge 1
This project contains the script for converting the CSV files (`titanic.py`) as well as the flask server file (`web.py`).

## Conversion File
This file contains all the functions needed to convert and output two CSV files. The functions are as follows:

`openAndParse` - This function is responsible for reading in the CSV file into a data structure we can work with.

`rearrangeList` - This rearranges a CSV file based on the list of headers passed into it. Any arrangement of headers can be passed in to produce a valid CSV file as output.

`reverseList` - This function takes in the list of headers and reverses the order of the headers and outputs it as a list. This list can then be used by `rearrangeList`.

`everOther` - Similar to `reverseList`, this function takes in the headers and outputs a list of every other header.

`writeFile` - This function handles the writing of the file.

Right now, these functions need to be called individually in order to get the expected output. Typical calls could look like:

```python
rawDat = openAndParse('train.csv')

revList = reverseList(rawDat[0])

reversedCols = rearrangeList(rawDat,revList)

writeFile(reversedCols,'output/reversed.csv')
```

## Flask Server
The Titanic page can be reached by navigating to [domain]/titanicmenu.

There are two radio buttons, and pressing the Get CSV button will download the CSV of the file currently selected.