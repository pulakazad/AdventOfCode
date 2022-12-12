def readingFile(txtName):

    with open(txtName) as f:
        lines = f.readlines()

        curCal = 0

        cals = []
        for each in lines:

            if (each == '\n'):
                cals += [curCal]
                curCal = 0
            else:
                curCal += int(each)

        cals.sort()
        MostMaxCal = cals[len(cals)-1]
        extraMaxCal = cals[len(cals)-2]
        maxCal = cals[len(cals)-3]

        total = MostMaxCal + extraMaxCal + maxCal
        print(total);

readingFile('input.txt')
