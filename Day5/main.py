from myexperiance.administration import fileoperation, excel

file_path = r"C:\Users\Ziyad\Desktop\pythoniti\day5\test.txt"

fileoperation.write_file(file_path, "Hello, World!")

fileoperation.append_file(file_path, "\nThis is an appended line.")

fileoperation.read_file(file_path)

fileoperation.read_and_write_file(file_path, "\nThis is new content.")

excel_file = r"C:\Users\Ziyad\Desktop\pythoniti\day5\test.xlsx"

# Excel Data
data = [
    ["Name", "Age"],
    ["Alice", 25],
    ["Bob", 30]
]

# Write to an Excel file
excel.write_excel(excel_file, "Sheet1", data)

# Read from the Excel file
excel_data = excel.read_excel(excel_file, "Sheet1")
print("Excel Data:", excel_data)
