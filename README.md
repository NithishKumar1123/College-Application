# College-Application
A College website using Python to take user inputs as command line arguments to generate specified output file(s).

## Requirements
1. The Python code must generate an output HTML document named "output.html" and an image in the current working directory.
2. The Python program must take as input two parameters as command line arguments.
3. The first parameter is either "-s" or "-c". "-s" specifies that the second parameter is a student ID and "-c" specifies that the second parameter is a course ID.
4. The second parameter will be the corresponding student ID or course ID.
5. If the first parameter is "-s", then the second parameter should be a student ID. From the input CSV file, the program must extract marks, for each course, of the student whose ID is given as the second parameter. It must create an HTML page that displays the output in a tabular form. The table should be titled as "Student Details" and should have column headers: "Student ID", "Course ID" and "Marks". The table should also display the total marks of that student in the last row as shown.
6. If the first parameter is "-c", then the second parameter should be a course ID. The Python program must find the highest and the average marks for that course and display it on an HTML page. The title of the table must be "Course Details" and the column headers must be "Average Marks" and "Maximum Marks". The Python code must also display the histogram of marks for the given course ID.
7. The program should display an error message if there is a deviation from the expected input. For instance, if "-s" is followed by a course ID or any invalid student ID, then a message must be displayed on the HTML page.
