def read_and_write(file_name):
    try:
        with open(file_name, "r") as source: #source = open(file_name, "r")
            read_source = source.read()  #store read content into read_source

            target = open("write.txt", "w") #open target (write.txt) for appending

            modified = read_source.upper() #modify source content to uppercase

            target.write(modified) #write into target (write.txt)

            print("Task complete! 🎉") #confirmation on terminal

    except FileNotFoundError:
        print("File not found, check file name.")

file_name = input("Enter a file name E.g read.txt: ")
read_and_write(file_name) #call function with file_name (entered by user) as argument

