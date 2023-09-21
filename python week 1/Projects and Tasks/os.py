import os


folder_name = input("Enter the name of the folder: ")

if os.path.exists(folder_name):
    print(f"The folder '{folder_name}' already exists.")
else:
    try:

        os.mkdir(folder_name)
        print(f"folder '{folder_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

