def readingFile(txtName):

    with open(txtName) as f:
        lines = f.readlines()

        points = 0

        cals = []
        for each in lines:
            letters = each.split(' ')

            if (letters[0] == 'A'):
                secondLetter = letters[1].strip()
                if (secondLetter == 'X'):
                    points += 0 + 3
                elif (secondLetter == 'Y'):
                    points += 3 + 1
                else:
                    points += 6 + 2
            elif (letters[0] == 'B'):
                secondLetter = letters[1].strip()
                if (secondLetter == 'X'):
                    points += 0 + 1
                elif (secondLetter == 'Y'):
                    points += 3 + 2
                else:
                    points += 6 + 3
            else:
                secondLetter = letters[1].strip()
                if (secondLetter == 'X'):
                    points += 0 + 2
                elif (secondLetter == 'Y'):
                    points += 3 + 3
                else:
                    points += 6 + 1

        print(points);

readingFile('input.txt')
