import csv

with open('test.csv', 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
  fields = spamreader.next()
  for row in spamreader:
    pass