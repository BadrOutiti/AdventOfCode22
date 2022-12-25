import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    counter = -1
    resultArray = [0 for i in range(500)]
    f = open("Input", "r")
    inputString = f.read()
    arrayOfAllNumbers = inputString.split("\n\n")

    for array in arrayOfAllNumbers:
        counter = counter + 1
        resultArray[counter] = 0
        numbersInArray = array.split("\n")
        for number in numbersInArray:
            if resultArray[counter] == 0:
                resultArray[counter] = int(number)
            else:
                resultArray[counter] += int(number)


    result = max(resultArray)

    print(result)

