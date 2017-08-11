import csv
import json
import cgi
import cgitb
cgitb.enable()

def main(): 

    fname1 = "/Users/mitesh/Documents/Python/atree01__raw__3ILnGc6S.csv"
    fname2="/Users/mitesh/Documents/Python/parsed.json"
    j = []

    
    f1 = open (fname1,'rU')
    f2 = open (fname2,'w')
    form = cgi.FieldStorage()
    a =  form.getvalue('searchbox')
    c=0
    d=0    
    reader = csv.DictReader(f1, delimiter=",", lineterminator='\n')
    

    for row in reader :
            
            
            del(row["timestamp"])
            del(row["wdc"])
            del(row["Temperature"])
            del(row["WS"])
            del(row["pyra"])
            del(row["Humidity"])
            del(row["Pressure"])
            row["Station"]=a
            j.append(row)
            c=c+1
    f2.write('[\n')
    for row in j : 

        json.dump(row,f2)
        if(d!=c-1):
         f2.write(',')
        f2.write('\n')
        d=d+1
    f2.write(']')
            
if __name__ == "__main__" :
    main() 
