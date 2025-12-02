# CS361
#Student.py
#Jacob Reppeto
# 8/22/2025

from typing import List

class Student:
    """
    Class representing a student with name, ID, class level, and email.
    """
    def __init__(self, name: List[str], studentId: str, email: str):
        self._name = name
        self._studentId = studentId
        self._email = email

    def __str__(self) -> str:
        """
        Returns a string representation of the Student object.
        """
        return f"{' '.join(self._name)},{self._studentId},{self._email}" # Format name as a single string

    def getName(self) -> List[str]:
        return self._name