# File Comparison Tool 
class FileComparator:
    def __init__(self, file1_path, file2_path):
        self.file1_path = file1_path
        self.file2_path = file2_path

    def compare_files(self):
        """Compare the two files line by line and output the differences."""
        differences = []
        
        try:
            with open(self.file1_path, 'r', encoding='utf-8') as file1:
                with open(self.file2_path, 'r', encoding='utf-8') as file2:
                
                        # enumerate is used to keep track of line numbers while comparing two files.
                        # The combination of zip() and enumerate() can be useful for processing
                        # multiple lists in parallel while also keeping track of Index.
                    for line_number, (line1, line2) in enumerate(zip(file1, file2), start=1): 
                        if line1.strip() != line2.strip():  # Compare lines after stripping whitespace
                            differences.append((line_number, line1.strip(), line2.strip()))
                
                    # Handle the case where files have different lengths
                    for remaining_line in file1:
                        differences.append((line_number, remaining_line.strip(), None))
                        line_number += 1
                    
                    for remaining_line in file2:
                        differences.append((line_number, None, remaining_line.strip()))
                        line_number += 1

        except FileNotFoundError as e:
            print(f"Error: {e}")
            return
        except PermissionError as e:
            print(f"Error: {e}")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return

        self.output_differences(differences)

    def output_differences(self, differences):
        """Output the differences in a user-friendly format."""
        if not differences:
            print("The files are identical.")
            return
        
        print("Differences found:")
        for line_number, line1, line2 in differences:
            if line1 is not None and line2 is not None:
                print(f"Line {line_number}:")
                print(f"  File 1: {line1}")
                print(f"  File 2: {line2}")
            elif line1 is None:
                print(f"Line {line_number}:")
                print(f"  File 1: [No content]")
                print(f"  File 2: {line2}")
            elif line2 is None:
                print(f"Line {line_number}:")
                print(f"  File 1: {line1}")
                print(f"  File 2: [No content]")

# Example Usage
if __name__ == "__main__":
    # Replace 'file1.txt' and 'file2.txt' with your actual file paths
    comparator = FileComparator('file1.txt', 'file2.txt')
    comparator.compare_files()