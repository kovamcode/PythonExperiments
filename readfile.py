fileref = open("olympics.txt", "r")
contents = fileref.read()
print(contents[:100])
fileref.close()
