def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
file_path = 'TASK1.PY'  # Replace with your actual file path
line_count = count_lines_in_file(file_path)
if line_count is not None:
    print(f"The file '{file_path}' has {line_count} lines.")