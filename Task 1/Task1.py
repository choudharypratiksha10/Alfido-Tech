import os
import shutil
import csv

try:
    filename = input("Enter text file name (with .txt): ")

    # Write
    with open(filename, "w") as file:
        data = input("Enter text to write in file: ")
        file.write(data)
    print("File written successfully.")

    # Read
    with open(filename, "r") as file:
        print("File Content:\n", file.read())

    # CSV Handling
    csv_name = input("Enter CSV file name (with .csv): ")
    with open(csv_name, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])

        for i in range(2):
            name = input("Enter name: ")
            age = input("Enter age: ")
            writer.writerow([name, age])

    print("CSV file created successfully.")

    # Rename
    new_name = input("Enter new name for text file: ")
    os.rename(filename, new_name)
    print("File renamed.")

    # Move
    folder = "new_folder"
    os.makedirs(folder, exist_ok=True)
    shutil.move(new_name, folder + "/" + new_name)
    print("File moved.")

    # Delete
    delete_file = input("Enter CSV file name to delete: ")
    os.remove(delete_file)
    print("File deleted.")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)