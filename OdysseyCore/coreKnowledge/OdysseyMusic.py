notesVar1 = ['A0,', 'A#0', 'B0', 'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1', 'C2',
             'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2',
             'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
             'C4',
             'C#4', 'D4',
             'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5',
             'G5',
             'G#5', 'A5', 'A#5',
             'B5', 'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 'C7', 'C#7', 'D7',
             'D#7',
             'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7', 'C8']
notesVar2 = ['A0,', 'B*0', 'B0', 'C1', 'D*1', 'D1', 'E*1', 'E1', 'F1', 'G*1', 'G1', 'A*1', 'A1', 'B*1', 'B1', 'C2',
             'D*2', 'D2', 'E*2', 'E2', 'F2', 'G*2', 'G2', 'A*2', 'A2', 'B*2', 'B2', 'C3', 'D*3', 'D3', 'E*3', 'E3',
             'F3',
             'G*3', 'G3', 'A*3', 'A3', 'B*3', 'B3', 'C4', 'D*4', 'D4', 'E*4', 'E4', 'F4', 'G*4', 'G4', 'A*4', 'A4',
             'B*4', 'B4', 'C5', 'D*5', 'D5', 'E*5', 'E5', 'F5', 'G*5', 'G5', 'A*5', 'A5', 'B*5', 'B5', 'C6', 'D*6',
             'D6',
             'E*6', 'E6', 'F6', 'G*6', 'G6', 'A*6', 'A6', 'B*6', 'B6', 'C7', 'D*7', 'D7', 'E*7', 'E7', 'F7', 'G*7',
             'G7',
             'A*7', 'A7', 'B*7', 'B7', 'C8']
intervals = {
    'd2': '0',
    'm2': '1',
    'M2': '2',
    'A2': '3',
    'd3': '2',
    'm3': '3',
    'M3': '4',
    'A3': '5',
    'd4': '4',
    'P4': '5',
    'A4': '6',
    'd5': '6',
    'P5': '7',
    'A5': '8',
    'd6': '7',
    'm6': '8',
    'M6': '9',
    'A6': '10',
    'd7': '9',
    'm7': '10',
    'M7': '11',
    'A7': '12',
    'd8': '11',
    'P8': '12',
    'A8': '13'
}
wholeIntervals = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5',
                  'F5', 'G5', 'A5', 'B5', 'C5']


def key(noteNumber):
    return notesVar1[noteNumber - 1]


def num(noteName):
    if noteName[0:2] == "B#":
        return notesVar1.index("C" + str(int(noteName[-1]) + 1))
    if noteName[0:2] == "C*":
        return notesVar1.index("B" + str(int(noteName[-1]) - 1))
    if noteName[0:2] == "E#":
        return notesVar1.index("F" + str(int(noteName[-1])))
    if noteName[0:2] == "F*":
        return notesVar1.index("E" + str(int(noteName[-1])))
    if noteName in notesVar1:
        return notesVar1.index(noteName) + 1
    else:
        return notesVar2.index(noteName) + 1


def getIntervals2(interval, startingNote, octave):
    returnLists = []

    jump = int(intervals[interval])
    startingNote = startingNote + octave
    numStart = num(startingNote)
    note1 = key(jump + numStart)
    note2 = key(numStart - jump)

    strTempNotes = note1 + "|" + note2

    quality = interval[0]
    jump = interval[1]

    startNote1 = wholeIntervals[(wholeIntervals.index(startingNote[0] + octave) + int(jump) - 1)]

    startNote2 = wholeIntervals[(wholeIntervals.index(startingNote[0] + octave) - int(jump) + 1)]

    tempNote1 = strTempNotes.split('|')[0]
    tempNote2 = strTempNotes.split('|')[1]

    if startNote1 == tempNote1[0]:
        returnLists.append(startNote1)
    else:
        diff = num(tempNote1) - num(startNote1)
        if diff > 0:
            tempStartNote1 = startNote1[0]
            for i in range(diff):
                tempStartNote1 += "#"
            returnLists.append(tempStartNote1 + startNote1[1])
        else:
            tempStartNote1 = startNote1[0]
            for i in range(-1 * diff):
                tempStartNote1 += "*"
            returnLists.append(tempStartNote1 + startNote1[1])

    if startNote2 == tempNote2[0]:
        returnLists.append(startNote2)
    else:
        diff = num(tempNote2) - num(startNote2)
        if diff > 0:
            tempStartNote2 = startNote2[0]
            for i in range(diff):
                tempStartNote2 += "#"
            returnLists.append(tempStartNote2 + startNote2[1])
        else:
            tempStartNote2 = startNote2[0]
            for i in range(-1 * diff):
                tempStartNote2 += "*"
            returnLists.append(tempStartNote2 + startNote2[1])

    return returnLists



def getIntervalFromTwoNote(upNote, downNote):
    for element in intervals:

        currNote = getIntervals2(element, upNote, '4')[1]
        # gets the bottom note not top note, thus top note should be passed in

        if currNote[0] == downNote:
            return element

    return 'No interval found'


