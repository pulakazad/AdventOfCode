def readingFile(txtName):

    with open(txtName) as f:
        lines = f.readlines()
        total = 0
        OuterLetterList = []
        print(lines)
        for i in range(0, len(lines)-2, 3):
            firstSack = lines[i].strip()
            secondSack = lines[i+1].strip()
            thirdSack = lines[i+2].strip()
            print('firstSack: ' + firstSack)
            print('secondSack: ' + secondSack)
            print('thirdSack: ' + thirdSack)
            letterList = []
            for letter in firstSack:
                if (letter in secondSack):
                    if (letter in thirdSack) and (letter not in letterList):
                        print(letter)

                        letterList.append(letter)
            OuterLetterList.append(letterList)

    print(OuterLetterList)
    total = countPriority(OuterLetterList)

    print(total)

def countPriority(OuterLetterList):
    total = 0;
    for eachList in OuterLetterList:
        for each in eachList:
            if ((ord(each) -96) < 0):
                total += ord(each)-38
                print('Capital: ' + each + ' ' + 'Value: ' + str(ord(each)-38))
            else:
                total += ord(each)-96
                print('lowercase: ' + each + ' ' + 'Value: ' + str(ord(each)-96))
    return total

readingFile('input.txt')
