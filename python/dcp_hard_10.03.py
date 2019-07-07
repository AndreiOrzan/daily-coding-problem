def main():
    list = [1, 2, 0]
    list.sort()
    res = []
    
    for i in list:
        if i + 1 not in list and i + 1 > 0: 
            res.append(i + 1)
            
    print min(res)
        
main()