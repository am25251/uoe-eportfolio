# course_management.py
import re
from typing import List, Optional
from datetime import datetime, timezone


class ValidationError(Exception):
    """Custom exception for input validation errors"""
    pass


class Course:
    """Represents an educational course with input validation"""
    
    def __init__(self, course_id: str, title: str, 
                 instructor: str, max_students: int = 50):
        self._validate_inputs(course_id, title, instructor, max_students)
        self._course_id = course_id
        self._title = title
        self._instructor = instructor
        self._max_students = max_students
        self._enrolled_students: List[str] = []
        self._created_date = datetime.now(timezone.utc)
    
    @staticmethod
    def _validate_inputs(course_id: str, title: str, 
                        instructor: str, max_students: int):
        """Validates course inputs"""
        if not course_id or not re.match(r'^[A-Z]{2,4}[0-9]{3}$', course_id):
            raise ValidationError("Invalid course ID format")
        if not title or len(title.strip()) < 3:
            raise ValidationError("Title must be at least 3 characters")
        if not instructor or len(instructor.strip()) < 2:
            raise ValidationError("Invalid instructor name")
        if max_students < 1 or max_students > 500:
            raise ValidationError("Max students must be between 1 and 500")
    
    def enrol_student(self, student_id: str) -> bool:
        """Enrols student with validation"""
        if not re.match(r'^STU[0-9]{5}$', student_id):
            raise ValidationError("Invalid student ID format")
        if student_id in self._enrolled_students:
            return False
        if len(self._enrolled_students) >= self._max_students:
            raise ValidationError("Course is full")
        self._enrolled_students.append(student_id)
        return True
    
    def get_enrolled_count(self) -> int:
        """Returns current enrolment count"""
        return len(self._enrolled_students)
    
    @property
    def course_id(self) -> str:
        return self._course_id
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def instructor(self) -> str:
        return self._instructor
    
    @property
    def max_students(self) -> int:
        return self._max_students


class CourseManager:
    """Manages multiple courses with validated operations"""
    
    def __init__(self):
        self._courses = {}
    
    def create_course(self, course_id: str, title: str, 
                      instructor: str, max_students: int = 50) -> Course:
        """Creates new course with duplicate prevention"""
        if course_id in self._courses:
            raise ValidationError("Course ID already exists")
        course = Course(course_id, title, instructor, max_students)
        self._courses[course_id] = course
        return course
    
    def get_course(self, course_id: str) -> Optional[Course]:
        """Retrieves course by ID"""
        return self._courses.get(course_id)
    
    def search_courses_by_instructor(self, instructor: str) -> List[Course]:
        """Searches courses by instructor name (case-insensitive)"""
        return [c for c in self._courses.values() 
                if c.instructor.lower() == instructor.lower()]
    
    def get_total_courses(self) -> int:
        """Returns total number of courses"""
        return len(self._courses)
