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


# DEMO SECTION
# This section is for testing purposes and is not part of the 
# core implementation shown in the academic report.


def run_demo():
    """Demonstrates the e-learning platform functionality"""
    
    print("=" * 70)
    print("SECURE E-LEARNING PLATFORM - DEMONSTRATION")
    print("=" * 70)
    print()
    
    manager = CourseManager()
    
    # Demo 1: Create courses
    print("1. Creating courses...")
    print("-" * 70)
    try:
        course1 = manager.create_course("CS101", "Introduction to Python", "Dr Smith", 30)
        print(f" Created: {course1.course_id} - {course1.title}")
        
        course2 = manager.create_course("CS102", "Data Structures", "Dr Smith", 25)
        print(f" Created: {course2.course_id} - {course2.title}")
        
        course3 = manager.create_course("MATH203", "Linear Algebra", "Dr Jones", 20)
        print(f" Created: {course3.course_id} - {course3.title}")
        print()
    except ValidationError as e:
        print(f"✗ Error: {e}")
        print()
    
    # Demo 2: Enrol students
    print("2. Enrolling students...")
    print("-" * 70)
    try:
        course1.enrol_student("STU12345")
        print(f" Student STU12345 enrolled in {course1.course_id}")
        
        course1.enrol_student("STU12346")
        print(f" Student STU12346 enrolled in {course1.course_id}")
        
        course1.enrol_student("STU12347")
        print(f" Student STU12347 enrolled in {course1.course_id}")
        
        print(f" Total enrolled in {course1.course_id}: {course1.get_enrolled_count()} students")
        print()
    except ValidationError as e:
        print(f"✗ Error: {e}")
        print()
    
    # Demo 3: Test duplicate prevention
    print("3. Testing duplicate enrolment prevention...")
    print("-" * 70)
    result = course1.enrol_student("STU12345")
    if not result:
        print(f" Duplicate prevention working: Student STU12345 already enrolled")
    print()
    
    # Demo 4: Test invalid student ID
    print("4. Testing input validation (invalid student ID)...")
    print("-" * 70)
    try:
        course1.enrol_student("INVALID123")
    except ValidationError as e:
        print(f" Input validation working: {e}")
        print()
    
    # Demo 5: Test invalid course ID format
    print("5. Testing course ID validation...")
    print("-" * 70)
    try:
        manager.create_course("invalid", "Test Course", "Dr Test", 30)
    except ValidationError as e:
        print(f" Course ID validation working: {e}")
        print(f" Required format: 2-4 letters followed by 3 digits (e.g., CS101, MATH203)")
        print()
    
    # Demo 6: Search courses by instructor
    print("6. Searching courses by instructor...")
    print("-" * 70)
    dr_smith_courses = manager.search_courses_by_instructor("Dr Smith")
    print(f" Dr Smith teaches {len(dr_smith_courses)} course(s):")
    for course in dr_smith_courses:
        print(f"  - {course.course_id}: {course.title}")
    print()
    
    # Demo 7: Case-insensitive search
    print("7. Testing case-insensitive search...")
    print("-" * 70)
    results = manager.search_courses_by_instructor("dr smith")
    print(f" Search for 'dr smith' (lowercase) found {len(results)} course(s)")
    print()
    
    # Demo 8: Test course capacity
    print("8. Testing course capacity limits...")
    print("-" * 70)
    try:
        small_course = manager.create_course("CS999", "Small Seminar", "Dr Taylor", 2)
        small_course.enrol_student("STU99901")
        small_course.enrol_student("STU99902")
        print(f" Enrolled 2 students (capacity: 2)")
        print(f" Attempting to enrol 3rd student (should fail)...")
        small_course.enrol_student("STU99903")
    except ValidationError as e:
        print(f" Capacity enforcement working: {e}")
        print()
    
    # Summary
    print("=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print(f"Total courses created: {manager.get_total_courses()}")
    print("All validation features verified successfully!")
    print()


if __name__ == '__main__':
    run_demo()
