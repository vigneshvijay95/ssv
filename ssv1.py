def sort(trainees):
  return trainees.sort()

def writeToFile(filePath, trainees):
  outStr = ("{name} of age {age} - Trainig batch march 2021")
  outfile = open(filePath, "w")
  for trainee in trainees:
    outfile.writelines("Training batch march 2021:")
    outfile.writelines(' '.join(trainee))
    outfile.writelines('\n')
    outfile.writelines(outStr.format(name = trainee[0], age = trainee[1]))
    outfile.writelines('\n')
    print("Training batch march 2021:", trainee)
  outfile.close()

def readData(filePath):
  infile = open(filePath)
  trainees = []
  for line in infile:
    lineItem = line.split()
    trainees.append(lineItem)
  infile.close()
  return trainees

def processFile(ipFile, outputFile):
  trainees = readData(ipFile)
  sort(trainees)
  writeToFile(outputFile, trainees)

processFile("E:/training 2021/vignesh95/ssv/ssv.txt", "result.txt")