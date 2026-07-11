**Secure E-Learning Platform README file**



This file is designed to deliver instructions about how to execute the files and tests.





**Requirements**

* Python 3.14 (you may need to setup your own python PATH in Windows)



Project Files

* **course\_management.py** (Core implementation)
* **test\_course\_management.py** (Automated unit tests)
* **course\_management\_with\_demo.py** (Demonstration and integration test version)



Note: This report contains the original PowerShell commands I used to run from my IDE (Visual Studio Code), during development and testing. The command above is a a simplified version intended for general instruction from a different systems.



**Running the Unit Tests**

* Open a terminal and navigate to the project directory and run:





Run the "**test\_course\_management.py**" file.

* \& "C:\\Users\\”Your User”\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m unittest test\_course\_management.py -v



**Expected Results**

The test suite executes 15 unit tests covering:

* Course ID validation
* Student ID validation
* Capacity limits
* Duplicate enrolment prevention
* Course management operations
* Case-insensitive instructor search





Running the Demonstration file "**course\_management\_with\_demo.py**"

Simply open python course\_management\_with\_demo.py in an IDE and run





**Expected Results**

All tests should pass successfully and display an **OK** status.

The demonstration the showcases:

* Course creation
* Student enrolment
* Duplicate enrolment prevention
* Input validation
* Capacity enforcement
* Instructor search functionality

