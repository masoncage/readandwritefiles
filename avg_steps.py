import csv

outfile = open('avg_steps.csv','w')
infile = open('steps.csv','r')
csvfile = csv.reader(infile, delimiter=',')

January = 0
February = 0 
March = 0 
April = 0 
May = 0 
June = 0 
July = 0 
August = 0 
September = 0 
October = 0 
November = 0 
December = 0 
Feb_Count = 0

next(csvfile)
for record in csvfile:
    record[0]=int(record[0])
    record[1]=int(record[1])
    if(record[0] == 1):
        January += record[1]
    January1 = January/31
    January1 = int(January1)
    if(record[0] == 2):
        February += record[1]
    February1 = February/28
    February1 = int(February1)
        #Feb_Count += 1    
    #Feb_Count = int(Feb_Count)  
    #February1 = February/Feb_Count
    #February1 = int(February1)
    if (record[0] == 3):
        March += record[1]
    March1 = March/31
    March1 = int(March1)
    if (record[0] == 4):
        April += record[1]
    April1 = April/30
    April1 = int(April1)
    if (record[0] == 5):
        May += record[1]
    May1 = May/31
    May1 = int(May1)
    if (record[0]== 6):
        June += record[1]
    June1 = June/30
    June1 = int(June1)
    if (record[0] == 7):
        July += record[1]
    July1 = July/31
    July1 = int(July1)
    if (record[0] == 8):
        August += record[1]
    August1 = August/31
    August1 = int(August1)
    if (record[0] == 9):
        September += record[1]
    September1 = September/30
    September1 = int(September1)
    if (record[0] == 10):
        October += record[1]
    October1 = October/31
    October1 = int(October1)
    if(record[0] == 11):
        November += record[1]
    November1 = November/30
    November1 = int(November1)
    if(record[0] == 12):
        December += record[1]
    December1 = December/31
    December1 = int(December1)

January1 = str(January1)
February1 = str(February1)
March1 = str(March1)
April1 = str(April1)
May1 = str(May1)
June1 = str(June1)
July1 = str(July1)
August1 = str(August1)
September1 = str(September1)
October1 = str(October1)
November1 = str(November1)
December1 = str(December1)

outfile.write('January:' + January1 + '\n')
outfile.write('February:' + February1+ '\n')
outfile.write('March:' + March1 + '\n')
outfile.write('April:' + April1+ '\n')
outfile.write('May:' + May1 + '\n')
outfile.write('June:' + June1 + '\n')
outfile.write('July:' + July1 + '\n')
outfile.write('August:' + August1 + '\n')
outfile.write('September:' + September1 + '\n')
outfile.write('October:' + October1 + '\n')
outfile.write('November:' + November1 + '\n')
outfile.write('December:' + December1 + '\n')



#print(January1)
#print(February1)
#print(Feb_Count)
#print(March1)