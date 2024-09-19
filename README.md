# File Comparison Tool


Problem Statement:

Develop a Python program that compares two text files(pdf) and outputs the differences between them, line by line. The program should be designed to handle large files efficiently, using context managers for file handling and object-oriented programming (OOP) concepts to organize the comparison logic.

Task to be Performed:

Implement a Class FileComparator:
Create a class named FileComparator to encapsulate the logic for comparing two text files. This class should include methods to open the files, compare their contents line by line, and output the differences.
Use Context Managers for File Handling:
Implement file handling using context managers (with statement) to ensure that the files are opened and closed properly, even if an error occurs during processing. This approach helps manage resources efficiently, especially when dealing with large files.
Define Methods for Comparison:
Within the FileComparator class, define methods such as compare_files that take the paths of two files as input and perform the comparison. This method should read the files line by line and compare corresponding lines.
If there are differences, the program should output the differing lines, possibly including the line numbers for clarity.
Handle Large Files Efficiently:
Ensure that the program is capable of handling large files by reading and comparing them line by line rather than loading the entire files into memory at once. This approach will make the program more memory-efficient.
Output the Differences:
The program should display the differences between the two files in a user-friendly format. This could include printing the differing lines from each file and indicating the line number where the difference occurs.
Additional Features (Optional):
Consider adding features such as ignoring white-space differences, case-insensitive comparison, or providing a summary of the total number of differences.
Implementation Guidelines:

Object-Oriented Design: Use OOP principles to structure the program. The FileComparator class should encapsulate all the functionality related to file comparison, making the program modular and easy to extend.
Efficiency: Focus on efficient handling of large files by processing them line by line. Avoid loading the entire file content into memory at once.
Error Handling: Implement error handling to manage issues such as file not found, permission errors, or reading errors.
