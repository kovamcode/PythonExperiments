olympians = [("John, Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open('writed_olympics.csv', "w")
outfile.write('"Name","Age","Sport"')
outfile.write('\n')

for olympian in olympians:
    #.format use when we have integers and strings, .join method when we have only strings,
    #row_string = ",".join(olympian) 
    #row_string = ','.join([olympian[0], str(olympian[1]), olympian[2]])
  
    row_string = '"{}","{}","{}"'. format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close