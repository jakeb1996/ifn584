---
name: "Workshop notes"
---

## Programming exercises

The exercises in this workshop will cover file handling mechanisms in C# with file and stream classes. The coding solutions to these exercises will be made available on Canvas, enabling you to validate your own solutions upon completion.

#### Exercise A

Create a program named `DirectoryInformation` that allows a user to continually enter directory names until the user types `end`. If the directory name exists, display a list of the files in it; otherwise, display a message indicating the directory does not exist. Create as many test directories and files as necessary to test your program.

#### Exercise B

Create a program named `FileComparison` that compares two files. First, use a text editor such as Notepad to save your favourite movie quote. Next, copy the file contents and paste them into a word-processing program such as Microsoft Word. Then, write the file-comparison application, which displays the sizes of the two files as well as the ratio of their sizes to each other. To discover a file’s size, you can create a `System.IO.FileInfo` object using statements such as the following, where `FILE_NAME` is a string that contains the name of the file and `size` has been declared as an integer:

```cs
FileInfo fileInfo = new FileInfo(FILE_NAME);
size = fileInfo.Length;
```

#### Exercise C

1. Create a program named `WritePatientRecords` that allows a doctor’s staff to enter data about patients and saves the data to a file. Create a `Patient` class that contains fields for an ID number, name, and current balance owed to the doctor’s office.
2. Create a program named `ReadPatientRecords` that reads the file created in Exercise C1 and displays each patient’s data on the screen.
3. Create a program named `FindPatientRecords` that prompts the user for an ID number, reads the file created in Exercise C1, and displays data for the specified record.
4. Create a program named `FindPatientRecords2` that prompts the user for a minimum balance due, reads the file created in Exercise C1, and displays all the records containing a balance greater than or equal to the entered value.