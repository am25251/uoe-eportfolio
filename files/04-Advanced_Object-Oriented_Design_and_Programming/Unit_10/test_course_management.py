# test_course_management.py
import unittest
from course_management import Course, CourseManager, ValidationError


class TestCourse(unittest.TestCase):
    """Test suite for Course class"""
    
    def test_create_valid_course(self):
        """Test successful course creation"""
        course = Course("CS101", "Python Programming", "Dr Smith", 30)
        self.assertEqual(course.course_id, "CS101")
        self.assertEqual(course.title, "Python Programming")
        self.assertEqual(course.instructor, "Dr Smith")
        self.assertEqual(course.max_students, 30)
        self.assertEqual(course.get_enrolled_count(), 0)
    
    def test_invalid_course_id_raises_error(self):
        """Test invalid course ID validation"""
        with self.assertRaises(ValidationError):
            Course("invalid", "Title", "Instructor", 30)
    
    def test_empty_title_raises_error(self):
        """Test title validation"""
        with self.assertRaises(ValidationError):
            Course("CS101", "", "Dr Smith", 30)
    
    def test_whitespace_title_raises_error(self):
        """Test whitespace-only title validation"""
        with self.assertRaises(ValidationError):
            Course("CS101", "   ", "Dr Smith", 30)
    
    def test_max_students_validation(self):
        """Test max students boundary validation"""
        with self.assertRaises(ValidationError):
            Course("CS101", "Title", "Dr Smith", 0)
        with self.assertRaises(ValidationError):
            Course("CS101", "Title", "Dr Smith", 501)
    
    def test_enrol_student_success(self):
        """Test successful student enrolment"""
        course = Course("CS101", "Python", "Dr Smith", 30)
        result = course.enrol_student("STU12345")
        self.assertTrue(result)
        self.assertEqual(course.get_enrolled_count(), 1)
    
    def test_invalid_student_id_format(self):
        """Test student ID format validation"""
        course = Course("CS101", "Python", "Dr Smith", 30)
        with self.assertRaises(ValidationError):
            course.enrol_student("INVALID")
    
    def test_duplicate_enrolment_prevented(self):
        """Test duplicate enrolment prevention"""
        course = Course("CS101", "Python", "Dr Smith", 30)
        course.enrol_student("STU12345")
        result = course.enrol_student("STU12345")
        self.assertFalse(result)
    
    def test_course_capacity_enforced(self):
        """Test maximum capacity enforcement"""
        course = Course("CS101", "Python", "Dr Smith", 2)
        course.enrol_student("STU12345")
        course.enrol_student("STU12346")
        with self.assertRaises(ValidationError):
            course.enrol_student("STU12347")
    
    def test_instructor_search_case_insensitive(self):
        """Test case-insensitive instructor search"""
        manager = CourseManager()
        manager.create_course("CS101", "Python", "Dr Smith", 30)
        results = manager.search_courses_by_instructor("dr smith")
        self.assertEqual(len(results), 1)


class TestCourseManager(unittest.TestCase):
    """Test suite for CourseManager class"""
    
    def setUp(self):
        """Setup test fixture"""
        self.manager = CourseManager()
    
    def test_create_course_success(self):
        """Test course creation through manager"""
        course = self.manager.create_course("CS101", "Python", "Dr Smith")
        self.assertIsNotNone(course)
        self.assertEqual(course.course_id, "CS101")
    
    def test_duplicate_course_id_prevented(self):
        """Test duplicate prevention"""
        self.manager.create_course("CS101", "Python", "Dr Smith")
        with self.assertRaises(ValidationError):
            self.manager.create_course("CS101", "Java", "Dr Jones")
    
    def test_get_existing_course(self):
        """Test course retrieval"""
        self.manager.create_course("CS101", "Python", "Dr Smith")
        course = self.manager.get_course("CS101")
        self.assertIsNotNone(course)
        self.assertEqual(course.title, "Python")
    
    def test_get_nonexistent_course(self):
        """Test retrieval of non-existent course"""
        course = self.manager.get_course("NONEXIST")
        self.assertIsNone(course)
    
    def test_search_by_instructor(self):
        """Test instructor search functionality"""
        self.manager.create_course("CS101", "Python", "Dr Smith")
        self.manager.create_course("CS102", "Java", "Dr Smith")
        self.manager.create_course("CS103", "C++", "Dr Jones")
        results = self.manager.search_courses_by_instructor("Dr Smith")
        self.assertEqual(len(results), 2)


if __name__ == '__main__':
    unittest.main()
