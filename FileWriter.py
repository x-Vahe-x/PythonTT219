def ValidFileName(FileName):
    if '.' not in FileName:
        return False
    name, extension = FileName.rsplit('.', 1)
    return extension == "txt" and name.isalnum()

while True:
    FileName = input("TXT File Name: ")

    if FileName.lower() == "exit":
        print("Program is over")
        break

    if not ValidFileName(FileName):
        print("File Name is incorrect, it must be 'name.txt', input again")
        continue

    try:
        with open(FileName, "r") as File:
            line = File.readline()
            while line:
                print(line, end="")
                line = File.readline()
    except FileNotFoundError:
        print("File not found, try again.")
        continue

    choice = input("Do you want to write to this file or another one? (yes for this file / new for new file / exit to quit): ")

    if choice.lower() == 'exit':
        print("Program terminated.")
        break

    elif choice.lower() == 'new':
        while True:
            NewFileName = input("Enter new file name (or 'exit' to quit): ")

            if NewFileName.lower() == 'exit':
                print("Program terminated.")
                break

            if not ValidFileName(NewFileName):
                print("Invalid file format. File must be 'name.txt' with alphanumeric characters.")
                continue

            FileName = NewFileName
            break  

        if NewFileName.lower() == 'exit':
            break

    text_to_write = input("Enter the text you want to write to the file: ")

    try:
        with open(FileName, 'w') as File:
            File.write(text_to_write)
        print(f"Text successfully written to {FileName}")
    except Exception as e:
        print(f"An error occurred: {e}")
