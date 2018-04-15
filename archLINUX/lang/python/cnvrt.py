f = open('out.txt','r+')
xleter = 0;
with open("in.txt") as ftext:
    for line in ftext:  
       for leter in line: 
       
           leter = leter.replace("\r"," ")
           f.write(leter)
       #python2