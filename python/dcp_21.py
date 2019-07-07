def main():
    list,min_,max_,c,res= [(30,75),(0,50),(60,150),(0,150)] ,0,0,0,0
    for i in list:
        if min_ > min(i):
            min_ = min(i)
        if max_ < max(i):
            max_ = max(i)
    for i in range(min_,max_):
        for j in list:
            if i in range(j[0],j[1]) :
                c += 1
                if res <c:
                    res =c
        c = 0
    print res
   
main()