def main():
    list = [1,2,3,4,5] 
    rez = []
    inmultire = 1
    for i in list:
        copy = list[:]
        
        del copy[copy.index(i)]
        
        for j in copy:
            inmultire = inmultire *j
            
        rez.append(inmultire)
        inmultire = 1
        
    
    print rez
    
main()