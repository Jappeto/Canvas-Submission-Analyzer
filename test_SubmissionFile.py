import unittest
from submission.SubmissionFile import SubmissionFile

class TestSubmissionFile(unittest.TestCase):

    def test_basic_filename(self):
        # Case: "smithjane_1234_56781234_main.py"
        s = SubmissionFile("smithjane_1234_56781234_main.py")
        self.assertEqual(s.studentName(), "smithjane")
        self.assertEqual(s.filename(), "main.py")

    def test_filename_with_resubmission(self):
        # Case: "smithjane_1234_56781234_main-2.py"
        s = SubmissionFile("smithjane_1234_56781234_main-2.py")
        self.assertEqual(s.studentName(), "smithjane")
        self.assertEqual(s.filename(), "main.py")

    def test_filename_with_prefix(self):
        # Case: "smithjane_1234_56781234_test_main.py"
        s = SubmissionFile("smithjane_1234_56781234_test_main.py")
        self.assertEqual(s.studentName(), "smithjane")
        self.assertEqual(s.filename(), "test_main.py")

    def test_different_student_and_file(self):
        # Case: "doejohn_4321_9999_project.py"
        s = SubmissionFile("doejohn_4321_9999_project.py")
        self.assertEqual(s.studentName(), "doejohn")
        self.assertEqual(s.filename(), "project.py")

    def test_resubmission_with_higher_number(self):
        # Case: "doejohn_4321_9999_project-5.py"
        s = SubmissionFile("doejohn_4321_9999_project-5.py")
        self.assertEqual(s.studentName(), "doejohn")
        self.assertEqual(s.filename(), "project.py")

    def test_filename_with_multiple_words(self):
        # Case: "annasmith_9876_1234_final_report.py"
        s = SubmissionFile("annasmith_9876_1234_final_report.py")
        self.assertEqual(s.studentName(), "annasmith")
        self.assertEqual(s.filename(), "final_report.py")

    def test_filename_with_multiple_words_and_resubmission(self):
        # Case: "annasmith_9876_1234_final_report-3.py"
        s = SubmissionFile("annasmith_9876_1234_final_report-3.py")
        self.assertEqual(s.studentName(), "annasmith")
        self.assertEqual(s.filename(), "final_report.py")

    def test_filename_with_different_extension(self):
        # Case: "brownchris_5555_8888_essay.pdf"
        s = SubmissionFile("brownchris_5555_8888_essay.pdf")
        self.assertEqual(s.studentName(), "brownchris")
        self.assertEqual(s.filename(), "essay.pdf")

if __name__ == "__main__":
    unittest.main()
