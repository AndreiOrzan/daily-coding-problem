def edit_distance():
    sr1 , sr2 ,counter = "Kitten","Sitting",0
    if len(sr1) >= len(sr2):
        bigger = len(sr1)
    else:
        bigger = len(sr2)
        for i in range(bigger):
            try :
                if sr1[i] != sr2[i]:
                    counter += 1

            except:
                counter +=1
    print counter
    
edit_distance()