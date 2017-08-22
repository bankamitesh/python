import csv
import json

def main(): 

    fname1 = "/Users/mitesh/code/bitbucket/python/data.csv"
    fname2 = "/Users/mitesh/code/bitbucket/python/parsed.json"
    
    j = []

    
    f1 = open (fname1,'rU')
    f2 = open (fname2,'w')
    c = 0
    d = 0    
    
    reader = csv.DictReader(f1, delimiter=",", lineterminator='\n')
    

    for row in reader :
        
        j.append(row)
        c=c+1
    f2.write('{\n')
    f2.write('"type": "FeatureCollection",\n')
    f2.write('"features": [\n')
    
    for row in j : 

        f2.write('{ "type": "Feature", "properties": ')
        json.dump(row,f2)
        f2.write('}')
        
        if(d!=c-1):
            f2.write(',')
        
        f2.write('\n')
        d=d+1
    
    f2.write(']\n}')
            
if __name__ == "__main__" :
    
    main() 
