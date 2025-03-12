#Files

#MacOS uses / to create a path to a file

#filevariable = open(filename, mode)

#mode = w will start at the beginning which means it will override everything if there is content
#a = will continue on at the end

def main():
    file_obj = open("review.text", "r")
    # returns(): returns the file content as a string object
    content = file_obj.read(10)
    print(content)

main()