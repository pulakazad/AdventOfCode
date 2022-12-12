def readingFile(txtName):

    with open(txtName) as f:
        lines = f.readlines()
        count = 0;
        for each in lines:
            intervals = each.split(",")

            numList = intervals[0].split("-")
            firstPair = []
            for num in numList:
                first = int(num.strip())
                firstPair.append(first)

            numList = intervals[1].split("-")
            secondPair = []
            for num in numList:
                first = int(num.strip())
                secondPair.append(first)

            if ((firstPair[0] <= secondPair[0])
                and (firstPair[1] >= secondPair[1])):
                count+=1
            elif ((secondPair[0] <= firstPair[0])
                and (secondPair[1] >= firstPair[1])):
                count+=1
            elif ((firstPair[0] <= secondPair[0])
                and (secondPair[0] <= firstPair[1])):
                    count+=1
            elif ((secondPair[0] <= firstPair[0])
                and (firstPair[0] <= secondPair[1])):
                    count+=1

            print(firstPair)
            print(secondPair)
            print('-----')
        print(count)
            # print(intervals)


readingFile('input.txt')
