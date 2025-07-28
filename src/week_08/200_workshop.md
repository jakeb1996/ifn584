---
name: "Workshop notes"
---

## Design exercises

This workshop provides hands-on experiences in object-oriented design using object and sequence diagrams. These exercises emphasise the use of instance-level diagrams to demonstrate different runtime behaviours of the application, as defined by the class diagram. Sample solutions to these exercises will be available on Canvas.

---

#### Exercise A

Imagine a system that models a university’s course registration process. In our design, we have:

- **Person:** A base class for all users with common properties like `Name` and `Email`.
- **Student:** Inherits from Person and holds a student’s unique info such as `StudentId` and a list of course registrations.
- **Professor:** Inherits from Person and contains properties like `EmployeeId`, `Department`, and the list of courses taught.
- **Course:** Represents a class offering with properties like `CourseCode`, `Title`, and a description. A Course is associated with an Instructor (Professor) and is composed of many Assignments.
- **Registration:** Creates an association between a Student and a Course, where we can record details (such as a Grade) for the student.
- **Assignment:** Represents coursework within a course. With composition, an Assignment cannot exist by itself—it is an integral part of a Course.

Develop a **class diagram** to define the classes and their relationships.

---
#### Exercise B

Object diagrams help visualise a system **at a particular moment in time**. Below are two example scenarios, where each object instance (with sample attribute values) should illustrate how the classes are used at runtimes.
###### Object Diagram 1: Student Course Registration

Develop an object diagram to show a scenario where a student registers for a course taught by a professor. An assignment already exists for the course.
###### Object Diagram 2: Professor Managing Multiple Courses

Develop an object diagram to show a scenario where a professor who is teaching two courses. Each course contains one assignment.

---

#### Exercise C

Sequence diagrams illustrate the **dynamic interactions between objects over time**. Here are two significant events. 

###### Sequence Diagram 1: Student Course Registration

In this scenario, a Student performs the registration for a Course by calling its `RegisterForCourse` method. Internally, the Student object creates a new `Registration` and then adds it to the Course and itself.
###### Sequence Diagram 2: Professor Posting an Assignment

In this scenario, a new Assignment is created and a Professor posts the assignment to a course.

---

#### Exercise D (optional)

Develop a sample C# implementation based on the above design. 