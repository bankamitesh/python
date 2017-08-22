import csv
import json

def main(): 

    fname1 = "/Users/mitesh/code/bitbucket/python/untitled folder/thejesh__raw__EzllYSfO.csv"
    fname2 = "/Users/mitesh/code/bitbucket/python/data.csv"
    
    j = []

    
    f1 = open (fname1,'rU')
    f2 = open (fname2,'a')
    a = 'thejesh'
    c = 0
    d = 0    
    
    reader = csv.DictReader(f1, delimiter= " ", lineterminator='\n')
    

    for row in reader :
        
        row["Station"]=a
        f2.write(row["Station"]+","+row["Date"]+","+row["Time,timestamp,Pressure,Rain,Humidity,Temperature"]+"\n")
    
            
if __name__ == "__main__" :
    
    main() 
