#!/usr/bin/env python3

# ----------------------------------------------------------------------
# submission.py
# Jacob Reppeto
# 09/04/2025
# ----------------------------------------------------------------------

import sys

from Roster import Roster
from Student import Student
from SubmissionFile import SubmissionFile



def main():
    # get the three filenames
    argv = sys.argv
    if len(argv) < 2:
        rosterFilename = input("enter roster filename: ")
    else:
        rosterFilename = argv[1]
    if len(argv) < 3:
        submissionFilename = input("enter submission filename: ")
    else:
        submissionFilename = argv[2]
    if len(argv) < 4:
        filesFilename = input("enter filename for expected files: ")
    else:
        filesFilename = argv[3]

#----------------------------------------------------------------------
    # create dictionary for roster and list for expected files
    rosterDict = dict()
    expectedFiles = list()

    # read in expected files
    with open(filesFilename, 'r') as file:
        for line in file:
            expectedFiles.append(line.strip())

    # read in roster and create dictionary entry for each student
    for student in Roster(rosterFilename).getStudent():
        # split name into parts
        parts = student.getName()
        firstName = parts[0]
        lastName = parts[-1]

        # create display name and key for dictionary
        displayName = " ".join(parts)
        nameKey = "".join([lastName, firstName,]).lower()

        # add entry to dictionary with copy of expected files as tuple
        rosterDict[nameKey] = (displayName, list(expectedFiles))

    # read in submission file and check against roster
    with open(submissionFilename, 'r') as file:
        for line in file:
            submittedFile = SubmissionFile(line.strip())

            # check if student in roster
            if submittedFile.studentName() in rosterDict:

                # print student name and submitted file
                display = rosterDict[submittedFile.studentName()][0]
                expected = rosterDict[submittedFile.studentName()][1]
                print(f"{display}: {submittedFile.filename()}")

                # remove submitted file from expected list if present
                if submittedFile.filename() in expected:
                    expected.remove(submittedFile.filename())


    # print missing files for each student
    print("\nmissing files:")
    for nameKey in rosterDict:
        display = rosterDict[nameKey][0]
        expected = rosterDict[nameKey][1]
        if len(expected) > 0:
            print(f"{display}: {', '.join(expected)}")

# ----------------------------------------------------------------------


if __name__ == "__main__":
    main()