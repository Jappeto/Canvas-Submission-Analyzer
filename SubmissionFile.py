
# ----------------------------------------------------------------------
# SubmissionFile.py
# Jacob Reppeto
# 09/01/2025
# ----------------------------------------------------------------------

from __future__ import annotations

class SubmissionFile:

    # ------------------------------------------------------------------

    def __init__(self, filename: str):
        """
        takes a filename from a Canvas zip file and parses out the student name
        and the actual name of the file the student submitted.

        the filename parameter consists of a student's last name followed by a student's
        first name with no space between them. next is an underscore followed by a submission
        number, then an underscore followed by an ID for the submitted file, then an
        underscore followed by the name of the submitted file. If a student has submitted
        that file more than once, there is a dash and a number between the base name
        of the submitted file and the extension.

        Here are some examples:
        "smithjane_1234_56781234_main.py" (name: smithjane, filename: main.py)
        "smithjane_1234_56781234_main-2.py" (name: smithjane, filename: main.py)
        "smithjane_1234_56781234_test_main.py" (name: smithjane, filename: test_main.py)

        :param filename: The input filename to be parsed
        """
        fields = filename.split("_")
        # student name is just part before first underscore
        self._studentName: str = fields[0]

        # ignore fields[1] and fields[2] which are submission numbers
        # join filename back in case underscores in it
        file = "_".join(fields[3:])
        # look for extension
        periodIndex = file.rfind(".")

        # check for extension and get parts with and without extension
        if periodIndex != -1:
            extension = file[periodIndex:]
            withoutExtension = file[:periodIndex]
        else:
            extension = ""
            withoutExtension = file

        # check if there is a version number
        dashIndex = withoutExtension.find("-")
        if dashIndex != -1:
            name = withoutExtension[:dashIndex]
        else:
            name = withoutExtension

        # store the name of submitted file
        self._filename: str = f"{name}{extension}"

    def studentName(self) -> str:
        """
        :return: the last name and student name for the student who submitted the file
        such as "smithjane"
        """
        return self._studentName

    def filename(self) -> str:
        """
        :return: the actual name of the file the student submitted (such as "main.py")
        """
        return self._filename

    # ------------------------------------------------------------------

# ----------------------------------------------------------------------