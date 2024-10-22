def ValidFileName(FileName) :
    if '.' not in FileName :
        return False
    name, extension = FileName.rsplit('.', 1)
    if extension == "txt" and name.isalnum() :
        return True
    else : 
        return False

while True :
    FileName = input("TXT File Name : ")

    if FileName.lower() == "exit" :
        print("Program is over")
        break

    if not ValidFileName(FileName) :
        print("File Name is incorrert, it must be 'name.txt', input again")
        continue

    try :
        with open(FileName, "r") as File :
            line = File.readline()
            while line:
                print(line, end="")
                line = File.readline()
            break    
    except FileNotFoundError:
        print("File not found, try again.")
        continue
