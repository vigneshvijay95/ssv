def sorting(ssv):
  outStr = ("{name} of age {age} - Trainig batch march 2021")
  infile = open(ssv)
  trainees = []
  for line in infile:
    lineItem = line.split()
    trainees.append(lineItem)
  infile.close()
  trainees.sort()
  outfile = open("result.txt", "w")
  for trainee in trainees:
    outfile.writelines("Training batch march 2021:")
    outfile.writelines(' '.join(trainee))
    outfile.writelines('\n')
    outfile.writelines(outStr.format(name = trainee[0], age = trainee[1]))
    outfile.writelines('\n')
    print("Training batch march 2021:", trainee)
  outfile.close()
  return outStr
sorting("E:/training 2021/vignesh95/ssv/ssv.txt")