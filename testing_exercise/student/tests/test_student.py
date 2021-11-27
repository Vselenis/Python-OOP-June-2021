from unittest import TestCase
from project1.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.s = Student("Gosho")

    def test_init(self):
        s = Student("Gosho")

        self.assertEqual(s.name, "Gosho")
        self.assertEqual(s.courses, {})

    def test_init_with_courses(self):
        s = Student("Gosho", {"Python": ["note1"]})

        self.assertEqual(s.name, "Gosho")
        self.assertEqual(s.courses, {"Python": ["note1"]})

    def test_init_with_none(self):
        s = Student("Gosho", None)

        self.assertEqual(s.name, "Gosho")
        self.assertEqual(s.courses, {})

    def test_enrol_duplicate_courses(self):
        self.s.courses = {"Python": ["note1"]}
        result = self.s.enroll("Python", ["note2"])

        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(["note1", "note2"], self.s.courses["Python"])


    def test_enroll_new_courses_with_notes(self):
        result = self.s.enroll("Python", ["note1"])

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.s.courses["Python"], ["note1"])

    def test_enroll_new_courses_without_adding_notes(self):
        result = self.s.enroll("Python", ["note1"], "no")

        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.s.courses["Python"], [])

    def test_enroll_new_courses_with_adding_notes(self):
        result = self.s.enroll("Python", ["note1", "note2"], "Y")

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.s.courses["Python"], ["note1", "note2"])


    def test_enroll_in_existing_course_with_adding_notes(self):
        self.s.enroll("Python", ["note1", "note2"], "Y")
        result = self.s.enroll("Python", ["note3"], "Y")

        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.s.courses["Python"], ["note1", "note2", "note3"])

    def test_add_notes(self):
        self.s.courses = {"Python": []}
        result = self.s.add_notes("Python", "note1")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1"], self.s.courses["Python"])

    def test_add_notes_exception(self):
        with self.assertRaises(Exception) as e:
            self.s.add_notes("JS", "note_fail")
        self.assertEqual(str(e.exception), "Cannot add notes. Course not found.")
        self.assertEqual(self.s.courses, {})

    def test_leave_course(self):
        self.s.courses = {"Python": []}
        result = self.s.leave_course("Python")

        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.s.courses, {})

    def test_leave_course_exception(self):
        with self.assertRaises(Exception) as e:
            self.s.leave_course("JS")
        self.assertEqual(str(e.exception), "Cannot remove course. Course not found.")
