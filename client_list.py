def main():
    infile = open('clients.txt', 'r')

    #count = 1 
    counter = 1 
    for line in infile:
        #count +=1 
        print(counter,". ", line.rstrip('\n'),sep='')

        counter +=1
    infile.close()    

main()
