import csv

infile = open('employeepay.csv','r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

for record in csvfile:
    record[3] = int(record[3])
    record[4] = float(record[4])
    print('ID:', record[0])
    print('Fname:', record[1])
    print('Lname:', record[2])
    print('Salary:', record[3])
    print('Bonus:', record[4]*record[3])
    print('Total Pay:', (record[4]*record[3])+record[3])

    input()
