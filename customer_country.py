
import csv

outfile = open('customer_country.csv', 'w')
infile = open('customers.csv','r')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile)
outfile.write('Full Name: Country:'+'\n')
for record in csvfile:
    outfile.write(record[1]+ ' '+record[2]+'   '+record[4]+'\n') 
    




    












