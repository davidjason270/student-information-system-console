# Student Management System (Python)

## 1. Overview

The **Student Management System** is a basic Python program that stores and manages student academic records. The system allows users to add students, record their subject marks, automatically calculate grades and GPA, generate reports, and save the data to a file so it can be used later.

This project demonstrates fundamental programming concepts and is designed for learning purposes.

---

## 2. Objectives

The main objectives of the system are to:

* Store student information
* Record subject marks
* Automatically calculate grades
* Calculate Grade Point Average (GPA)
* Display student reports
* Save and load data from a file

---

## 3. Main Features

### Add Student

Allows the user to enter:

* Student name
* Number of subjects
* Subject names
* Marks for each subject

The system automatically calculates the grade and GPA.

---

### View Students

Displays all students stored in the system including:

* Student name
* Subjects
* Marks
* Grades
* GPA

---

### Delete Student

Removes a student record from the system by selecting the student number from the list.

---

### Generate GPA Report

Displays a summary report showing each student and their GPA.

---

## 4. Grade System

| Marks    | Grade | Grade Point |
| -------- | ----- | ----------- |
| 90 – 100 | A     | 4           |
| 80 – 89  | B     | 3           |
| 70 – 79  | C     | 2           |
| 60 – 69  | D     | 1           |
| Below 60 | F     | 0           |

---

## 5. GPA Calculation

The Grade Point Average (GPA) is calculated using the formula:

**GPA = Total Grade Points ÷ Number of Subjects**

Example:

Math = B → 3
English = A → 4

GPA = (3 + 4) ÷ 2 = **3.5**

---

## 6. Data Storage

Student records are saved in a file called:

**students.json**

This file stores all student data so that it can be loaded again when the program runs.

---

## 7. Technologies Used

* Python Programming Language
* JSON File Storage
* Command Line Interface (CLI)

---

## 8. Conclusion

This project demonstrates how Python can be used to build a simple system for managing student records. It introduces key programming skills such as data structures, functions, user input, file handling, and basic calculations.
