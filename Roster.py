#!/usr/bin/env python3

# ----------------------------------------------------------------------
# Roster.py
# Jacob Reppeto
# 05/14/2025
# ----------------------------------------------------------------------

from __future__ import annotations
from typing import List
import csv
import sys

from Student import Student

# ----------------------------------------------------------------------

class Roster:
    def __init__(self, fileName: str) -> None:
        """
        Initializes a Roster object by reading the student data from a CSV file.
        """
        self._students: List[Student] = []

        with open(fileName, "r") as file:
            rows = csv.reader(file) # Read CSV file
            next(rows) # Skip header row
            for row in rows:
                name = row[0].split() # Split full name into list
                studentId = row[1]
                email = row[3]
                student = Student(name, studentId, email) # Create Student object
                self._students.append(student) # Add Student object to list

    def __str__(self) -> str:
        """
        Returns a string representation of the Roster object.
        """
        result = ""
        for student in self._students:
            result += str(student) + "\n"
        return result

    def getStudent(self) -> List[Student]:
        return self._students

def main():
    """
    Creates a Roster object from the specified filename and prints its contents.
    """
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "roster.csv"

    roster = Roster(filename)
    print(roster)

# ----------------------------------------------------------------------


if __name__ == "__main__":
    main()