'''
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''

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

    counter = 0
    result = 0

    while counter < 3:
        result += max(resultArray)
        resultArray.remove(max(resultArray))
        counter += 1



    print(result)