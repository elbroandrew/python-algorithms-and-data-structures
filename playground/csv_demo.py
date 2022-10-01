import csv

mylist = ["a", "b", "c", "v", "n"]

with open("myfile.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=',')
    wr.writerow(mylist)
