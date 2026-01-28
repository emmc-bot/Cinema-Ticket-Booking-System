def readFile():
    file = open("D:\\python3\\finaltest\\movies.txt", "r")
    for line in file:
        line = line.replace("\n", "")
        mList = line.split("|")
        mCode = mList[0].strip()
        mTitle = mList[1].strip()
        mStatus = mList[2].strip()
        movieD[mCode] = [mTitle, mStatus] 

    file = open("D:\\python3\\finaltest\\studios.txt", "r")
    for line in file:
        line = line.replace("\n", "")
        line = line.replace("\t", "")
        sList = line.split("|")
        sCode = sList[0].strip()
        sName = sList[1].strip()
        sRows = sList[2].strip()
        sCols = sList[3].strip()
        sStatus = sList[4].strip()
        studioD[sCode] = [sName, sRows, sCols, sStatus]

def generateSeats():
    for mCode in playD:
        daylist = playD[mCode]
        for shiftList in daylist:
            pTIme = shiftList[0]
            sCode = shiftList[1]
            sRows = int(studioD[sCode][1])
            sCols = int(studioD[sCode][2])
            key = mCode + "-" + pTIme
            tempList = [[0 for c in range(sCols)] for r in range(sRows)]
            seatD[key] = tempList

def movieInfo():
    for mCode in movieD:
        mTitle = movieD[mCode][0]
        mStatus = movieD[mCode][1]

        if mStatus == "A":
            if mCode in playD:
                print(mTitle, ":", mCode)
                dayList = playD[mCode]
                for shiftList in dayList:
                    pTime = shiftList[0]
                    sCode = shiftList[1]
                    sName = studioD[sCode][0]
                    sRows = int(studioD[sCode][1])
                    sCols = int(studioD[sCode][2])
                    print(pTime, sName, "(", sRows, "x", sCols, ")")
        
def chooseMovie():
    while True:
        mCode = input("Enter movie code: ").upper()
        if mCode in movieD:
            mStatus = movieD[mCode][1]
            if mStatus == "A":
                mTitle = movieD[mCode][0]
                print("Movie Title: ", mTitle)
                return mCode
            else:
                print("Invalid Status")
        else:
            print("Invalid movie code")

def chooseTime(mCode):
    dayList = playD[mCode]
    timeList = list()
    for shiftList in dayList:
        pTime = shiftList[0]
        timeList.append(pTime)
    print(timeList)

    while True:
        pTime = input("Choose playing time: ")
        if pTime in timeList:
          return pTime
        else:
            print("Invalid time")

def getStudio(mCode, pTime):
    dayList = playD[mCode]
    for shiftList in dayList:
        if pTime == shiftList[0]:
            return shiftList[1]

def inputSeat(sRows, sCols):
    while True:
        seat = input("Enter seat: ").upper()
        if len(seat) < 2 or len(seat) > 3:
            print("Seat Unavailable")
        else:
            letter = seat[0:1]
            number = seat[1:]
            r = ord(letter) - 65
            c = int(number) - 1
            if r < 0 or r > int(sRows):
                print("Seat Unavailable")
            elif c < 0 or c > int(sCols):
                print("Seat Unavailable")
            else:
                return r, c, seat

def printLayout(sRows, sCols, seatList):
    print("\nSEATS LAYOUT")
    for i in range(1, int(sCols)+ 1):
        print(f"{i:3}", end=" ")
    print()
    for r in range(int(sRows)):
        print(chr(65+r), end=" ")
        for c in range(int(sCols)):
            seat = seatList[r][c]
            if seat == 0:
                print("[ ]", end=" ")
            else:
                print("[x]", end=" ")
        print()

def createReciept(mCode, pTime, sCode, soldList):
    price = 50000
    mTitle = movieD[mCode][0]
    print("RECIEPT:\n")
    print(mTitle)
    print("TIME: {}".format(pTime))
    print("STUDIO: {}".format(sCode))
    print("TICKETS: {}".format(soldList))
    print("QUANTITY: {}".format(len(soldList)))
    print("PRICE: Rp. {}".format(price))
    print("TOTAL PRICE: RP. {}".format(price*len(soldList)))
    print("Thank you!!")


def buyTickets():
    mCode = chooseMovie()
    pTime = chooseTime(mCode)
    sCode = getStudio(mCode, pTime)
    sRows = studioD[sCode][1]
    sCols = studioD[sCode][2]
    key = mCode + "-" + pTime
    seatList = seatD[key]
    printLayout(sRows, sCols, seatList)

    soldList = []
    while True:
        r, c, seat = inputSeat(sRows, sCols)
        if seatList[r][c] == 0:
            seatList[r][c] = 1
            soldList.append(seat)           
        else:
            print("SEAT IS TAKEN")
        again = input("Do you want to order another seat (y/n) ?")
        if again == "n":
            createReciept(mCode, pTime, sCode, soldList)
            break

    

playD = {
    'TLT': [['13.30', 'S1'], ['15.00', 'S4'], ['19.30', 'MX']],
    'TMR': [['15.30', 'S4'], ['21.00', 'S1'], ['23.30', 'S1']],
    'TGM': [['18.30', 'S5'], ['22.00', 'S3'], ['22.30', 'MX']],
    'LSP': [['13.35', 'S6'], ['18.20', 'S6']]
}

movieD = dict()
studioD = dict()
seatD = dict()

readFile()
generateSeats()
while True:
    movieInfo()
    buyTickets()
    break