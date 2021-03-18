import csv
with open ('vignesh1.txt',mode='r') as csv_file:
    read_content=csv.reader(csv_file,delimiter ="," )
    next(read_content) # skip the header
    for line in read_content:
        print(line[0]) # print the 0th index element
        print(line) # print all elements
with open ('vignesh2.txt',mode='w') as csv_file:
    new_content=csv.writer(csv_file)
    for line in read_content:
        new_content.writerow(line)
    
